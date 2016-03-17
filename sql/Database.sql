
CREATE TABLE `TestInfo` (
  `ImageCount` VARCHAR(45) NOT NULL,
  `ImageCountGroup` VARCHAR(45) NOT NULL,
  `QuestionCount` VARCHAR(45) NOT NULL,
  `SevenPointQuestion` VARCHAR(45) NOT NULL,
  `ImageURL` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ImageCount`, `ImageCountGroup`, `QuestionCount`));

CREATE TABLE `Admin` (
  `AdminName` VARCHAR(45) NOT NULL,
  `AdminPassword` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`AdminName`));

CREATE TABLE `User` (
  `Student_ID` VARCHAR(45) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Student_ID`));

CREATE TABLE `Image` (
  `Image_ID` VARCHAR(45) NOT NULL,
  `Question_count` INT NOT NULL,
  PRIMARY KEY (`Image_ID`));

CREATE TABLE `Question` (
  `Image_ID` VARCHAR(45) NOT NULL,
  `Q_ID` VARCHAR(45) NOT NULL,
  `Question` VARCHAR(100) NOT NULL,
  `SelectA` VARCHAR(45) NOT NULL,
  `SelectB` VARCHAR(45) NOT NULL,
  `SelectC` VARCHAR(45) NOT NULL,
  `SelectD` VARCHAR(45) NOT NULL,
  `CorrectAnswer` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Q_ID`, `Image_ID`));

CREATE TABLE `ParticipateAnswer` (
  `Student_ID` VARCHAR(45) NOT NULL,
  `Image_ID` VARCHAR(45) NOT NULL,
  `Q_ID` VARCHAR(45) NOT NULL,
  `Answer` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Student_ID`, `Image_ID`, `Q_ID`));

CREATE TABLE `ImageGrade` (
  `Image_ID` VARCHAR(45) NOT NULL,
  `Student_ID` VARCHAR(45) NOT NULL,
  `Grade` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Image_ID`, `Student_ID`));

CREATE TABLE `UseTime` (
  `Student_ID` VARCHAR(45) NOT NULL,
  `Image_ID` VARCHAR(45) NOT NULL,
  `UseTime` BIGINT NOT NULL,
  PRIMARY KEY (`Student_ID`, `Image_ID`));

