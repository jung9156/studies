DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_no` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NULL,
  `gender` VARCHAR(2) NULL,
  `birth` DATE NULL,
  `phone` VARCHAR(45) NULL,
  PRIMARY KEY (`user_no`))
ENGINE = InnoDB DEFAULT CHARACTER SET = utf8 COLLATE = utf8_bin;