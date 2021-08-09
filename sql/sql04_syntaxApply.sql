-- 숫자함수 예제
SELECT ABS(+ 17), ABS(- 17), CEIL(3.28), FLOOR(4.259);

SELECT 학번, SUM(기말성적)/COUNT(*), ROUND(SUM(기말성적)/COUNT(*), 2)
FROM 수강
GROUP BY 학번;

-- 문자함수 예제
SELECT LENGTH(소속학과), RIGHT(학번, 2), REPEAT('*', 나이), CONCAT(소속학과, '학과')
FROM 학생;

SELECT SUBSTRING(주소, 1, 2), REPLACE(SUBSTRING(휴대폰번호, 5, 9), '-', ',')
FROM 학생;

-- 날짜, 시간함수 예제
SELECT 신청날짜, LAST_DAY(신청날짜)
FROM 수강
WHERE YEAR(신청날짜) = '2019';

SELECT SYSDATE(), DATEDIFF(신청날짜, '2019-01-01') -- DATEDIFF() : 두 개의 날짜값 차이를 int로 변환
FROM 수강;

SELECT 신청날짜, DATE_FORMAT(신청날짜, '%b/%d/%y'), DATE_FORMAT(신청날짜, '%Y년%c월%e일')
FROM 수강;

-- 프로시저
-- 예제 7-1 (프로시저 생성)
DELIMITER //
CREATE PROCEDURE InsertOrUpdateCourse (
	IN CourseNo		VARCHAR(4),
    IN CourseName 	VARCHAR(20),
    IN CourseRoom	CHAR(3),
    IN CourseDept	VARCHAR(20),
    IN CourseCredit	INT )
BEGIN
	DECLARE Count INT;
    SELECT COUNT(*) INTO Count FROM 과목 WHERE 과목번호 = CourseNo;
    IF (Count = 0) THEN
		INSERT INTO 과목(과목번호, 이름, 강의실, 개설학과, 시수)
        VALUES(CourseNo, CourseName, CourseRoom, CourseDept, CourseCredit);
	ELSE
		UPDATE 과목
        SET 이름 = CourseName, 강의실 = CourseRoom, 개설학과 = CourseDept, 시수 = CourseCredit
        WHERE 과목번호 = CourseNo;
	END IF;
END; //
DELIMITER ;

-- 예제 7-2 (삽입프로시저 호출)
CALL InsertOrUpdateCourse('c006', '연극학개론', '310', '교양학부', 2);

SELECT * FROM 과목;

-- 예제 7-3 (수정,저장 프로시저 호출)
CALL InsertOrUpdateCourse('c006', '연극학개론', '410', '교양학부', 2);

SELECT * FROM 과목;

-- 7-4 (검색, 저장 프로시저 생성)
DELIMITER //
CREATE PROCEDURE SelectAverageOfBestScore (
	IN  Score INT,
    OUT Count INT)
BEGIN
	DECLARE NoMoreData INT DEFAULT FALSE;
    DECLARE Midterm    INT;
    DECLARE Final	   INT;
    DECLARE Best	   INT;
    DECLARE ScoreListCursor CURSOR FOR
		SELECT 중간성적, 기말성적 FROM 수강;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET NoMoreData = TRUE;
		SET Count = 0;
	OPEN ScoreListCursor;
    REPEAT
		FETCH ScoreListCursor INTO Midterm, Final;
        IF Midterm > Final THEN
			SET Best = Midterm;
		ELSE
			SET BEST = FINAL;
		END IF;
        IF (Best >= Score) THEN
			SET Count = Count + 1;
		END IF;
	UNTIL NoMoreData END REPEAT;
    CLOSE ScoreListCursor;
END; //
DELIMITER ;

-- 7-5 (검색 프로시저 호출)
CALL SelectAverageOfBestScore(95, @Count);

SELECT @Count;

-- 7-6 (저장 프로시저 삭제)
SHOW CREATE PROCEDURE InsertOrUpdateCourse; -- 프로시저의 내용 확인

DROP PROCEDURE InsertOrUpdateCourse;

-- 7-7
-- 예제 테이블 생성
CREATE TABLE 남녀학생총수(
	성별  CHAR(1) NOT NULL DEFAULT 0,
    인원수 INT	 NOT NULL DEFAULT 0,
    PRIMARY KEY (성별));
    
INSERT INTO 남녀학생총수 
SELECT '남', COUNT(*) 
FROM 학생
WHERE 성별 = '남';

INSERT INTO 남녀학생총수 
SELECT '여', COUNT(*) 
FROM 학생
WHERE 성별 = '여';

SELECT * FROM 남녀학생총수;

-- 트리거 생성
DELIMITER //
CREATE TRIGGER AfterInsertStu
AFTER INSERT ON 학생 FOR EACH ROW
BEGIN
	IF(NEW.성별 = '남') THEN
		UPDATE 남녀학생총수 SET 인원수 = 인원수 + 1 WHERE 성별 = '남';
	ELSEIF(NEW.성별 = '여') THEN
		UPDATE 남녀학생총수 SET 인원수 = 인원수 + 1 WHERE 성별 = '여';
	END IF;
END; //
DELIMITER ;

-- INSERT문 UPDATE문으로 변환시 어떻게 변환되는지 확인
UPDATE 남녀학생총수 
SET 인원수 = ( SELECT COUNT(*) FROM 학생 WHERE 성별='남') 
WHERE 성별='남';

-- 트리거 실행
INSERT INTO 학생
VALUES('s008', '최동석', '경기 수원', 2, 26, '남', '010-8888-6666', '컴퓨터');

SELECT * FROM 학생;
SELECT * FROM 남녀학생총수;

-- 예제 7-8 (트리거 삭제)
DROP TRIGGER AfterInsertStu;

SHOW TRIGGERS;

-- 예제 7-9 (사용자 함수 정의)
DELIMITER //
CREATE FUNCTION Fn_Grade( grade CHAR(1) )
RETURNS VARCHAR(10)
BEGIN
	DECLARE ret_grade VARCHAR(10);
    IF ( grade = 'A' ) THEN
		SET ret_grade = '최우수';
	ELSEIF ( grade = 'B' ) THEN
		SET ret_grade = '우수';
	ELSEIF ( grade = 'C' ) THEN
		SET ret_grade = '보통';
	ELSEIF ( grade = 'D' OR grade = 'F' ) THEN
		SET ret_grade = '미흡';
	END IF;
    RETURN ret_grade;
END //
DELIMITER ;


