DROP TABLE IF EXISTS `notice`;
CREATE TABLE `notice` (
  `notice_no` int NOT NULL AUTO_INCREMENT,
  `notice_id` varchar(20) DEFAULT NULL,
  `notice_title` varchar(100) DEFAULT NULL,
  `notice_content` varchar(2000) DEFAULT NULL,
  `notice_regtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`notice_no`))
  ENGINE = InnoDB DEFAULT CHARACTER SET = utf8 COLLATE = utf8_bin;