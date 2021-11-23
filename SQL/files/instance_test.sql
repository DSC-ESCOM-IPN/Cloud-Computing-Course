CREATE DATABASE test;

USE test;

CREATE TABLE profile (
    LastName varchar(255),
    FirstName varchar(255)
);

INSERT INTO profile
VALUES ('Cruz', 'Paul');

SELECT * FROM profile;