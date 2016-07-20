CREATE TABLE `subscribe_calendar` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `start` int(20) NOT NULL,
  `end` int(20) NOT NULL,
  `type` smallint(11) NOT NULL,
  `title` text,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
  KEY `index_name` (`type`,`start`,`title`)
) ENGINE=InnoDB AUTO_INCREMENT=4616 DEFAULT CHARSET=utf8;

CREATE TABLE `product_type` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `type` int(11) NOT NULL COMMENT '产品类型',
  `description` text COMMENT '产品描述',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `user_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(20) NOT NULL DEFAULT '',
  `phone` int(11) NOT NULL DEFAULT '',
  `password` char(20) NOT NULL DEFAULT '',
  `email` char(20) NOT NULL DEFAULT '',
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
