DROP DATABASE debtDB;

CREATE DATABASE IF NOT EXISTS debtDB;
GRANT ALL PRIVILEGES ON debtDB.* to 'debt'@'localhost'
identified by 'password';
USE debtDB;

CREATE TABLE main_list (
  id INT NOT NULL AUTO_INCREMENT,
  firstname VARCHAR(25),
  lastname VARCHAR(25),
  total_debt INT(100),
  PRIMARY KEY(id)
);

CREATE TABLE friend_debt (
  friend_lastname VARCHAR(50),
  debt_amount INT(100),
  description VARCHAR(100)
);

CREATE TABLE user_debt (
  user_id VARCHAR(50),
  debt_amount INT(100),
  description VARCHAR(100)
);
 

INSERT INTO main_list (id, firstname, lastname, total_debt) VALUES (NULL,'Brennan','Miller', 0);
INSERT INTO main_list (id, firstname, lastname, total_debt) VALUES (NULL,'Austin','Bouchard', -1);
INSERT INTO main_list (id, firstname, lastname, total_debt) VALUES (NULL,'Riley','Starrs', 0);
INSERT INTO main_list (id, firstname, lastname, total_debt) VALUES (NULL,'Patrick','Stalcup', 59);

INSERT INTO friend_debt VALUES('Zacharski', 55, 'stole my girlfriend');
INSERT INTO friend_debt VALUES('Benshoff', 10, 'Back massage');
INSERT INTO friend_debt VALUES('Patrick', -10, 'let me eat girlscout cookies');
INSERT INTO user_debt VALUES ('Raz', 1, 'Bummed a smoke');