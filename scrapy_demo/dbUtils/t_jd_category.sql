/*
Navicat MySQL Data Transfer

Source Server         : 239-抓取本地数据库
Source Server Version : 50145
Source Host           : 192.168.100.239:3306
Source Database       : Spider

Target Server Type    : MYSQL
Target Server Version : 50145
File Encoding         : 65001

Date: 2016-11-25 17:46:22
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_jd_category
-- ----------------------------
DROP TABLE IF EXISTS `t_jd_category`;
CREATE TABLE `t_jd_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category1` varchar(255) DEFAULT NULL,
  `category2` varchar(255) DEFAULT NULL,
  `category3` varchar(255) DEFAULT NULL,
  `cid1` varchar(255) DEFAULT NULL,
  `cid3` varchar(255) DEFAULT NULL,
  `c3Url` varchar(255) DEFAULT NULL,
  `path` varchar(255) DEFAULT NULL,
  `searchKey` varchar(255) DEFAULT NULL,
  `cid2` varchar(255) DEFAULT NULL,
  `actionUrl` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10029 DEFAULT CHARSET=utf8;
