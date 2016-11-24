/*
Navicat MySQL Data Transfer

Source Server         : 239-抓取本地数据库
Source Server Version : 50145
Source Host           : 192.168.100.239:3306
Source Database       : Spider

Target Server Type    : MYSQL
Target Server Version : 50145
File Encoding         : 65001

Date: 2016-11-23 17:43:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_lianjia_deal
-- ----------------------------
DROP TABLE IF EXISTS `t_lianjia_deal`;
CREATE TABLE `t_lianjia_deal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(255) DEFAULT NULL,
  `area` varchar(255) DEFAULT NULL,
  `areaUrl` varchar(255) DEFAULT NULL,
  `district` varchar(255) DEFAULT NULL,
  `districtUrl` varchar(255) DEFAULT NULL,
  `houseName` varchar(255) DEFAULT NULL,
  `houseType` varchar(255) DEFAULT NULL,
  `houseArea` varchar(255) DEFAULT NULL,
  `dealTime` datetime DEFAULT NULL,
  `totalPrice` varchar(255) DEFAULT NULL,
  `unitPrice` varchar(255) DEFAULT NULL,
  `floor` varchar(255) DEFAULT NULL,
  `memo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=505819 DEFAULT CHARSET=utf8;
