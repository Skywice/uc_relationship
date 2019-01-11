-- ----------------------------
-- 1. ip_pool 代理IP表
-- ----------------------------
-- DROP TABLE IF EXISTS `ip_pool`;
CREATE TABLE IF NOT EXISTS `ip_pool`(
    `id` INT(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `ip` VARCHAR(20) DEFAULT NULL,
    `port` VARCHAR(20) DEFAULT NULL,
    `claim_time` float DEFAULT 0.0 COMMENT 'response time from website',
    `test_time` float DEFAULT 0.0 COMMENT 'test response time',
    `pro_type` VARCHAR(20) DEFAULT NULL COMMENT '协议类型 HTTP/HTTPS',
    `net_type` VARCHAR(20) DEFAULT NULL COMMENT '网络类型 hide(高匿)/norm(norm)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- 2. news 新闻
-- ----------------------------
-- DROP TABLE IF EXISTS `news`;
CREATE TABLE IF NOT EXISTS `news`(
    `id` INT(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `date` VARCHAR(20) DEFAULT NULL COMMENT '新闻日期',
    `time` VARCHAR(20) DEFAULT NULL COMMENT '新闻时间',
    `title` TEXT DEFAULT NULL COMMENT '新闻标题',
    `content` MEDIUMTEXT DEFAULT NULL COMMENT '新闻内容',
    `link` VARCHAR(100) DEFAULT NULL COMMENT '网页链接',
    `media` VARCHAR(20) DEFAULT NULL COMMENT '新闻媒体',
    `language` VARCHAR(20) DEFAULT NULL COMMENT '新闻语言：中,英'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;