DROP TABLE IF EXISTS `ssafyproject1`.`violation`;
CREATE TABLE `ssafyproject1`.`violation` (
  `violation_no` INT NOT NULL AUTO_INCREMENT,
  `user_no` INT NOT NULL,
  `item` VARCHAR(45) NULL,
  `date` VARCHAR(45) NOT NULL,
  `time` VARCHAR(45) NOT NULL,
  `car_num` VARCHAR(45) NULL,
  `spot` VARCHAR(45) NULL,
  `address` VARCHAR(50) NULL,
  `contents` VARCHAR(100) NULL,
  `video_url` VARCHAR(50) NOT NULL,
  `report_status` INT NULL,
  `lat` VARCHAR(45) NOT NULL,
  `lng` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`violation_no`, `user_no`),
  FOREIGN KEY (`user_no`) REFERENCES `user` (`user_no`) on delete cascade)
ENGINE = InnoDB DEFAULT CHARACTER SET = utf8 COLLATE = utf8_bin;