-- 0809

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

-- create 예제
CREATE USER 'user1'@'127.1.1.1' IDENTIFIED BY '1111'; -- 계정 생성
CREATE USER 'user2'@'localhost' IDENTIFIED BY '2222';
CREATE USER 'user3'@'192.182.10.2' IDENTIFIED BY '3333';
CREATE USER 'user4'@'%' IDENTIFIED BY '4444';

SELECT host, user FROM mysql.user; -- 계정정보 확인

-- grant 예제
GRANT INSERT, UPDATE, DELETE ON univDB.* TO 'user1'@'127.1.1.1';
GRANT ALL ON *.* TO 'user4'@'%' WITH GRANT OPTION;
GRANT SELECT ON univDB.학생 TO 'user2'@'localhost';

-- 계정 권한 확인
SHOW GRANTS FOR 'user1'@'127.1.1.1';
SHOW GRANTS;

-- revoke 예제
REVOKE DELETE ON univDB.* FROM 'user1'@'127.1.1.1';

-- drop 예제
DROP USER 'user1'@'127.1.1.1';

SHOW PROCESSLIST; -- 접속중인 사용자 계정 확

-- 예제 6-7
CREATE VIEW V1_고학년학생(학생이름, 나이, 성, 학년)
AS SELECT 이름, 나이, 성별, 학년
   FROM 학생
   WHERE 학년 >= 3 AND 학년 <= 4;

-- 뷰 데이터 확인
SELECT *
FROM V1_고학년학생;

-- 뷰의 존재 확인
SHOW TABLES;

-- 뷰의 구조 확인
DESC V1_고학년학생;

-- 예제 6-8
CREATE VIEW V2_과목수강현황(과목번호, 강의실, 수강인원수)
AS SELECT 과목.과목번호, 강의실, COUNT(과목.과목번호)
   FROM 과목 JOIN 수강 ON 과목.과목번호 = 수강.과목번호
   GROUP BY 과목.과목번호;
   
SELECT * FROM V2_과목수강현황;

-- 예제 6-9
CREATE VIEW V3_고학년여학생
AS SELECT *
   FROM V1_고학년학생
   WHERE 성 = '여';
   
SELECT * FROM V3_고학년여학생;

-- 예제 6-10
SELECT *
FROM V1_고학년학생
WHERE 성 = '여';

SELECT * 
FROM V3_고학년여학생;

-- 예제 6-11
SELECT *
FROM V2_과목수강현황
WHERE 수강인원수 = (SELECT MAX(수강인원수) FROM V2_과목수강현황) OR
	  수강인원수 = (SELECT MIN(수강인원수) FROM V2_과목수강현황);
      
-- 예제 6-12
DROP VIEW V1_고학년학생;

SHOW TABLES;

-- 예제 6-13
CREATE INDEX idx_수강
ON 수강(학번, 과목번호);

SHOW INDEX FROM 수강; -- 인덱스 확인

-- 예제 6-14
CREATE UNIQUE INDEX idx_과목
ON 과목(이름 ASC);

SHOW INDEX FROM 과목;

-- 예제 6-15
DROP INDEX idx_수강 ON 수강; -- 방법 1
ALTER TABLE 과목 DROP INDEX idx_과목;

SHOW INDEX FROM 과목;
SHOW INDEX FROM 수강;