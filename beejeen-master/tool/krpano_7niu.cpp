#include <iostream>
#include <thread>
#include <atomic>
#include <mutex>
#include <condition_variable>
#include <stdlib.h>
#include <set>
#include <vector>
#include <algorithm>
#include <chrono>
#include <experimental/filesystem>
#include "ThreadPool.h"

#include <signal.h>


using std::string;



static ThreadPool tp(5);
static std::vector<std::future<string>> results;
static std::set<std::string> files;

static std::mutex mtx;
static std::condition_variable cond_var;

static std::atomic_bool done{false};
static bool stopCondVar = false;


// param file is enclosed by a quotation mark
string execute(const string & file)
{
	std::cout<<"executing: "<<file<<std::endl;

	size_t len = file.find_last_of('_') - file.find_first_of(' ') - 1;
	string country = file.substr(17, len);
	string continent = file.substr(file.find_last_of('_') + 1);
	continent.pop_back();
	std::transform(continent.begin(), continent.end(), continent.begin(), ::tolower);
	std::cout<<"country: "<<country<<std::endl;
	std::cout<<"continent: "<<continent<<std::endl;

	string cmd;

	cmd = string("cp -r ./* ../media/") + file;
	system(cmd.c_str());

	cmd = string("rm -rf ") + file + "/common";
	system(cmd.c_str());

	cmd = string("cd ../media/") + file;
	system(cmd.c_str());

	std::cout<<"generate krpano: "<<file<<std::endl;
	cmd = string("./krpano.sh ") + file.c_str() + "/\"Backup " + country +"\"";
	system(cmd.c_str());
	std::cout<<"krpano done"<<file<<std::endl;

	cmd = file + "/main.sh \"" + country + "\" init";
	system(cmd.c_str());
	

//	continent = "test"; /////////////////////////////////////////

	cmd = file + "/main.sh \"" + country + "\" " + continent +  " upload";
	system(cmd.c_str());

	cmd = string("../sql/main.sh \"") + continent + " url";
	system(cmd.c_str());

	cmd = string("rm -rf ") + file;
	//cmd = string("mv ") + file + " ~/";
	system(cmd.c_str());
//	std::cout<<file<<" removed"<<std::endl;
	std::cout<<file<<" doneeeeeeeeeeeeeeeeeeeeeeeeeee"<<std::endl;
	return file;
}

void search()
{
	while(!done)
	{
		//std::cout<<"searching..."<<std::endl;
		std::this_thread::sleep_for(std::chrono::seconds(2));
		std::string path = "../media";
		std::unique_lock<std::mutex> ulock(mtx);
		for (const auto & p : std::experimental::filesystem::directory_iterator(path))
		{
			std::ostringstream oss;
			oss << p;
			string tmp = oss.str();
			//std::cout<<tmp<<std::endl;
			if (std::find(files.begin(), files.end(), tmp) == files.end() && std::experimental::filesystem::is_directory(p) && tmp.rfind("\"../media/Backup", 0) != string::npos)
			{
				files.insert(tmp);
				std::cout<<"enqueue "<<tmp<<std::endl;
				results.emplace_back(tp.enqueue(execute, tmp));
				cond_var.notify_one();
			}
		}
		ulock.unlock();
	}
}

void process()
{
	while(!done)
	{
	//	std::cout<<"processing..."<<std::endl;
		std::this_thread::sleep_for(std::chrono::seconds(2));
		std::unique_lock<std::mutex> ulock(mtx);
		while(results.empty() && !stopCondVar)
		{
			cond_var.wait(ulock);
		}
		for(auto && it = results.begin(); it != results.end();)
		{
			if (it->wait_for(std::chrono::seconds(0)) == std::future_status::ready)
			{
				// the function execute will return the file name, which is stored in results
				files.erase(it->get());
				it = results.erase(it);
			}
			else
			{
				++it;
			}
		}
		ulock.unlock();
	}
}

static std::thread s(search);
static std::thread p(process);


void finish(int ps)
{
	done = true; 
	stopCondVar = true;
	cond_var.notify_one();
	s.detach();
	p.detach();
}



int main()
{
//	std::thread s(search);
//	std::thread p(process);

	signal(SIGINT, finish);

	s.join();
//	p.join();

	return 0;
}

