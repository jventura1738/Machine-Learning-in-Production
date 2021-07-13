# china_area_mysql
## 中国5级行政区域mysql库

  爬取国家统计局官网的行政区域数据,包括省市县镇村5个层级;
  
  港澳地区的数据只有3级;台湾地区4级;
  
  包含大陆地区的邮政编码和经纬度信息.
  
---------------------------------------
#####  cnarea20200630.7z 是爬取2020年的数据,截止2020年6月30日.

  全部共 **758049** 条  
  - 大陆数据共**679237** 条,其中
     - 省/直辖市 `31`
     - 市/州 `342`
     - 县/区 `3348`
     - 乡/镇 `42757`
     - 村/社区 `632759`
     
  - 港澳台数据共**78812** 条,其中
     - 省/特区 `3`
     - 港澳辖区 `33`
     - 台湾市/县 `23`
     - 台湾区/镇 `371`
     - 台湾街道/村 `78384`  

  - 改动:   
    - 2020比2019的数据少了25513条记录
    - 具体说明见 [#56](https://github.com/kakuilan/china_area_mysql/issues/56)

### 表结构

```mysql

CREATE TABLE `cnarea_2020` (
  `id` mediumint(7) unsigned NOT NULL AUTO_INCREMENT,
  `level` tinyint(1) unsigned NOT NULL COMMENT '层级',
  `parent_code` bigint(14) unsigned NOT NULL DEFAULT '0' COMMENT '父级行政代码',
  `area_code` bigint(14) unsigned NOT NULL DEFAULT '0' COMMENT '行政代码',
  `zip_code` mediumint(6) unsigned zerofill NOT NULL DEFAULT '000000' COMMENT '邮政编码',
  `city_code` char(6) NOT NULL DEFAULT '' COMMENT '区号',
  `name` varchar(50) NOT NULL DEFAULT '' COMMENT '名称',
  `short_name` varchar(50) NOT NULL DEFAULT '' COMMENT '简称',
  `merger_name` varchar(50) NOT NULL DEFAULT '' COMMENT '组合名',
  `pinyin` varchar(30) NOT NULL DEFAULT '' COMMENT '拼音',
  `lng` decimal(10,6) NOT NULL DEFAULT '0.000000' COMMENT '经度',
  `lat` decimal(10,6) NOT NULL DEFAULT '0.000000' COMMENT '纬度',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_code` (`area_code`) USING BTREE,
  KEY `idx_parent_code` (`parent_code`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='中国行政地区表';

```
