CREATE TABLE `user_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(20) NOT NULL DEFAULT '',
  `phone` int(11) NOT NULL,
  `address` char(50) DEFAULT NULL,
  `password` char(20) NOT NULL DEFAULT '',
  `email` char(20) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
