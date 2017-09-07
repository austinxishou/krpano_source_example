delete from tmp;
LOAD DATA LOCAL INFILE '%fileName%' INTO TABLE tmp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

update Travel join tmp on substring_index(substring_index(tmp.url, '/', -1), '.', 1)=concat("Thumb%20", replace(Travel.name_en, ' ', '%20')) and tmp.url not like '%mobile%' set Travel.thumb_link=tmp.url;
update Travel join tmp on substring_index(substring_index(tmp.url, '/', -1), '.', 1)=concat("Thumb%20", replace(Travel.name_en, ' ', '%20')) and tmp.url like '%mobile%' set Travel.thumb_mobile_link=tmp.url;
