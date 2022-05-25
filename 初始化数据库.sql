drop database if exists 南昌天气;
create database 南昌天气 character set utf8 collate utf8_general_ci;
use 南昌天气;
create table 每月数据
(
    日期     varchar(10)              not null,
    平均高温   varchar(10) default '未知' null,
    平均低温   varchar(10) default '未知' null,
    极端高温   varchar(10) default '未知' null,
    极端低温   varchar(10) default '未知' null,
    平均空气质量 varchar(10) default '未知' null,
    空气最好   varchar(10) default '未知' null,
    空气最差   varchar(10) default '未知' null
)
    comment '每月的天气指标';

create table 每日数据
(
    日期     varchar(30)              not null,
    最高温    varchar(10) default '未知' null,
    最低温    varchar(10) default '未知' null,
    天气     varchar(20) default '未知' null,
    风力风向   varchar(20) default '未知' null,
    空气质量指数 varchar(20) default '未知' null
)
    comment '每天的天气指标';
