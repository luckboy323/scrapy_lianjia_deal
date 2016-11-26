/*
Navicat MySQL Data Transfer

Source Server Version : 50145
Source Host           : 192.168.100.239:3306
Source Database       : Spider

Target Server Type    : MYSQL
Target Server Version : 50145
File Encoding         : 65001

Date: 2016-11-25 17:47:16
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
  `countOfarticle` int(255) DEFAULT NULL,
  `auxdescription` varchar(255) DEFAULT NULL,
  `salesCode` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `ware` varchar(255) DEFAULT NULL,
  `srcUrl` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1660720 DEFAULT CHARSET=utf8;
