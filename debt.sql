DROP DATABASE debtDB;

CREATE DATABASE IF NOT EXISTS debtDB;
GRANT ALL PRIVILEGES ON debtDB.* to 'debt'@'localhost' 
identified by 'password';
USE debtDB;

CREATE TABLE user_list (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,/*Auto increment here? also primary key?*/
  username VARCHAR(50),
  password VARCHAR(20),
  total_debt INT(100)
);

CREATE TABLE friend_debt (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, /*primary key*/  
  transaction VARCHAR(50),
  debt_amount INT(100),
  description VARCHAR(100)
);

CREATE TABLE friend_info (
  user_id INT NOT NULL, 
  CONSTRAINT user_list_user_id_fk
  FOREIGN KEY (user_id)
  REFERENCES user_list (id),
  debt_id INT NOT NULL,
  CONSTRAINT friend_debt_debt_id_fk
  FOREIGN KEY (debt_id)
  REFERENCES friend_debt (id)
);


/*CREATE TABLE user_debt (
  user_id INT NOT NULL,
  CONSTRAINT friend_list_user_id_fk
  FOREIGN KEY (user_id)
  REFERENCES friend_list (user_id)
  transaction VARCHAR(50),
  debt_amount INT(100),
  description VARCHAR(100)
);*/
 

INSERT INTO user_list VALUES (id,'Brennan Miller','peanut', 10);
INSERT INTO user_list VALUES ( id,'Austin Bouchard','12345', 30);
INSERT INTO user_list VALUES (id,'Riley Starrs','Riotpls01', 50);

/*INSERT INTO friend_debt VALUES('Zacharski', 55, 'stole my girlfriend');
INSERT INTO friend_debt VALUES('Benshoff', 10, 'Back massage');
INSERT INTO friend_debt VALUES('Patrick', -10, 'let me eat girlscout cookies');
INSERT INTO user_debt VALUES ('Raz', 1, 'Bummed a smoke');*/