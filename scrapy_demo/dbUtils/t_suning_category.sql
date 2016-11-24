/*
Navicat MySQL Data Transfer

Source Server         : 239-抓取本地数据库
Source Server Version : 50145
Source Host           : 192.168.100.239:3306
Source Database       : Spider

Target Server Type    : MYSQL
Target Server Version : 50145
File Encoding         : 65001

Date: 2016-11-23 17:43:28
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_suning_category
-- ----------------------------
DROP TABLE IF EXISTS `t_suning_category`;
CREATE TABLE `t_suning_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(255) DEFAULT NULL,
  `ware` varchar(255) DEFAULT NULL,
  `wareUrl` varchar(255) DEFAULT NULL,
  `imgUrl` varchar(255) DEFAULT NULL,
  `memo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1349 DEFAULT CHARSET=utf8;
