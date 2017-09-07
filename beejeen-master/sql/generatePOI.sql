drop table if exists poitmp;
create table poitmp
select Sight.name_cn as poi, Country.name_cn as country, Country.id as id, City.name_cn as city, 'Sight' as type, (case when Sight.img_link is null or Sight.img_link = '' then '' else 'YES' end) as image, (case when Sight.video_link is null or Sight.video_link = '' then '' else 'YES' end) as video from Sight join Country on Country.id = Sight.countryid join City on City.id = Sight.cityid
union
select Hotel.name_cn as poi, Country.name_cn as country, Country.id as id, City.name_cn as city, 'Hotel' as type, (case when Hotel.img_link is null or Hotel.img_link = '' then '' else 'YES' end) as image, (case when Hotel.video_link is null or Hotel.video_link = '' then '' else 'YES' end) as video from Hotel join Country on Country.id = Hotel.countryid join City on City.id = Hotel.cityid
union
select Activity.name_cn as poi, Country.name_cn as country, Country.id as id, City.name_cn as city, 'Activity' as type, (case when Activity.img_link is null or Activity.img_link = '' then '' else 'YES' end) as image, (case when Activity.video_link is null or Activity.video_link = '' then '' else 'YES' end) as video from Activity join Country on Country.id = Activity.countryid join City on City.id = Activity.cityid
union
select Restaurant.name_cn as poi, Country.name_cn as country, Country.id as id, City.name_cn as city, 'Restaurant' as type, (case when Restaurant.img_link is null or Restaurant.img_link = '' then '' else 'YES' end) as image, (case when Restaurant.video_link is null or Restaurant.video_link = '' then '' else 'YES' end) as video from Restaurant join Country on Country.id = Restaurant.countryid join City on City.id = Restaurant.cityid order by id;

alter table poitmp drop column id;

alter table poitmp add column id int;

alter table poitmp change id id int AUTO_INCREMENT PRIMARY KEY first;
