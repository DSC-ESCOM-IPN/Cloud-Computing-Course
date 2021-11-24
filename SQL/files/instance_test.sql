CREATE DATABASE test;

USE test;

CREATE TABLE profile (
    boleta      VARCHAR(10) NOT NULL PRIMARY KEY,
    LastName    VARCHAR(50),
    FirstName   VARCHAR(50)
);

INSERT INTO profile
VALUES ('2019630529', 'Cruz', 'Paul');

SELECT * FROM profile;