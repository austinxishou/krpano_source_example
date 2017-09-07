delete from tmp;
LOAD DATA LOCAL INFILE '%fileName%' INTO TABLE tmp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

update Chosen join tmp on substring_index(substring_index(tmp.url, '/', -1), '.', 1)=concat("Thumb%20", replace(Chosen.name_en, ' ', '%20')) and substring_index(substring_index(tmp.url, '/', 5), '/', -1)='Chosen' and substring_index(substring_index(tmp.url, '/', 6), '/', -1)!='mobile' set Chosen.thumb_link=tmp.url;

update Chosen join tmp on substring_index(substring_index(tmp.url, '/', -1), '.', 1)=concat("Thumb%20", replace(Chosen.name_en, ' ', '%20')) and substring_index(substring_index(tmp.url, '/', 5), '/', -1)='Chosen' and substring_index(substring_index(tmp.url, '/', 6), '/', -1)='mobile' set Chosen.thumb_mobile_link=tmp.url;
