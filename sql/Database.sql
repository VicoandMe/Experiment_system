DROP DATABASE IF EXISTS `Experiment`;

CREATE DATABASE `Experiment` CHARACTER SET utf8;

USE Experiment;

CREATE TABLE `Experiment`.`User` (
  `Student_ID` VARCHAR(10) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Student_ID`));

CREATE TABLE `Experiment`.`Image` (
  `Image_ID` VARCHAR(10) NOT NULL,
  `Question_count` INT NOT NULL,
  PRIMARY KEY (`Image_ID`));

CREATE TABLE `Experiment`.`Question` (
  `Image_ID` VARCHAR(10) NOT NULL,
  `Q_ID` VARCHAR(10) NOT NULL,
  `Question` VARCHAR(100) NOT NULL,
  `SelectA` VARCHAR(45) NOT NULL,
  `SelectB` VARCHAR(45) NOT NULL,
  `SelectC` VARCHAR(45) NOT NULL,
  `SelectD` VARCHAR(45) NOT NULL,
  `CorrectAnswer` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Q_ID`),
  CONSTRAINT `Image_ID`
    FOREIGN KEY (`Image_ID`)
    REFERENCES `Experiment`.`Image` (`Image_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `Experiment`.`ParticipateAnswer` (
  `Student_ID` VARCHAR(10) NOT NULL,
  `Q_ID` VARCHAR(10) NOT NULL,
  `Answer` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Q_ID`),
  CONSTRAINT `Q_ID`
    FOREIGN KEY (`Q_ID`)
    REFERENCES `Experiment`.`Question` (`Q_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `Experiment`.`UseTime` (
  `Student_ID` VARCHAR(10) NOT NULL,
  `Image_ID` VARCHAR(10) NOT NULL,
  `UseTime` BIGINT NOT NULL,
  PRIMARY KEY (`Student_ID`, `Image_ID`),
  INDEX `Image_ID_idx` (`Image_ID` ASC),
  CONSTRAINT `Student_ID`
    FOREIGN KEY (`Student_ID`)
    REFERENCES `Experiment`.`User` (`Student_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Image_ID`
    FOREIGN KEY (`Image_ID`)
    REFERENCES `Experiment`.`Image` (`Image_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

