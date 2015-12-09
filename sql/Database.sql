DROP DATABASE IF EXISTS `Experiment`;

CREATE DATABASE `Experiment` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE Experiment;

CREATE TABLE `Experiment`.`User` (
  `Student_ID` VARCHAR(45) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Student_ID`));

CREATE TABLE `Experiment`.`Image` (
  `Image_ID` VARCHAR(45) NOT NULL,
  `Question_count` INT NOT NULL,
  PRIMARY KEY (`Image_ID`));

CREATE TABLE `Experiment`.`Question` (
  `Image_ID` VARCHAR(45) NOT NULL,
  `Q_ID` VARCHAR(45) NOT NULL,
  `Question` VARCHAR(100) NOT NULL,
  `SelectA` VARCHAR(45) NOT NULL,
  `SelectB` VARCHAR(45) NOT NULL,
  `SelectC` VARCHAR(45) NOT NULL,
  `SelectD` VARCHAR(45) NOT NULL,
  `CorrectAnswer` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Q_ID`, `Image_ID`),
  CONSTRAINT `Image_ID`
    FOREIGN KEY (`Image_ID`)
    REFERENCES `Experiment`.`Image` (`Image_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `Experiment`.`ParticipateAnswer` (
  `Student_ID` VARCHAR(45) NOT NULL,
  `Image_ID` VARCHAR(45) NOT NULL,
  `Q_ID` VARCHAR(45) NOT NULL,
  `Answer` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Student_ID`, `Image_ID`, `Q_ID`));

CREATE TABLE `Experiment`.`ImageGrade` (
  `Image_ID` VARCHAR(45) NOT NULL,
  `Student_ID` VARCHAR(45) NOT NULL,
  `Grade` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Image_ID`, `Student_ID`));

CREATE TABLE `Experiment`.`UseTime` (
  `Student_ID` VARCHAR(45) NOT NULL,
  `Image_ID` VARCHAR(45) NOT NULL,
  `UseTime` BIGINT NOT NULL,
  PRIMARY KEY (`Student_ID`, `Image_ID`));

