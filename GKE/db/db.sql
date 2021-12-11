CREATE DATABASE dbapp;

\c dbapp;

CREATE TABLE profile (
    boleta      VARCHAR(10) NOT NULL PRIMARY KEY,
    lastname    VARCHAR(50),
    firstname   VARCHAR(50)
);

INSERT INTO profile
VALUES ('2019630529', 'Cruz', 'Paul');

SELECT * FROM profile;