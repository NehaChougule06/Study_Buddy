-- Active: 1699592676579@@127.0.0.1@3306@study_buddy

CREATE TABLE Login (
  Username VARCHAR(18) PRIMARY KEY,
  Password VARCHAR(255) NOT NULL
);

CREATE TABLE F_faculty (
    F_ID VARCHAR(15) PRIMARY KEY,
    F_time TIME,
    classes_conducted INTEGER,
    F_name VARCHAR(255),
    class_ID INTEGER,
    course_ID VARCHAR(255)
);

CREATE TABLE Subject (
    courseID VARCHAR(255) PRIMARY KEY,
    course_name VARCHAR(15),
    resources TEXT
);

CREATE TABLE Student (
    S_UID INTEGER AUTO_INCREMENT PRIMARY KEY,
    S_SRN VARCHAR(18),
    S_section VARCHAR(15),
    S_name VARCHAR(15),
    S_sem INTEGER
);

CREATE TABLE Class (
    class_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    duration VARCHAR(15),
    class_status ENUM('in progress', 'canceled', 'scheduled'),
    class_date DATE,
    building VARCHAR(255),
    Floor_number INTEGER,
    Room_no VARCHAR(255),
    Class_time TIME,
    class_type ENUM('online', 'offline'),
    class_category ENUM('Faculty','Tutor','Group Study')
);

CREATE TABLE T_tutor (
    T_SRN INT PRIMARY KEY,
    T_section VARCHAR(255),
    T_name VARCHAR(255),
    T_sem INTEGER,
    T_time TIME,
    Class_ID INTEGER,
    Course_ID VARCHAR(15)
);

CREATE TABLE tutor_details (
    T_ID INTEGER AUTO_INCREMENT PRIMARY KEY,
    T_SRN INT,
    T_section VARCHAR(255),
    T_name VARCHAR(255),
    T_sem INTEGER,
    T_time TIME,
    Class_ID INTEGER,
    Course_ID VARCHAR(15)
);

ALTER TABLE f_faculty
MODIFY COLUMN F_time VARCHAR(20);

ALTER TABLE t_tutor
MODIFY COLUMN T_time VARCHAR(20);

ALTER TABLE tutor_details
MODIFY COLUMN T_time VARCHAR(20);

ALTER TABLE class
MODIFY COLUMN duration VARCHAR(20);

ALTER TABLE class
MODIFY COLUMN class_time VARCHAR(20);

ALTER TABLE student ADD FOREIGN KEY (S_SRN) REFERENCES Login(Username);

ALTER TABLE F_Faculty
ADD FOREIGN KEY (class_ID) REFERENCES Class(class_id), ADD FOREIGN KEY (course_ID) REFERENCES Subject(courseID);

ALTER TABLE T_tutor
ADD FOREIGN KEY (Class_ID) REFERENCES Class(class_id), ADD FOREIGN KEY (Course_ID) REFERENCES Subject(courseID);

ALTER TABLE tutor_details
ADD FOREIGN KEY (Class_ID) REFERENCES Class(class_id), ADD FOREIGN KEY (Course_ID) REFERENCES Subject(courseID);

INSERT INTO Subject (courseID, course_name, resources) VALUES
('UE21CS341A', 'SE' ,'Textbook'),
('UE21CS342AA2', 'DA' ,'Notes'),
('UE21CS343AB3', 'GTA' ,'Textbook'),
('UE21CS351A', 'DBMS' ,'Slides'),
('UE21CS352A', 'MI' ,'Notes, Slides');

INSERT INTO Student (S_SRN, S_section, S_name, S_sem) VALUES
('PES1UG21CS121', 'A', 'Kevin', 1),
('PES1UG21CS131', 'B', 'Joe', 2),
('PES1UG21CS141', 'C', 'Dhruv', 3),
('PES1UG21CS181', 'D', 'Albert', 1),
('PES1UG21CS120', 'B', 'Isaac', 2);

