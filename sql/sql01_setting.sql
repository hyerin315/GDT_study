/*
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
/*
-- 데이터 베이스 삭제 및 생성, 기본 데이터베이스 사용 설정
DROP DATABASE IF EXISTS univDB;
CREATE DATABASE IF NOT EXISTS univDB;
USE univDB;
*/
/*
-- 과목테이블 생성
CREATE TABLE 과목(과목번호 	CHAR(4)		 NOT NULL 	PRIMARY KEY, -- 방법 1
				 이름 	VARCHAR(20)	 NOT NULL,
                 강의실  	CHAR(3)		 NOT NULL,
                 개설학과  VARCHAR(20) NOT NULL,
				 시수	 INT NOT NULL );
                 
-- 과목테이블 입력
INSERT INTO 과목
VALUES ('c001', '데이터베이스', 126, '컴퓨터', 3);
INSERT INTO 과목
VALUES ('c002', '정보보호', 137, '정보통신', 3);
INSERT INTO 과목
VALUES ('c003', '모바일웹', 128, '컴퓨터', 3);
INSERT INTO 과목
VALUES ('c004', '철학개론', 117, '철학', 2);
INSERT INTO 과목
VALUES ('c005', '전공글쓰기', 120, '교양학부', 1);
*/
/*
-- 데이터베이스 테이블 생성
CREATE TABLE 학생(학번 	 CHAR(4) 		NOT NULL,
				 이름 	 VARCHAR(20)	NOT NULL,
                 주소 	 VARCHAR(50)	NULL DEFAULT '미정',
                 학년 	 INT 			NOT NULL,
                 나이 	 INT			NULL, 
                 성별 	 CHAR(1)		NOT NULL,
                 휴대폰번호 CHAR(14)		NULL,
                 소속학과   VARCHAR(20)	NULL,
                 PRIMARY KEY (학번));
*/
/*
-- 학생 테이블 입력
INSERT INTO 학생
VALUES ('s001', '김연아', '서울 서초', 4, 23, '여', '010-1111-2222', '컴퓨터');
INSERT INTO 학생
VALUES ('s002', '홍길동', DEFAULT, 1, 26, '남', NULL, '통계');
INSERT INTO 학생
VALUES ('s003', '이승엽', NULL, 3, 30, '남', NULL, '정보통신');
INSERT INTO 학생
VALUES ('s004', '이영애', '경기 분당', 2, NULL, '여', '010-4444-5555', '정보통신');
INSERT INTO 학생
VALUES ('s005', '송윤아', '경기 분당', 4, 23, '여', '010-6666-7777', '컴퓨터');
INSERT INTO 학생
VALUES ('s006', '홍길동', '서울 종로', 2, 26, '남', '010-8888-9999', '컴퓨터');
INSERT INTO 학생
VALUES ('s007', '이은진', '경기 과천', 1, 23, '여', '010-2222-3333', '경영');
*/
/*
-- 수강테이블 생성
CREATE TABLE 수강(학번 	 CHAR(6)	NOT NULL,
				 과목번호  CHAR(4)	NOT NULL,
                 신청날짜  DATE		NOT NULL,
                 중간성적  INT 		NULL	   DEFAULT 0,
				 기말성적	 INT		NULL	   DEFAULT 0,
                 평가학점  CHAR(1)    NULL,
                 PRIMARY KEY(학번, 과목번호)); -- 방법 2
            
-- 수강테이블 입력
INSERT INTO 수강
VALUES ('s001', 'c002', '2019-09-03', 93, 98, 'A');
INSERT INTO 수강
VALUES ('s004', 'c005', '2019-03-03', 72, 78, 'C');
INSERT INTO 수강
VALUES ('s003', 'c002', '2017-09-06', 85, 82, 'B');
INSERT INTO 수강
VALUES ('s002', 'c001', '2018-03-10', 31, 50, 'F');
INSERT INTO 수강
VALUES ('s001', 'c004', '2019-03-05', 82, 89, 'B');
INSERT INTO 수강
VALUES ('s004', 'c003', '2020-09-03', 91, 94, 'A');
INSERT INTO 수강
VALUES ('s001', 'c005', '2020-09-03', 74, 79, 'C');
INSERT INTO 수강
VALUES ('s003', 'c001', '2019-03-03', 81, 82, 'B');
INSERT INTO 수강
VALUES ('s004', 'c002', '2018-03-05', 92, 95, 'A');
*/
/*
-- 데이터베이스 및 테이블 확인
SELECT database(); -- 현재 사용 데이터베이스 확인
SHOW TABLES; -- univDB 안의 생성 테이블 목록 확인

DESC 과목;
DESC 학생;
DESC 수강;

SELECT * FROM 과목;
SELECT * FROM 학생;
SELECT * FROM 수강;

-- DB 실행시 데이터베이스 가져오기
USE univDB; -- univDB 다시 가져오기
*/

-- 예제 5-1
SELECT 이름, 주소 
FROM 학생;

-- 예제 5-2
SELECT 학번, 이름, 주소, 학년, 나이, 성별, 휴대폰번호, 소속학과
FROM 학생;

SELECT * FROM 학생;

-- 예제 5-3
SELECT DISTINCT 소속학과 
FROM 학생;

SELECT 소속학과
FROM 학생;

SELECT ALL 소속학과
FROM 학생;

-- 예제 5-4
SELECT 이름, 학년, 소속학과, 휴대폰번호
FROM 학생
WHERE 학년 >= 2 AND 소속학과 = '컴퓨터';

-- 예제 5-5
SELECT 이름, 학년, 소속학과, 휴대폰번호
FROM 학생
WHERE (학년 >= 1 AND 학년 <= 3) OR NOT (소속학과 = '컴퓨터');

SELECT 이름, 학년, 소속학과, 휴대폰번호
FROM 학생
WHERE (학년 BETWEEN 1 AND 3) OR NOT (소속학과 = '컴퓨터');

-- 예제 5-6
SELECT 이름, 학년, 소속학과
FROM 학생
WHERE 소속학과 = '컴퓨터' OR 소속학과 = '정보통신'
ORDER BY 학년 ASC; 

-- 예제 5-7
SELECT *
FROM 학생
ORDER BY 학년 ASC, 이름 DESC;

-- 예제 5-8
SELECT COUNT(*)
FROM 학생;

SELECT COUNT(학번)
FROM 학생;

SELECT COUNT(*) AS 학생수1, COUNT(주소) AS 학생수2, COUNT(DISTINCT 주소) AS 학생수3
FROM 학생; 

-- 예제 5-9
SELECT AVG(나이) '여학생 평균나이' -- AS : 별칭, 생략가능
FROM 학생
WHERE 성별 = '여';

-- 예제 5-10
SELECT 성별, MAX(나이) AS '최고나이', MIN(나이) AS '최저나이'
FROM 학생
GROUP BY 성별;

-- 예제 5-11
SELECT 나이, COUNT(*) AS '나이별 학생수'
FROM 학생
WHERE 나이 >= 20 AND 나이 <= 30
GROUP BY 나이;

-- 예제 5-12
SELECT 학년, COUNT(*) AS '학년별 학생수'
FROM 학생
GROUP BY 학년
HAVING COUNT(*) >= 2;
