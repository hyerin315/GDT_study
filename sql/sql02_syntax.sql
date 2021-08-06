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

/*
-- 0806
USE univDB;
*/

-- 예제 5-13
SELECT 학번, 이름
FROM 학생
WHERE 이름 LIKE '이__';

-- 예제 5-14
SELECT 이름, 주소, 학년
FROM 학생
WHERE 주소 LIKE '%서울%'
ORDER BY 학년 DESC;

-- 예제 5-15
SELECT 이름, 휴대폰번호
FROM 학생
WHERE 휴대폰번호 IS NULL;

-- 예제 5-16
SELECT 학번	FROM 학생  WHERE 성별 = '여'
UNION
SELECT 학번	FROM 수강  WHERE 평가학점='A';

-- 예제 5-17a
SELECT 이름
FROM 학생
WHERE 학번 IN ('s001', 's003', 's004');

-- 예제 5-17b
SELECT 이름
FROM 학생
WHERE 학번 IN (SELECT 학번
			  FROM 수강
              WHERE 과목번호 = 'c002');

-- 예제 5-17c
SELECT 이름
FROM 학생
WHERE 학번 IN (SELECT 학번
			  FROM 수강
			  WHERE 과목번호 = (SELECT 과목번호
							  FROM 과목
                              WHERE 이름 = '정보보호'));

-- 예제 5-17d
SELECT 이름
FROM 학생
WHERE EXISTS (SELECT *
			  FROM 수강
              WHERE 수강.학번 = 학생.학번 AND 과목번호 = 'c002');
              
-- 예제 Cross join
SELECT *
FROM 학생, 수강;

SELECT *
FROM 학생 CROSS JOIN 수강;

-- 예제 5-18
SELECT *
FROM 학생, 수강
WHERE 학생.학번 = 수강.학번;

SELECT *
FROM 학생 JOIN 수강 ON 학생.학번 = 수강.학번;

-- 예제 5-19
SELECT 학생.학번, 이름, 과목번호, 중간성적+(중간성적*0.1) AS 변환중간성적
FROM 학생, 수강
WHERE 학생.학번 = 수강.학번 AND 과목번호 = 'c002';

-- 예제 5-20
SELECT 학생.학번, 학생.이름, 수강.과목번호
FROM 학생, 수강, 과목
WHERE 학생.학번 = 수강.학번 AND 수강.과목번호 = 과목.과목번호 AND 과목.이름 = '정보보호';

SELECT 학생.학번, 학생.이름, 수강.과목번호
FROM (학생 JOIN 수강 ON 학생.학번 = 수강.학번) JOIN 과목 ON 수강.과목번호 = 과목.과목번호
WHERE 과목.이름 = '정보보호';

-- 예제 5-21
SELECT 이름, 과목번호
FROM 학생 AS S, 수강 AS E
WHERE S.학번 = E.학번 AND 과목번호 = 'c002';

SELECT 이름, 과목번호
FROM (학생 AS S) JOIN (수강 AS E) ON S.학번 = E.학번 AND 과목번호 = 'c002';

-- 예제 5-22
SELECT S1.이름, S2.이름
FROM 학생 S1 JOIN 학생 S2 ON S1.주소 = S2.주소
WHERE S1.학년 > S2.학년;

-- 예제 5-23
SELECT 학생.학번, 이름, 평가학점
FROM 학생 LEFT OUTER JOIN 수강 ON 학생.학번 = 수강.학번;

-- 새 테이블 생성 전 테이블 확인
SHOW TABLES;

-- 테이블 복제 (복제시, 데이터는 복제되나 키나 제약조건은 복제되지 않음)
CREATE TABLE 학생1 AS (SELECT * FROM 학생);
CREATE TABLE 과목1 AS (SELECT * FROM 과목);
CREATE TABLE 수강1 AS (SELECT * FROM 수강);

-- 테이블 확인
SELECT * FROM 학생1;

-- 예제 5-24
INSERT INTO 학생1
VALUES ('g001', '김연아2', '서울 서초', 4, 23, '여', '010-1111-2222', '컴퓨터');

-- 예제 5-25
INSERT INTO 학생1 (이름, 주소, 학년, 나이, 성별, 휴대폰번호, 소속학과, 학번)
VALUES ('홍길동2', DEFAULT, 1, 26, '남', NULL, '통계', 'g002');

INSERT INTO 학생1 (이름, 학년, 나이, 성별, 소속학과, 학번)
VALUES ('홍길동2', 1, 26, '남', '통계', 'g002');

-- 예제 5-26
INSERT INTO 학생1 (학번, 이름, 학년, 나이, 성별, 소속학과)
VALUES ('g003', '이승엽2', 3, 30, '남', '정보통신');

-- 예제 5-27
SET SQL_SAFE_UPDATES = 0; -- 안전모드 변경 (기본으로 safe_update 설정되어있음)

UPDATE 학생1
SET 학년 = 3
WHERE 이름 = '이은진';

SELECT * FROM 학생1 WHERE 이름 = '이은진';

-- 예제 5-28
UPDATE 학생1
SET 학년=학년+1, 소속학과 = '자유전공학부'
WHERE 학년 = 4;

SELECT * FROM 학생1;

-- 예제 5-29
UPDATE 학생1
SET 소속학과 = NULL
WHERE 학번 NOT IN (SELECT 학번
				  FROM 수강1);

-- 예제 5-30
UPDATE 수강1
SET 학번 = (SELECT 학번
		   FROM 학생1
           WHERE 이름 = '이은진')
