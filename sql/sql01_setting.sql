/*
-- 0805
- 버전 체크
SELECT version(); -- MsSQL 버전 확인
SELECT current_date(), current_time(), now();
*/
/*
-- 계정 생성
CREATE USER 'manager'@'%' IDENTIFIED BY '123'; -- % : 모든 컴퓨터에서 접근 가능
GRANT ALL ON *.* TO 'manager'@'%' WITH GRANT OPTION; -- ALL : 모든 권한
*/
/*
-- User 및 데이터베이스 확인
SELECT USER();
SHOW DATABASE();
*/