INSERT INTO Class (duration, class_status, class_date, building, Floor_number, Room_no, Class_time, class_type, class_category) VALUES
(60, 'in progress', '2023-11-11', 'Building A', 2, 'Room 201', '08:00:00', 'offline', 'Tutor'),
(90, 'scheduled', '2023-11-12', 'Building B', 1, 'Room 101', '10:30:00', 'offline', 'Faculty'),
(120, 'canceled', '2023-11-13', 'Building C', 3, 'Room 301', '13:00:00', 'offline', 'Group Study'),
(30, 'in progress', '2023-11-14', NULL, NULL, NULL, '09:45:00', 'online', 'Faculty'),
(45, 'scheduled', '2023-11-15', NULL, NULL, NULL, NULL, 'online', 'Tutor');

INSERT INTO Login (Username, Password) VALUES
('PES1UG21CS121', 'password1'),
('PES1UG21CS131', 'password2'),
('PES1UG21CS141', 'password3'),
('PES1UG21CS181', 'password4'),
('PES1UG21CS120', 'password5');

INSERT INTO F_faculty (F_ID, F_time, classes_conducted, F_name, class_ID, course_ID) VALUES
('PES3001', '10:00:00', 10, 'David', 1, 'UE21CS341A'),
('PES3002', '11:30:00', 8, 'Faculty 2', 2, 'UE21CS342AA2'),
('PES3003', '14:00:00', 12, 'Faculty 3', 3, 'UE21CS352A'),
('PES3004', '09:15:00', 15, 'Faculty 4', 4, 'UE21CS343AB3'),
('PES3005', '16:45:00', 7, 'Faculty 5', 5, 'UE21CS351A');

INSERT INTO t_tutor (T_SRN, T_section, T_name, T_sem, T_time, Class_ID, Course_ID) VALUES
(4001, 'A', 'Tutor 1', 1, '12:00:00', 1, 'UE21CS341A'),
(4002, 'B', 'Tutor 2', 2, '13:30:00', 2, 'UE21CS342AA2'),
(4003, 'C', 'Tutor 3', 3, '16:00:00', 3, 'UE21CS352A'),
(4004, 'A', 'Tutor 4', 1, '11:15:00', 4, 'UE21CS343AB3'),
(4005, 'B', 'Tutor 5', 2, '18:45:00', 5, 'UE21CS351A');

INSERT INTO tutor_details (T_SRN, T_section, T_name, T_sem, T_time, Class_ID, Course_ID) VALUES
(4001, 'A', 'Tutor 1', 1, '12:00:00', 1, 'UE21CS341A'),
(4002, 'B', 'Tutor 2', 2, '13:30:00', 2, 'UE21CS342AA2'),
(4003, 'C', 'Tutor 3', 3, '16:00:00', 3, 'UE21CS352A'),
(4004, 'A', 'Tutor 4', 1, '11:15:00', 4, 'UE21CS343AB3'),
(4005, 'B', 'Tutor 5', 2, '18:45:00', 5, 'UE21CS351A');

INSERT INTO tutor_details (T_SRN, T_section, T_name, T_sem, T_time, Class_ID, Course_ID) VALUES
(4001, 'A', 'Tutor 1', 1, '12:00:00', 2, NULL),
(4001, 'B', 'Tutor 1', 1, '12:00:00', 4, NULL),
(4001, 'D', 'Tutor 1', 1, '12:00:00', 3, NULL),
(4001, 'E', 'Tutor 1', 1, '12:00:00', 5, NULL);



-- Triggers
DELIMITER //
CREATE TRIGGER update_class_status
BEFORE INSERT ON Class
FOR EACH ROW
BEGIN
    IF NEW.class_date < CURDATE() THEN
        SET NEW.class_status = 'canceled';
    END IF;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER set_building_for_online_classes