WHERE 학번 = 's003';

SELECT * FROM 수강1 WHERE 학번 = 's003' OR 학번 = 's007';

-- 예제 5-31
DELETE FROM 학생1
WHERE 이름 = '송윤아학생1수강1';

SELECT * FROM 학생1;

-- 예제 5-32
DELETE FROM 학생1
WHERE 학년 = 3;

SELECT * FROM 학생1;

-- 예제 5-33
DELETE FROM 과목1
WHERE 과목번호 IN (SELECT 과목번호
				 FROM 수강1
                 GROUP BY 과목번호
                 HAVING COUNT(*) < 2);

SELECT * FROM 과목1;

-- 예제 5-34
DELETE FROM 학생1;

SELECT * FROM 학생1;

-- 예제 6-1
CREATE TABLE IF NOT EXISTS 과목2(과목번호 	CHAR(4)		 	 NOT NULL 	PRIMARY KEY,
								이름 	VARCHAR(20)	 	 NOT NULL,
								강의실  	CHAR(5)			 NOT NULL,
								개설학과  VARCHAR(20) 	 NOT NULL,
								시수	 	INT NOT NULL);
                  
DESC 과목2;

-- 예제 6-2
CREATE TABLE IF NOT EXISTS 학생2(학번 	  CHAR(4) 		NOT NULL,
								이름 	  VARCHAR(20)	NOT NULL,
								주소 	  VARCHAR(50)	NULL DEFAULT '미정',
								학년 	  INT 			NOT NULL,
								나이 	  INT			NULL, 
								성별 	  CHAR(1)		NOT NULL,
								휴대폰번호 CHAR(13)		NULL,
								소속학과   VARCHAR(20)	NULL,
								PRIMARY KEY (학번),
								UNIQUE (휴대폰번호));
 
 DESC 학생2;
 
 SHOW CREATE TABLE 학생2; -- 테이블 생성 SQL문 확인
 
 -- 예제 6-3
 CREATE TABLE IF NOT EXISTS 수강2(학번 	 CHAR(6)	NOT NULL,
								 과목번호  CHAR(4)	NOT NULL,
								 신청날짜  DATE		NOT NULL,
								 중간성적  INT 		NULL	   DEFAULT 0,
								 기말성적	 INT		NULL	   DEFAULT 0,
								 평가학점  CHAR(1)    NULL,
								 PRIMARY KEY(학번, 과목번호),
                                 FOREIGN KEY(학번) REFERENCES 학생2(학번),
                                 FOREIGN KEY(과목번호) REFERENCES 과목2(과목번호)); 
 
DESC 수강2;
 
-- error 확인
INSERT INTO 과목2(과목번호, 이름, 강의실, 개설학과)
VALUES ('c111', 'database', A-123, '산업공학'); -- 1054
 
INSERT INTO 과목2(과목번호, 이름, 강의실, 개설학과, 시수)
VALUES ('c111', 'database', 'A-123', '산업공학'); -- 1136

INSERT INTO 과목2(과목번호, 이름, 강의실, 개설학과, 시수)
VALUES ('c111', 'database', 'A-123', '산업공학', '3'); -- 정상수행

SELECT * FROM 과목2;
 
-- error 확인2
INSERT INTO 학생2(학번, 이름, 학년, 나이, 성별, 휴대폰번호, 소속학과)
VALUES ('s111', '박태환', 4, NULL, '남', '010-1111-1111', '산업공학'); -- 정상수행
 
INSERT INTO 학생2(학번, 이름, 학년, 나이, 성별, 휴대폰번호, 소속학과)
VALUES ('s222', '박태환', 2, NULL, '남', '010-111-1111', '산업공학'); -- 1062

INSERT INTO 학생2(학번, 이름, 학년, 나이, 성별, 휴대폰번호, 소속학과)
VALUES ('s222', '박태환', 2, NULL, '남', '010-2222-2222', '산업공학'); -- 정상수행

SELECT * FROM 학생2;

-- error 확인3
INSERT INTO 수강2(학번, 과목번호, 신청날짜)
VALUES ('s111', 'c111', '2019-12-31'); -- 정상수행

INSERT INTO 수강2(학번, 과목번호, 신청날짜, 중간성적, 기말성적, 평가학점)
VALUES ('s111', 'c222', '2019-12-31', 93, 98, 'A'); -- 1452

INSERT INTO 수강2(학번, 과목번호, 신청날짜, 중간성적, 기말성적, 평가학점)
VALUES ('s111', 'c111', '2019-12-31', 93, 98, 'A'); -- 1062
 
INSERT INTO 수강2(학번, 과목번호, 신청날짜, 중간성적, 기말성적, 평가학점)
VALUES ('s222', 'c111', '2019-12-31', 93, 98, 'A'); -- 정상수행

-- 테이블 복사
INSERT INTO 과목2 SELECT * FROM 과목;
INSERT INTO 학생2 SELECT * FROM 학생;
INSERT INTO 수강2 SELECT * FROM 수강;

-- 예제 6-4
ALTER TABLE 학생2
	ADD 등록날짜 DATETIME NOT NULL DEFAULT '2019-12-30';

SELECT * FROM 학생2;

-- 예제 6-5
ALTER TABLE 학생2
	DROP COLUMN 등록날짜;
    
SELECT * FROM 학생2;
/*
-- Drop 예제
DROP TABLE 수강2;
DROP TABLE 과목2;
DROP TABLE 학생2;
*/