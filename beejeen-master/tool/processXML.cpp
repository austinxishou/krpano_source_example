#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>

using std::cout;
using std::endl;
using std::string;
using std::ios;


int main(int argc, char ** argv)
{
	std::ifstream fin(argv[1]);
	string tmp;
	string content;
	getline(fin, tmp);
	std::size_t index1, index2;
	// kill windows carriage return
	if (tmp.back() == 13)
	{
		tmp.back() = '\n';
	}
	else
	{
		tmp += '\n';
	}
	// remove the content of title
	index2 = tmp.find_last_of("\"");
	index1 = tmp.find_last_of("\"", index2 - 1);
	content = tmp.substr(0, index1 + 1) + tmp.substr(index2);
	string head("\t<include url=\"");
	int num = std::stoi(argv[2]);
	for (int i = 0; i <= num; i++)
	{
		head += "..\/";
	}
	head += "common\/";

	bool done = false;
	// add automatic rotation
	while(getline(fin, tmp))
	{
		if (tmp.length() > 1)
		{
			if (tmp.back() == 13)
			{
				tmp.back() = '\n';
			}
			else
			{
				tmp += '\n';
			}
			if (tmp.find("<autorotate") != string::npos)
			{
				continue;
			}
			if (tmp.find("vtourskin") != string::npos && tmp.find("..\/") == string::npos)
			{
				if (argc == 4)
				{
					continue;
				}
				tmp = head + "skin\/vtourskin.xml\" \/>\n";
			}
			//if (tmp.find("dm.xml") != string::npos)
			//{
			//	done = true;
			//}
			if (tmp.find("<!") != string::npos)
			{
				if (argc == 4)
				{
					content += ("\t<autorotate enabled=\"true\"  waittime=\"0\" speed=\"-2.5\"  horizon=\"0.0\" tofov=\"120.0\" \/>\n");
				}
				else
				{
					//if (!done)
					//{
					//	content += (head + "dm.xml\"\/>\n\t<autorotate enabled=\"true\"  waittime=\"0\" speed=\"-2.5\"  horizon=\"0.0\" tofov=\"120.0\" \/>\n");
					//}
					//else
					//{
						content += ("\t<autorotate enabled=\"true\"  waittime=\"0\" speed=\"-2.5\"  horizon=\"0.0\" tofov=\"120.0\" \/>\n");
						content += (head + "comment/plugin/comment/xml/plugin.xml\" />\n");
					//}
				}
				content += tmp;
				break;
			}
			content += tmp;
		}
	}
	// remove google earch icon
	while(getline(fin, tmp))
	{
		if (tmp.length() > 1)
		{
			if (tmp.back() == 13)
			{
				tmp.back() = '\n';
			}
			else
			{
				tmp += '\n';
			}
			if (tmp.find("maps=") != string::npos)
			{
				content += "\t<skin_settings maps= \"false\"\n";
				break;
			}
			content += tmp;
		}
	}
	// set thumbs_opened = true
	if (argc == 3)
	{
		while(getline(fin, tmp))
		{
			if (tmp.length() > 1)
			{
				if (tmp.back() == 13)
				{
					tmp.back() = '\n';
				}
				else
				{
					tmp += '\n';
				}
				if (tmp.find("opened") != string::npos)
				{
					content += "\tthumbs_opened= \"true\"\n";
					break;
				}
				content += tmp;
			}
		}
	}
	// set transparency of tool bar
	while(getline(fin, tmp))
	{
		if (tmp.length() > 1)
		{
			if (tmp.back() == 13)
			{
				tmp.back() = '\n';
			}
			else
			{
				tmp += '\n';
			}
			if (tmp.find("bgcolor") != string::npos)
			{
				content += "\tdesign_bgcolor=\"0x000000\"\n";
				continue;
			}
			if (tmp.find("bgalpha") != string::npos)
			{

				content += "\tdesign_bgalpha=\"0.7\"\n";
				break;
			}
			content += tmp;
		}
	}
	std::map<int, string> scenes;
	bool b = false;
	int key;
	string title;
	// make all of scenes in order
	while(getline(fin, tmp))
	{
		if (tmp.find("<\/krpano") != string::npos)
		{
			break;
		}
		if (tmp.length() > 1)
		{
			if (tmp.back() == 13)
			{
				tmp.back() = '\n';
			}
			else
			{
				tmp += '\n';
			}
			if (tmp.find("<scene") != string::npos)
			{
				index1 = tmp.find("_");
				index2 = tmp.find("_", index1 + 1);
				try
				{
					key = std::stoi(tmp.substr(index1 + 1, index2 - index1 - 1));
					index1 = tmp.find("title");
					index1 = tmp.find("\"", index1);
					index2 = tmp.find(" ", index1 + 1);
					title = tmp.substr(index1 + 1, index2 - index1 - 1);
					if (std::any_of(title.begin(), title.end(), ::isdigit))
					{
						scenes[key] = tmp.substr(0, index1 + 1) + tmp.substr(index2 + 1);
					}
					else
					{
						scenes[key] = tmp;
					}
				}catch(...)
				{
					// Name doesn't contain number, which means that this is a single picture.
					key = 0;
					scenes[key] = tmp;
				}
				b = true;
			}
			else if (tmp.find("<\/scene") != string::npos)
			{
				scenes[key] += tmp;
				b = false;
			}
			else if (b)
			{
				scenes[key] += tmp;
			}
			else
			{
				content += tmp;
			}
		}
	}

	for(const auto & i : scenes)
	{
		content += i.second;
	}

	content += "<\/krpano>";

	fin.close();

	std::ofstream fout(argv[1], ios::out | ios::trunc);

	fout << content;


	return EXIT_SUCCESS;
}