BEFORE INSERT ON Class
FOR EACH ROW
BEGIN
    IF NEW.class_type = 'online' THEN
        SET NEW.building = 'Online';
    END IF;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER prevent_tutor_overlap
BEFORE INSERT ON T_tutor
FOR EACH ROW
BEGIN
    DECLARE overlap_count INT;
    SELECT COUNT(*)
    INTO overlap_count
    FROM T_tutor
    WHERE T_SRN = NEW.T_SRN
    AND ((NEW.Class_ID IS NOT NULL AND Class_ID = NEW.Class_ID)
         OR (NEW.Course_ID IS NOT NULL AND Course_ID = NEW.Course_ID));

    IF overlap_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Tutor already assigned to the selected class or course.';
    END IF;
END;
//
DELIMITER ;

-- Stored Procedures    
DELIMITER //
CREATE PROCEDURE GetStudentClassSchedule(IN studentSRN VARCHAR(18))
BEGIN
    SELECT Class.*
    FROM Class
    JOIN Student ON Class.class_id = Student.S_UID
    WHERE Student.S_SRN = studentSRN;
END;
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE EnrollStudent(IN studentSRN VARCHAR(18), IN classID INT)
BEGIN
    INSERT INTO Student (S_SRN, S_UID)
    VALUES (studentSRN, classID);
END;
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetFacultyClasses(IN facultyID VARCHAR(15))
BEGIN
    SELECT *
    FROM F_faculty
    WHERE F_ID = facultyID;
END;
//
DELIMITER ;

--Functions

DELIMITER //
CREATE FUNCTION GetFacultyClassCount(facultyID VARCHAR(15)) RETURNS INT DETERMINISTIC
BEGIN
    DECLARE classCount INT;
    SELECT COUNT(*)
    INTO classCount
    FROM F_faculty
    WHERE F_ID = facultyID;
    RETURN classCount;
END;
//
DELIMITER ;

DELIMITER //
CREATE FUNCTION IsStudentEnrolled(studentSRN VARCHAR(18), classID INT) RETURNS BOOLEAN READS SQL DATA
BEGIN
    DECLARE isEnrolled BOOLEAN;
    SELECT COUNT(*)
    INTO isEnrolled
    FROM Student
    WHERE S_SRN = studentSRN AND S_UID = classID;
    RETURN isEnrolled;
END;
//
DELIMITER ;


DELIMITER //
CREATE FUNCTION CalculateAverageClasses() RETURNS DECIMAL(5, 2) READS SQL DATA
BEGIN
    DECLARE totalClasses INT;
    DECLARE facultyCount INT;
    SELECT SUM(classes_conducted), COUNT(*)
    INTO totalClasses, facultyCount
    FROM F_faculty;
    
    IF facultyCount > 0 THEN
        RETURN totalClasses / facultyCount;
    ELSE
        RETURN 0;
    END IF;
END;
//
DELIMITER ;

DROP Procedure IF EXISTS AssignTutorToClass;

DELIMITER //
CREATE PROCEDURE AssignTutorToClass(
    IN p_T_SRN INT,
    IN p_T_section VARCHAR(255),
    IN p_T_name VARCHAR(255),
    IN p_T_sem INTEGER,
    IN p_T_time TIME,
    IN p_Class_ID INTEGER,
    IN p_Course_ID VARCHAR(15)
)
BEGIN
    INSERT INTO tutor_details(T_SRN, T_section, T_name, T_sem, T_time, Class_ID, Course_ID)
    VALUES (p_T_SRN, p_T_section, p_T_name, p_T_sem, p_T_time, p_Class_ID, p_Course_ID);
END
DELIMITER ;

SELECT building, SUM(duration) AS total_duration
    FROM Class
    WHERE class_type = 'offline' AND building IS NOT NULL
    GROUP BY building;

SELECT T_SRN, COUNT(*) AS ClassesConducted
FROM tutor_details
GROUP BY T_SRN
HAVING COUNT(*) > 5;
