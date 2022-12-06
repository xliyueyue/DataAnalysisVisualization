/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50625
Source Host           : localhost:3306
Source Database       : k12edu

Target Server Type    : MYSQL
Target Server Version : 50625
File Encoding         : 65001

Date: 2020-06-10 15:52:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for grade_count_compare1
-- ----------------------------
DROP TABLE IF EXISTS `grade_count_compare1`;
CREATE TABLE `grade_count_compare1` (
  `count` bigint(20) DEFAULT NULL,
  `data_type` text,
  `grade` text,
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of grade_count_compare1
-- ----------------------------
INSERT INTO `grade_count_compare1` VALUES ('138', 'xdf', '初二', '17179869186');
INSERT INTO `grade_count_compare1` VALUES ('276', 'xdf', '高三', '6');
INSERT INTO `grade_count_compare1` VALUES ('25', 'xdf', '高二', '8589934597');
INSERT INTO `grade_count_compare1` VALUES ('492', 'xdf', '六年级', '8');
INSERT INTO `grade_count_compare1` VALUES ('3', 'xdf', '四年级', '11');
INSERT INTO `grade_count_compare1` VALUES ('489', 'xdf', '初三', '8589934599');
INSERT INTO `grade_count_compare1` VALUES ('3', 'xdf', '三年级', '10');
INSERT INTO `grade_count_compare1` VALUES ('9', 'xdf', '一年级', '7');
INSERT INTO `grade_count_compare1` VALUES ('4', 'xdf', '二年级', '17179869187');
INSERT INTO `grade_count_compare1` VALUES ('689', 'xdf', '高一', '8589934596');
INSERT INTO `grade_count_compare1` VALUES ('2', 'xdf', '五年级', '9');
INSERT INTO `grade_count_compare1` VALUES ('103', 'xdf', '初一', '8589934598');
INSERT INTO `grade_count_compare1` VALUES ('5', 'jh', '五年级', '0');
INSERT INTO `grade_count_compare1` VALUES ('5', 'jh', '三年级', '3');
INSERT INTO `grade_count_compare1` VALUES ('44', 'jh', '初二', '17179869185');
INSERT INTO `grade_count_compare1` VALUES ('56', 'jh', '高三', '5');
INSERT INTO `grade_count_compare1` VALUES ('1', '0', '一年级', '4');
INSERT INTO `grade_count_compare1` VALUES ('92', 'jh', '初三', '8589934594');
INSERT INTO `grade_count_compare1` VALUES ('26', 'jh', '初一', '8589934595');
INSERT INTO `grade_count_compare1` VALUES ('51', 'jh', '六年级', '2');
INSERT INTO `grade_count_compare1` VALUES ('6', 'jh', '四年级', '1');
INSERT INTO `grade_count_compare1` VALUES ('37', 'jh', '高一', '8589934592');
INSERT INTO `grade_count_compare1` VALUES ('30', 'jh', '高二', '8589934593');
INSERT INTO `grade_count_compare1` VALUES ('4', 'jh', '二年级', '17179869184');

-- ----------------------------
-- Table structure for g_price
-- ----------------------------
DROP TABLE IF EXISTS `g_price`;
CREATE TABLE `g_price` (
  `course` text,
  `price` double DEFAULT NULL,
  `count` bigint(20) NOT NULL,
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of g_price
-- ----------------------------
INSERT INTO `g_price` VALUES ('联报', '6026.5542857142855', '175', '231928233984');
INSERT INTO `g_price` VALUES ('生物', '1728.7388888888888', '180', '395136991232');
INSERT INTO `g_price` VALUES ('化学', '1773.2842105263157', '190', '566935683072');
INSERT INTO `g_price` VALUES ('历史', '1017.1304347826087', '69', '1176821039104');
INSERT INTO `g_price` VALUES ('政治', '861.2820512820513', '39', '214748364800');
INSERT INTO `g_price` VALUES ('物理', '1666.4904214559388', '262', '944892805120');
INSERT INTO `g_price` VALUES ('地理', '1212', '115', '944892805121');
INSERT INTO `g_price` VALUES ('数学', '1581.3064516129032', '372', '1511828488192');
INSERT INTO `g_price` VALUES ('语文', '1467.816933638444', '437', '1477468749824');
INSERT INTO `g_price` VALUES ('英语', '2046.513422818792', '597', '1451698946048');
INSERT INTO `g_price` VALUES ('科学', '1199', '154', '1297080123392');

-- ----------------------------
-- Table structure for jh
-- ----------------------------
DROP TABLE IF EXISTS `jh`;
CREATE TABLE `jh` (
  `course` text,
  `price` double DEFAULT NULL,
  `count` bigint(20) NOT NULL,
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of jh
-- ----------------------------
INSERT INTO `jh` VALUES ('英语', '950.2028985507246', '70', '17179869184');
INSERT INTO `jh` VALUES ('物理', '769.46', '51', '25769803776');
INSERT INTO `jh` VALUES ('生物', '407.75', '4', '42949672960');
INSERT INTO `jh` VALUES ('语文', '1021.0370370370371', '54', '0');
INSERT INTO `jh` VALUES ('化学', '766.2', '35', '34359738368');
INSERT INTO `jh` VALUES ('联报', '2769.3035714285716', '56', '51539607552');
INSERT INTO `jh` VALUES ('数学', '799.0114942528736', '87', '8589934592');

-- ----------------------------
-- Table structure for jh_course
-- ----------------------------
DROP TABLE IF EXISTS `jh_course`;
CREATE TABLE `jh_course` (
  `count` bigint(20) DEFAULT NULL,
  `courcename` text,
  `price` double DEFAULT NULL,
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of jh_course
-- ----------------------------
INSERT INTO `jh_course` VALUES ('35', '化学', '766.2', '8589934592');
INSERT INTO `jh_course` VALUES ('87', '数学', '799.0114942528736', '0');
INSERT INTO `jh_course` VALUES ('54', '语文', '1021.0370370370371', '1');
INSERT INTO `jh_course` VALUES ('51', '物理', '754.3725490196078', '8589934593');
INSERT INTO `jh_course` VALUES ('4', '生物', '407.75', '8589934594');
INSERT INTO `jh_course` VALUES ('56', '联报', '2769.3035714285716', '2');
INSERT INTO `jh_course` VALUES ('70', '英语', '936.6285714285714', '3');

-- ----------------------------
-- Table structure for jh_course1
-- ----------------------------
DROP TABLE IF EXISTS `jh_course1`;
CREATE TABLE `jh_course1` (
  `course` text,
  `avg(price)` double DEFAULT NULL,
  `count(course)` bigint(20) NOT NULL,
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of jh_course1
-- ----------------------------
INSERT INTO `jh_course1` VALUES ('生物', '1758.7613636363637', '176', '51539607552');
INSERT INTO `jh_course1` VALUES ('联报', '7559.378151260505', '119', '68719476736');
INSERT INTO `jh_course1` VALUES ('政治', '861.2820512820513', '39', '25769803776');
INSERT INTO `jh_course1` VALUES ('物理', '1879.0568720379147', '211', '42949672960');
INSERT INTO `jh_course1` VALUES ('化学', '2000.6903225806452', '155', '0');
INSERT INTO `jh_course1` VALUES ('地理', '1212', '115', '17179869184');
INSERT INTO `jh_course1` VALUES ('英语', '2190.053130929791', '527', '77309411328');
INSERT INTO `jh_course1` VALUES ('语文', '1530.809399477807', '383', '85899345920');
INSERT INTO `jh_course1` VALUES ('数学', '1820.1122807017543', '285', '34359738368');
INSERT INTO `jh_course1` VALUES ('科学', '1199', '154', '60129542144');
INSERT INTO `jh_course1` VALUES ('历史', '1017.1304347826087', '69', '8589934592');

-- ----------------------------
-- Table structure for jh_edition
-- ----------------------------
DROP TABLE IF EXISTS `jh_edition`;
CREATE TABLE `jh_edition` (
  `count` bigint(20) DEFAULT NULL,
  `edition` text,
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of jh_edition
-- ----------------------------
INSERT INTO `jh_edition` VALUES ('148', '全国通用', '8589934592');
INSERT INTO `jh_edition` VALUES ('20', '上海牛津', '0');
INSERT INTO `jh_edition` VALUES ('127', '人教', '17179869184');
INSERT INTO `jh_edition` VALUES ('108', '沪教', '17179869185');
INSERT INTO `jh_edition` VALUES ('44', '苏科', '17179869186');

-- ----------------------------
-- Table structure for jh_grade
-- ----------------------------
DROP TABLE IF EXISTS `jh_grade`;
CREATE TABLE `jh_grade` (
  `count` bigint(20) DEFAULT NULL,
  `grade` text,
  `price` double DEFAULT NULL,
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of jh_grade
-- ----------------------------
INSERT INTO `jh_grade` VALUES ('37', '高一', '1200.4594594594594', '8589934592');
INSERT INTO `jh_grade` VALUES ('5', '五年级', '1069', '0');
INSERT INTO `jh_grade` VALUES ('30', '高二', '1130.7', '8589934593');
INSERT INTO `jh_grade` VALUES ('6', '四年级', '931.6666666666666', '1');
INSERT INTO `jh_grade` VALUES ('51', '六年级', '1116.9803921568628', '2');
INSERT INTO `jh_grade` VALUES ('92', '初三', '1175.4347826086957', '8589934594');
INSERT INTO `jh_grade` VALUES ('5', '三年级', '1023.6', '3');
INSERT INTO `jh_grade` VALUES ('26', '初一', '857', '8589934595');
INSERT INTO `jh_grade` VALUES ('1', '一年级', '1440', '4');
INSERT INTO `jh_grade` VALUES ('56', '高三', '1469.9642857142858', '5');
INSERT INTO `jh_grade` VALUES ('4', '二年级', '880.5', '17179869184');
INSERT INTO `jh_grade` VALUES ('44', '初二', '980.8409090909091', '17179869185');

-- ----------------------------
-- Table structure for t_course
-- ----------------------------
DROP TABLE IF EXISTS `t_course`;
CREATE TABLE `t_course` (
  `course` text,
  `price` double DEFAULT NULL,
  `count` bigint(20) NOT NULL,
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_course
-- ----------------------------
INSERT INTO `t_course` VALUES ('英语', '2046.513422818792', '597', '77309411328');
INSERT INTO `t_course` VALUES ('联报', '6026.5542857142855', '175', '68719476736');
INSERT INTO `t_course` VALUES ('化学', '1773.2842105263157', '190', '0');
INSERT INTO `t_course` VALUES ('数学', '1581.3064516129032', '372', '34359738368');
INSERT INTO `t_course` VALUES ('地理', '1212', '115', '17179869184');
INSERT INTO `t_course` VALUES ('政治', '861.2820512820513', '39', '25769803776');
INSERT INTO `t_course` VALUES ('语文', '1467.816933638444', '437', '85899345920');
INSERT INTO `t_course` VALUES ('生物', '1728.7388888888888', '180', '51539607552');
INSERT INTO `t_course` VALUES ('历史', '1017.1304347826087', '69', '8589934592');
INSERT INTO `t_course` VALUES ('物理', '1666.4904214559388', '262', '42949672960');
INSERT INTO `t_course` VALUES ('科学', '1199', '154', '60129542144');

-- ----------------------------
-- Table structure for t_grade
-- ----------------------------
DROP TABLE IF EXISTS `t_grade`;
CREATE TABLE `t_grade` (
  `grade` text,
  `price` double DEFAULT NULL,
  `count` bigint(20) NOT NULL,
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_grade
-- ----------------------------
INSERT INTO `t_grade` VALUES ('二年级', '1207.75', '8', '17179869184');
INSERT INTO `t_grade` VALUES ('高一', '2860.3292011019284', '726', '77309411328');
INSERT INTO `t_grade` VALUES ('高二', '2925.327272727273', '55', '94489280512');
INSERT INTO `t_grade` VALUES ('三年级', '1746', '8', '8589934592');
INSERT INTO `t_grade` VALUES ('四年级', '1082.2222222222222', '9', '68719476736');
INSERT INTO `t_grade` VALUES ('一年级', '1729', '10', '0');
INSERT INTO `t_grade` VALUES ('高三', '3087.6656626506024', '332', '85899345920');
INSERT INTO `t_grade` VALUES ('六年级', '1211.254143646409', '543', '34359738368');
INSERT INTO `t_grade` VALUES ('初二', '1613.9505494505495', '182', '60129542144');
INSERT INTO `t_grade` VALUES ('初一', '1475.2635658914728', '129', '42949672960');
INSERT INTO `t_grade` VALUES ('初三', '955.6804835924007', '581', '51539607552');
INSERT INTO `t_grade` VALUES ('五年级', '935', '7', '25769803776');

-- ----------------------------
-- Table structure for t_material
-- ----------------------------
DROP TABLE IF EXISTS `t_material`;
CREATE TABLE `t_material` (
  `count` int(11) DEFAULT NULL,
  `material` varchar(255) DEFAULT NULL,
  `download` varchar(255) DEFAULT NULL,
  `collection` varchar(255) DEFAULT NULL,
  `id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_material
-- ----------------------------
INSERT INTO `t_material` VALUES ('165', '科学', '53', '112', '0');
INSERT INTO `t_material` VALUES ('444', '语文', '265', '179', '1');
INSERT INTO `t_material` VALUES ('502', '数学', '137', '365', '2');
INSERT INTO `t_material` VALUES ('603', '英语', '270', '333', '3');
INSERT INTO `t_material` VALUES ('278', '物理', '86', '192', '4');
INSERT INTO `t_material` VALUES ('202', '化学', '98', '104', '5');
INSERT INTO `t_material` VALUES ('179', '生物', '66', '113', '6');
INSERT INTO `t_material` VALUES ('81', '历史', '27', '54', '7');
INSERT INTO `t_material` VALUES ('111', '地理', '49', '62', '8');
INSERT INTO `t_material` VALUES ('53', '政治', '22', '31', '9');
INSERT INTO `t_material` VALUES ('188', '综合', '64', '124', '10');

-- ----------------------------
-- Table structure for xdf
-- ----------------------------
DROP TABLE IF EXISTS `xdf`;
CREATE TABLE `xdf` (
  `course` text,
  `price` double DEFAULT NULL,
  `count` bigint(20) NOT NULL,
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xdf
-- ----------------------------
INSERT INTO `xdf` VALUES ('联报', '7559.378151260505', '119', '51539607552');
INSERT INTO `xdf` VALUES ('历史', '1017.1304347826087', '69', '60129542144');
INSERT INTO `xdf` VALUES ('数学', '1820.1122807017543', '285', '8589934592');
INSERT INTO `xdf` VALUES ('地理', '1212', '115', '77309411328');
INSERT INTO `xdf` VALUES ('物理', '1879.0568720379147', '211', '25769803776');
INSERT INTO `xdf` VALUES ('生物', '1758.7613636363637', '176', '42949672960');
INSERT INTO `xdf` VALUES ('语文', '1530.809399477807', '383', '0');
INSERT INTO `xdf` VALUES ('政治', '861.2820512820513', '39', '68719476736');
INSERT INTO `xdf` VALUES ('科学', '1199', '154', '85899345920');
INSERT INTO `xdf` VALUES ('英语', '2190.053130929791', '527', '17179869184');
INSERT INTO `xdf` VALUES ('化学', '2000.6903225806452', '155', '34359738368');

-- ----------------------------
-- Table structure for xdf_course
-- ----------------------------
DROP TABLE IF EXISTS `xdf_course`;
CREATE TABLE `xdf_course` (
  `count` bigint(20) DEFAULT NULL,
  `courcename` text,
  `price` double DEFAULT NULL,
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xdf_course
-- ----------------------------
INSERT INTO `xdf_course` VALUES ('7', '历史', '892.5714285714286', '17179869184');
INSERT INTO `xdf_course` VALUES ('256', '物理', '829.17578125', '8589934592');
INSERT INTO `xdf_course` VALUES ('59', '生物', '1095.135593220339', '8589934593');
INSERT INTO `xdf_course` VALUES ('123', '化学', '880.5121951219512', '8589934594');
INSERT INTO `xdf_course` VALUES ('7', '政治', '975.5714285714286', '8589934595');
INSERT INTO `xdf_course` VALUES ('154', '科学', '1199', '8589934596');
INSERT INTO `xdf_course` VALUES ('122', '联报', '8066.836065573771', '0');
INSERT INTO `xdf_course` VALUES ('435', '语文', '905.9080459770115', '1');
INSERT INTO `xdf_course` VALUES ('748', '英语', '854.6363636363636', '2');
INSERT INTO `xdf_course` VALUES ('463', '数学', '731.2894168466522', '3');
INSERT INTO `xdf_course` VALUES ('19', '地理', '1443.5263157894738', '4');

-- ----------------------------
-- Table structure for xdf_grade
-- ----------------------------
DROP TABLE IF EXISTS `xdf_grade`;
CREATE TABLE `xdf_grade` (
  `count` bigint(20) DEFAULT NULL,
  `grade` text,
  `price` double DEFAULT NULL,
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xdf_grade
-- ----------------------------
INSERT INTO `xdf_grade` VALUES ('276', '高三', '3415.894927536232', '0');
INSERT INTO `xdf_grade` VALUES ('138', '初二', '1815.8115942028985', '17179869184');
INSERT INTO `xdf_grade` VALUES ('4', '二年级', '1535', '17179869185');
INSERT INTO `xdf_grade` VALUES ('9', '一年级', '1761.111111111111', '1');
INSERT INTO `xdf_grade` VALUES ('492', '六年级', '1221.0264227642276', '2');
INSERT INTO `xdf_grade` VALUES ('2', '五年级', '600', '3');
INSERT INTO `xdf_grade` VALUES ('3', '三年级', '2950', '4');
INSERT INTO `xdf_grade` VALUES ('3', '四年级', '1383.3333333333333', '5');
INSERT INTO `xdf_grade` VALUES ('689', '高一', '2949.465892597968', '8589934592');
INSERT INTO `xdf_grade` VALUES ('25', '高二', '5078.88', '8589934593');
INSERT INTO `xdf_grade` VALUES ('103', '初一', '1631.3300970873786', '8589934594');
INSERT INTO `xdf_grade` VALUES ('489', '初三', '910.4274028629857', '8589934595');

-- ----------------------------
-- Table structure for xdf_type
-- ----------------------------
DROP TABLE IF EXISTS `xdf_type`;
CREATE TABLE `xdf_type` (
  `count` bigint(20) DEFAULT NULL,
  `per_price` double DEFAULT NULL,
  `type` text,
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xdf_type
-- ----------------------------
INSERT INTO `xdf_type` VALUES ('172', '98.5393494592784', '直播', '0');
INSERT INTO `xdf_type` VALUES ('3', '40', '面授+直播', '8589934592');
INSERT INTO `xdf_type` VALUES ('51', '45.98873892991542', '住宿', '1');
INSERT INTO `xdf_type` VALUES ('6', '117.22222222222221', 'None', '2');
INSERT INTO `xdf_type` VALUES ('2142', '111.04635875799394', '面授', '17179869184');
INSERT INTO `xdf_type` VALUES ('3', '50', '录播', '17179869185');
INSERT INTO `xdf_type` VALUES ('16', '59.9375', '可在线', '17179869186');
