USE Experiment;

INSERT INTO `Image` (`Image_ID`, `Question_count`) VALUES
('1', 4),
('2', 4),
('3', 4),
('4', 4);

INSERT INTO `Question` (`Image_ID`, `Q_ID`, `Question`, `SelectA`, `SelectB`, `SelectC`, `SelectD`, `CorrectAnswer`) VALUES
('1', '1', '1', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('1', '2', '2', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('1', '3', '3', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('1', '4', '4', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('2', '1', '1', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('2', '2', '2', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('2', '3', '3', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('2', '4', '4', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('3', '1', '1', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('3', '2', '2', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('3', '3', '3', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('3', '4', '4', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('4', '1', '1', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('4', '2', '2', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('4', '3', '3', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C'),
('4', '4', '4', 'AAAAA', 'BBBBB', 'CCCCC', 'DDDDDD', 'C');