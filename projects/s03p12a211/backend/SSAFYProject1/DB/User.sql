DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_no` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NULL,
  `name` VARCHAR(45) NULL,
  `gender` VARCHAR(2) NULL,
  `birth` varchar(20) NULL,
  `phone` VARCHAR(45) NULL,
  `isSNS` BOOLEAN DEFAULT FALSE,
  PRIMARY KEY (`user_no`))
ENGINE = InnoDB DEFAULT CHARACTER SET = utf8 COLLATE = utf8_bin;