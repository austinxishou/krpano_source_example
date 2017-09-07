LOAD DATA LOCAL INFILE 'country.csv' INTO TABLE Country FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;
LOAD DATA LOCAL INFILE 'city.csv' INTO TABLE City FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;
LOAD DATA LOCAL INFILE 'activity.csv' INTO TABLE Activity FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;
LOAD DATA LOCAL INFILE 'restaurant.csv' INTO TABLE Restaurant FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;
LOAD DATA LOCAL INFILE 'hotel.csv' INTO TABLE Hotel FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;
LOAD DATA LOCAL INFILE 'sight.csv' INTO TABLE Sight FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;
LOAD DATA LOCAL INFILE 'travel.csv' INTO TABLE Travel FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;
LOAD DATA LOCAL INFILE 'infotravel.csv' INTO TABLE InfoTravel FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;


update Country set name_en = trim(name_en);
update Country set name_cn = name_en where name_cn is null or name_cn = '';
update City set name_en = trim(name_en);
update City set name_cn = name_en where name_cn is null or name_cn = '';
update Activity set name_en = trim(name_en);
update Activity set name_cn = name_en where name_cn is null or name_cn = '';
update Restaurant set name_en = trim(name_en);
update Restaurant set name_cn = name_en where name_cn is null or name_cn = '';
update Hotel set name_en = trim(name_en);
update Hotel set name_cn = name_en where name_cn is null or name_cn = '';
update Sight set name_en = trim(name_en);
update Sight set name_cn = name_en where name_cn is null or name_cn = '';
update Travel set name_en = trim(name_en);
update Travel set name_cn = name_en where name_cn is null or name_cn = '';

update Country set name_cn = trim(name_cn);
update Country set name_en = name_cn where name_en is null or name_en = '';
update City set name_cn = trim(name_cn);
update City set name_en = name_cn where name_en is null or name_en = '';
update Activity set name_cn = trim(name_cn);
update Activity set name_en = name_cn where name_en is null or name_en = '';
update Restaurant set name_cn = trim(name_cn);
update Restaurant set name_en = name_cn where name_en is null or name_en = '';
update Hotel set name_cn = trim(name_cn);
update Hotel set name_en = name_cn where name_en is null or name_en = '';
update Sight set name_cn = trim(name_cn);
update Sight set name_en = name_cn where name_en is null or name_en = '';
update Travel set name_cn = trim(name_cn);
update Travel set name_en = name_cn where name_en is null or name_en = '';


update Activity set view = (FLOOR( 3000 + RAND( ) * 7000 )) where view = 0;
update Restaurant set view = (FLOOR( 3000 + RAND( ) * 7000 )) where view = 0;
update Hotel set view = (FLOOR( 3000 + RAND( ) * 7000 )) where view = 0;
update Sight set view = (FLOOR( 3000 + RAND( ) * 7000 )) where view = 0;

update Activity set adore = (FLOOR( 50 + RAND( ) * 100 )) where adore = 0;
update Restaurant set adore = (FLOOR( 50 + RAND( ) * 100 )) where adore = 0;
update Hotel set adore = (FLOOR( 50 + RAND( ) * 100 )) where adore = 0;
update Sight set adore = (FLOOR( 50 + RAND( ) * 100 )) where adore = 0;
