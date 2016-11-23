/*
Navicat MySQL Data Transfer

Source Server         : 239-抓取本地数据库
Source Server Version : 50145
Source Host           : 192.168.100.239:3306
Source Database       : Spider

Target Server Type    : MYSQL
Target Server Version : 50145
File Encoding         : 65001

Date: 2016-11-23 17:47:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_suning_ware
-- ----------------------------
DROP TABLE IF EXISTS `t_suning_ware`;
CREATE TABLE `t_suning_ware` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `catentryId` int(11) DEFAULT NULL,
  `catentdesc` varchar(255) DEFAULT NULL,
  `price` decimal(10,0) DEFAULT NULL,
  `praiseRate` varchar(255) DEFAULT NULL,
  `countOfarticle` varchar(255) DEFAULT NULL,
  `auxdescription` varchar(255) DEFAULT NULL,
  `salesCode` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
