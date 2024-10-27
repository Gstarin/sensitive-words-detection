CREATE DATABASE  IF NOT EXISTS `sensitive_word_system` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `sensitive_word_system`;
-- MySQL dump 10.13  Distrib 8.0.34, for macos13 (arm64)
--
-- Host: localhost    Database: sensitive_word_system
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `words`
--

DROP TABLE IF EXISTS `words`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `words` (
  `id` int NOT NULL AUTO_INCREMENT,
  `word` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `regex` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `type` tinyint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `word` (`word`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `words`
--

LOCK TABLES `words` WRITE;
/*!40000 ALTER TABLE `words` DISABLE KEYS */;
INSERT INTO `words` VALUES (1,'“两学一做”学习教育','/[^“]两学一做[^“]|“两学一做”学习教育活动/u',1),(2,'反腐倡廉','/反[\\x{4e00}-\\x{9fa5}]倡[\\x{4e00}-\\x{9fa5}]|倡反腐|倡廉反|反腐廉|防腐倡廉|腐倡廉|反腐创廉/u',0),(3,'扫黑除恶','/扫[\\x{4e00}-\\x{9fa5}]除[\\x{4e00}-\\x{9fa5}]|打黑除恶|除恶打黑|除恶扫黑/u',0),(4,'《中华人民共和国合同法》','/《[\\x{4e00}-\\x{9fa5}]{0,8}合同法》/u',0),(5,'村民委员会','/村[\\x{4e00}-\\x{9fa5}]{0,1}委[\\x{4e00}-\\x{9fa5}]{0,1}会/u',1),(6,'侵华日军南京大屠杀遇难同胞纪念馆','/[\\x{4e00}-\\x{9fa5}]{0,4}南京大屠杀[\\x{4e00}-\\x{9fa5}]{0,6}馆/u',1),(7,'庆祝建党','/纪念建党/u',1),(8,'庆祝中国共产党','/纪念中[\\x{4e00}-\\x{9fa5}]{0,1}共/u',1),(9,'中国共产党建党','/[^中][^国]共产党建党/u',1),(10,'中国共产党建党一百周年','/[^中][^国]共产党建党[\\x{4e00}-\\x{9fa5}]{0,1}百[\\x{4e00}-\\x{9fa5}]{0,1}年|共产党一百年/u',1),(11,'改革开放','/改 革开放|改草革开放|改革 开放|改革放开|改革开 放|改革开发|改[\\x{4e00}-\\x{9fa5}]{2}放/u',1),(12,'党史学习教育','/党史学习活动|党史学习教育活动/u',1),(13,'村民委员会主任','/村长/u',1),(14,'检察长','/[最][高][检]检察长/u',1),(15,'新冠肺炎','/新冠状肺炎/u',0),(16,'志存高远、脚踏实地','/志[\\x{4e00}-\\x{9fa5}]{0,1}高远、[\\x{4e00}-\\x{9fa5}]{2,4}实地/u',0),(17,'四中全会','/四[\\x{4e00}-\\x{9fa5}]{0,1}全会/u',1),(18,'六中全会','/六[\\x{4e00}-\\x{9fa5}]{0,1}全会/u',1),(19,'安徽','/安微/u',0),(20,'部署','/部暑/u',0),(21,'书记','/书纪/u',0),(22,'政府','/镇府/u',0),(23,'特色','/特设/u',0),(24,'自找苦吃','/自讨苦吃/u',0),(25,'建功立业','/建工立业/u',0),(26,'走进乡土中国深处','/走进中国乡土深处/u',0),(27,'强国先强农、农大作先锋','/国先强农，农大[^作]先锋/u',0),(28,'把课堂学习和乡村实践紧密结合起来','/把课堂[\\x{4e00}-\\x{9fa5}]{2,4}乡村[\\x{4e00}-\\x{9fa5}]{2,5}结合起来/u',0),(29,'厚植爱农情怀，练就兴农本领','/厚植[\\x{4e00}-\\x{9fa5}]{3,4}，练就[\\x{4e00}-\\x{9fa5}]{2,4}/u',0);
/*!40000 ALTER TABLE `words` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-28  3:28:04
