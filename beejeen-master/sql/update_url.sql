delete from tmp;
LOAD DATA LOCAL INFILE '%fileName%' INTO TABLE tmp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

update Country join tmp on replace(Country.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 6), '/', -1) and substring_index(substring_index(tmp.url, '/', 5), '/', -1)=concat('Thumb%20', replace(Country.name_en, ' ', '%20')) and substring_index(substring_index(tmp.url, '/', 7), '/', -1)='vtour' set Country.rep_link=tmp.url;

update Country join tmp on replace(Country.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 6), '/', -1) and substring_index(substring_index(tmp.url, '/', 5), '/', -1)=replace(Country.name_en, ' ', '%20') and substring_index(tmp.url, '.', -1)!='mp3' set Country.img_link=tmp.url;

update Country join tmp on replace(Country.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 6), '/', -1) and substring_index(substring_index(tmp.url, '/', -1), '.', 1)=concat('Thumb%20', replace(Country.name_en, ' ', '%20')) set Country.thumb_link=tmp.url;

update Country join tmp on replace(Country.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(tmp.url, '.', -1)='mp3' set Country.music_link=tmp.url;

update Country join tmp on replace(Country.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(substring_index(tmp.url, '/', 5), '/', -1)='video_utovr' and tmp.url not like '%Thumb%' set Country.video_link=tmp.url;

update Country join tmp on replace(Country.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(substring_index(tmp.url, '/', 5), '/', -1)='video_utovr' and tmp.url like '%Thumb%' set Country.rep_link=tmp.url;

update City join tmp on replace(City.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 6), '/', -1) and substring_index(substring_index(tmp.url, '/', -1), '.', 1)=concat('Thumb%20', replace(City.name_en, ' ', '%20')) set City.thumb_link=tmp.url;

update City join tmp on replace(City.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 6), '/', -1) and substring_index(substring_index(tmp.url, '/', 7), '/', -1)='vtour' set City.rep_link=tmp.url;

update City join tmp on replace(City.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 6), '/', -1) and substring_index(substring_index(tmp.url, '/', 7), '/', -1)=replace(City.name_en, ' ', '%20') and substring_index(tmp.url, '.', -1)!='mp3' set City.img_link=tmp.url;

update City join tmp on replace(City.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(tmp.url, '.', -1)='mp3' set City.music_link=tmp.url;

update City join tmp on replace(City.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(substring_index(tmp.url, '/', 5), '/', -1)='video_utovr' and tmp.url not like '%Thumb%' set City.video_link=tmp.url;

update City join tmp on replace(City.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(substring_index(tmp.url, '/', 5), '/', -1)='video_utovr' and tmp.url like '%Thumb%' set City.rep_link=tmp.url;

update Activity join tmp on replace(Activity.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 8), '/', -1) and substring_index(substring_index(tmp.url, '/', -1), '.', 1)=concat('Thumb%20', replace(Activity.name_en, ' ', '%20')) set Activity.thumb_link=tmp.url;
update Hotel join tmp on replace(Hotel.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 8), '/', -1) and substring_index(substring_index(tmp.url, '/', -1), '.', 1)=concat('Thumb%20', replace(Hotel.name_en, ' ', '%20')) set Hotel.thumb_link=tmp.url;
update Restaurant join tmp on replace(Restaurant.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 8), '/', -1) and substring_index(substring_index(tmp.url, '/', -1), '.', 1)=concat('Thumb%20', replace(Restaurant.name_en, ' ', '%20')) set Restaurant.thumb_link=tmp.url;
update Sight join tmp on replace(Sight.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 8), '/', -1) and substring_index(substring_index(tmp.url, '/', -1), '.', 1)=concat('Thumb%20', replace(Sight.name_en, ' ', '%20')) set Sight.thumb_link=tmp.url;

update Activity join tmp on replace(Activity.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 8), '/', -1) and substring_index(substring_index(tmp.url, '/', 9), '/', -1)='vtour' set Activity.img_link=tmp.url;
update Hotel join tmp on replace(Hotel.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 8), '/', -1) and substring_index(substring_index(tmp.url, '/', 9), '/', -1)='vtour' set Hotel.img_link=tmp.url;
update Restaurant join tmp on replace(Restaurant.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 8), '/', -1) and substring_index(substring_index(tmp.url, '/', 9), '/', -1)='vtour' set Restaurant.img_link=tmp.url;
update Sight join tmp on replace(Sight.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', 8), '/', -1) and substring_index(substring_index(tmp.url, '/', 9), '/', -1)='vtour' set Sight.img_link=tmp.url;

update Activity join tmp on replace(Activity.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(substring_index(tmp.url, '/', 5), '/', -1)='video_utovr' set Activity.video_link=tmp.url;
update Hotel join tmp on replace(Hotel.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(substring_index(tmp.url, '/', 5), '/', -1)='video_utovr' set Hotel.video_link=tmp.url;
update Restaurant join tmp on replace(Restaurant.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(substring_index(tmp.url, '/', 5), '/', -1)='video_utovr' set Restaurant.video_link=tmp.url;
update Sight join tmp on replace(Sight.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(substring_index(tmp.url, '/', 5), '/', -1)='video_utovr' set Sight.video_link=tmp.url;

update Activity join tmp on replace(Activity.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(tmp.url, '.', -1)='mp3' set Activity.music_link=tmp.url;
update Hotel join tmp on replace(Hotel.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(tmp.url, '.', -1)='mp3' set Hotel.music_link=tmp.url;
update Restaurant join tmp on replace(Restaurant.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(tmp.url, '.', -1)='mp3' set Restaurant.music_link=tmp.url;
update Sight join tmp on replace(Sight.name_en, ' ', '%20')=substring_index(substring_index(tmp.url, '/', -1), '.', 1) and substring_index(tmp.url, '.', -1)='mp3' set Sight.music_link=tmp.url;
