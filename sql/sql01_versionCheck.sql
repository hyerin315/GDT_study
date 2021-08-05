/*
SELECT version(); -- MsSQL 버전 확인
SELECT current_date(), current_time(), now();
*/
/*
CREATE USER 'manager'@'%' IDENTIFIED BY '123'; -- % : 모든 컴퓨터에서 접근 가능
GRANT ALL ON *.* TO 'manager'@'%' WITH GRANT OPTION; -- ALL : 모든 권한
*/
/*
SELECT USER();
SHOW DATABASE();
*/
DROP DATABASE IF EXISTS univDB;
CREATE DATABASE IF NOT EXISTS univDB;
USE univDB

