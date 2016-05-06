-- phpMyAdmin SQL Dump
-- version 3.3.8.1
-- http://www.phpmyadmin.net
--
-- 主机: w.rdc.sae.sina.com.cn:3307
-- 生成日期: 2016 年 01 月 07 日 13:17
-- 服务器版本: 5.5.23
-- PHP 版本: 5.3.3
USE Experiment;

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `app_sysujob`
--

-- --------------------------------------------------------

--
-- 表的结构 `User`
--
/*
CREATE TABLE IF NOT EXISTS `User` (
  `Student_ID` varchar(45) NOT NULL,
  `Name` varchar(45) NOT NULL,
  PRIMARY KEY (`Student_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
*/
--
-- 转存表中的数据 `User`
--

INSERT INTO `User` (`Student_ID`, `Name`) VALUES
('14302191', 'zhangxiaoxin'),
('14302006', 'Jonathan'),
('14302192', 'zhangxin'),
('14302193', 'zhangyaoyun'),
('14302034', 'Esy'),
('14302030', 'guoyingying'),
('14302133', 'wangdanni'),
('14302100', 'lvsiying'),
('14302037', 'huangchuanqi'),
('14302141', 'Wang Weiding'),
('14302031', ' guozixuan'),
('14302124', 'qinyun'),
('13349099', 'Sun binglun'),
('14302008', 'caizhilong'),
('14302096', 'luminghua'),
('13331088', 'huanglingling'),
('13301174', 'zhangyu'),
('13331079', 'huyinglin'),
('15211783', 'zhongyya'),
('14302024', 'dumin'),
('14302028', 'Gong Yuqiong'),
('14302053', 'laile'),
('14302186', 'zhanglinglong'),
('15211792', 'JingYibu'),
('13301175', 'Zheng Yuyi'),
('14302209', 'zhangshiyue'),
('15214228', 'glglzb'),
('13331024', 'chenxuanfeng'),
('13301176', 'ZHOU'),
('12330165', 'lijianhua'),
('14302140', 'wangsonlin'),
('14302036', 'huangbaiquan'),
('13331182', 'longliling'),
('14302208', 'zhouqibin'),
('13331145', 'linchuting'),
('13331183', 'Jukia'),
('15214226', 'xujianqiao'),
('14302047', 'jia xinyue'),
('12330349', 'xuxin'),
('13323007', 'chengken'),
('15211730', 'weizhen'),
('120085', 'maoli'),
('15212957', 'HMQ'),
('13306140', 'tanj'),
('13307427', 'xubeing'),
('13326053', 'yangxin'),
('15110292', 'WANG YIHENG'),
('13110311', 'hewei'),
('15110288', 'Sunny '),
('14302207', 'ZhouMei'),
('14302016', 'CHENSIEN'),
('14302205', 'zhongyujie'),
('14302055', 'lanjuan'),
('15361017', 'xuyang'),
('12345678', 'zhengdanni'),
('13323017', 'gsc'),
('14302144', 'wangyujie'),
('14302131', 'Iris'),
('14302197', 'jannica'),
('14302083', 'linzhiyun'),
('15331202', 'linmiao'),
('15331224', 'LuJiaxi'),
('14302057', 'lei lingyu'),
('13331156', 'linxiaomin'),
('13331166', 'liuchang'),
('14302007', 'CaiYing'),
('14302091', 'LIUXINGCHEN'),
('14323041', 'liu xinliang'),
('13332005', 'HuangGeyu'),
('13332016', 'ou yang guo lin'),
('14302061', 'liaixin'),
('15331103', 'hongzhenwe'),
('15331100', 'romeoking'),
('14312065', 'zhou yingxin'),
('14311030', 'pengqh'),
('14302129', 'Tang Weijuan'),
('14302011', 'chendantong'),
('14302155', 'wuyifan'),
('14302182', 'yuanqinghua'),
('15324051', 'lvzhenzhen'),
('14302073', 'liansijuan'),
('13331173-2', 'lmoavne'),
('14302090', 'liutt'),
('15361005', 'huqiuyue'),
('14348025', 'Alan'),
('14348019-2', 'duchengyi'),
('14302012', 'chenjiaqi'),
('15308023', 'Grace'),
('15308020', 'lidan'),
('14952006', 'yu zhi long'),
('13331167', 'liuzhuopeng'),
('13331071', 'heweiyong'),
('13331157', 'linyiting'),
('13331169', 'liujch'),
('14970011', 'songsiting'),
('14302145', 'wangzihan'),
('14302065', 'lily'),
('14302121', 'shuaishuai'),
('14302116', 'qiumingrong'),
('15308046', 'xionghj'),
('15308010', 'HongLantian'),
('13331375', 'zhoutengteng'),
('13331125', 'litianpei'),
('15351041', 'lanjiao'),
('12330173', 'KenLee'),
('12330277', 'shuizm'),
('13331021', 'cxy'),
('13331174', 'shuangshaung'),
('15343031', 'jiangshitong'),
('15343033', 'kuangruncong'),
('15331199', 'jinghua lin'),
('15331188', 'liaochongxiang'),
('15358092', 'Lam'),
('15351034', 'huangyj'),
('13331075', 'hexiang'),
('14302072', 'Dorothy'),
('15321016', 'lulu'),
('15351043', 'leijialu'),
('14307151', 'Wei Zihan'),
('14307147', 'saran'),
('14313130', 'tangjiajun'),
('12330340', 'fairyshaw'),
('14302046', 'huangyushan'),
('14302045-2', 'huangyishu'),
('12330345', 'Xieyuan'),
('12330298', 'wangchengcheng'),
('12330363', 'yangjing');
