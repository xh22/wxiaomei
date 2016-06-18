CREATE TABLE `subscribe_calendar` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `start` char(20) NOT NULL DEFAULT '',
  `end` char(20) NOT NULL DEFAULT '',
  `type` smallint(11) NOT NULL,
  `email` char(20) NOT NULL DEFAULT '',
  `title` char(20) DEFAULT NULL,
  `create_time` TIMESTAMP  NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `product_type` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `type` int(11) NOT NULL COMMENT '产品类型',
  `description` text COMMENT '产品描述',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `user_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(20) NOT NULL DEFAULT '',
  `phone` int(11) NOT NULL,
  `address` char(50) DEFAULT NULL,
  `password` char(20) NOT NULL DEFAULT '',
  `email` char(20) DEFAULT '',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
