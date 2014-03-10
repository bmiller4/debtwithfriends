DROP DATABASE debtDB;

CREATE DATABASE IF NOT EXISTS debtDB;
GRANT ALL PRIVILEGES ON debtDB.* to 'debt'@'localhost'
identified by 'password';
USE debtDB;

CREATE TABLE main_list (
  firstname VARCHAR(25),
  lastname VARCHAR(25),
  total_debt INT(100)
);

CREATE TABLE friend_debt (
  transaction VARCHAR(50),
  debt_amount INT(100),
  description VARCHAR(100)
);

CREATE TABLE user_debt (
  transaction VARCHAR(50),
  debt_amount INT(100),
  description VARCHAR(100)
);
 

INSERT INTO main_list VALUES ('Brennan','Miller', 10);
INSERT INTO main_list VALUES ('Austin','Bouchard', 30);
INSERT INTO main_list VALUES ('Riley','Starrs', 50);
INSERT INTO main_list VALUES ('Patrick','Stalcup', -59);