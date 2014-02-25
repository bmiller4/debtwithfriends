DROP DATABASE debtDB;

CREATE DATABASE IF NOT EXISTS debtDB;
GRANT ALL PRIVILEGES ON debtDB.* to 'debt'@'localhost' 
identified by 'password';
USE debtDB;

CREATE TABLE friend_list (
  id /*Auto increment here? also primary key?*/
  firstname VARCHAR(25),
  lastname VARCHAR(25),
  total_debt INT(1000),
);

CREATE TABLE friend_debt (
  id /*primary key*/  
  transaction VARCHAR(50),
  debt_amount INT(100),
  description VARCHAR(100)
);

CREATE TABLE user_debt (
  id /*primary key*/
  transaction VARCHAR(50),
  debt_amount INT(100),
  description VARCHAR(100)
);
 

INSERT INTO friend_list VALUES ( /*id*/, 'Brennan','Miller', 10);
INSERT INTO friend_list VALUES ( /*id*/, 'Austin','Bouchard', 30);
INSERT INTO friend_list VALUES ( /*id*/, 'Riley','Starrs', 50);
INSERT INTO friend_list VALUES ( /*id*/, 'Patrick','Stalcup', -59);