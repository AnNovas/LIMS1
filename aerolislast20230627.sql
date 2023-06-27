CREATE DATABASE  IF NOT EXISTS `mydb` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mydb`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `analyticaldata`
--

DROP TABLE IF EXISTS `analyticaldata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analyticaldata` (
  `idAnalyticalData` int NOT NULL,
  `AnDataName` varchar(100) DEFAULT NULL,
  `AnDataSN` varchar(100) DEFAULT NULL,
  `ADUnits` varchar(100) DEFAULT NULL,
  `ADUnitsSN` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idAnalyticalData`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analyticaldata`
--

LOCK TABLES `analyticaldata` WRITE;
/*!40000 ALTER TABLE `analyticaldata` DISABLE KEYS */;
INSERT INTO `analyticaldata` VALUES (1,'Молекулярная масса','М','КилоДальтон','кДа'),(2,'Истинная плотность','p(и)','-','кг/м3'),(3,'Средняя плотность','р(ср)','-','кг/м3'),(4,'Насыпная плотность','р(н)','-','кг/м3'),(5,'Удельная площадь поверхности','S(уд)','-','м2/г'),(6,'Объем пор','V(пор)','-','см3/г'),(7,'Диаметр пор','d(пор)','-','нм'),(8,'Диаметр фибриллы','d(фибр)','-','нм'),(9,'Сорбционная емкость','-','-','г/г'),(10,'Пористость',NULL,NULL,'%'),(11,'Кажущаяся плотность',NULL,NULL,'кг/м3');
/*!40000 ALTER TABLE `analyticaldata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipment`
--

DROP TABLE IF EXISTS `equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipment` (
  `idEquipment` int NOT NULL,
  `EquipName` varchar(200) DEFAULT NULL,
  `EquipType_idEquipType` int NOT NULL,
  `DateReceived` date DEFAULT NULL,
  `SerialNumber` varchar(200) DEFAULT NULL,
  `StorageNumber` varchar(200) DEFAULT NULL,
  `Location_idLocation` int NOT NULL,
  PRIMARY KEY (`idEquipment`,`EquipType_idEquipType`,`Location_idLocation`),
  KEY `fk_Equipment_Location1_idx` (`Location_idLocation`),
  KEY `fk_equipment_EquipType1_idx` (`EquipType_idEquipType`),
  CONSTRAINT `fk_equipment_EquipType1` FOREIGN KEY (`EquipType_idEquipType`) REFERENCES `equiptype` (`idEquipType`),
  CONSTRAINT `fk_Equipment_Location1` FOREIGN KEY (`Location_idLocation`) REFERENCES `location` (`idLocation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipment`
--

LOCK TABLES `equipment` WRITE;
/*!40000 ALTER TABLE `equipment` DISABLE KEYS */;
INSERT INTO `equipment` VALUES (1,'Форсунка',1,'2022-03-04','48399','347384',1),(2,'Диспергатор',1,'2022-05-06','47593','654054',2),(3,'Лопастная мешалка',1,'2022-09-02','32894','437859',3),(4,'Лиофильная сушилка',2,'2022-03-01','45783','473859',2),(5,'Центрифуга',1,'2022-08-07','23058','537290',1),(6,'СК-оборудование',2,'2022-09-01','23984','346278',2),(7,'Азотный порозиметр',3,'2022-06-04','34278','234789',3),(8,'Газовый пикнометр',3,'2022-03-05','32419','549568',2),(9,'Спектрофотометр',3,'2000-01-01','74835','246378',1),(10,'ВЭЖХ',3,'2000-01-01','37482','327403',2),(11,'Влагоанализатор',3,'2000-01-01','36274','495030',2),(12,'Гелиевый пикнометр',3,'2000-01-01','47385','235748',2),(13,'Шприцевой насос',1,'2000-01-01','43758','437854',2),(14,'Тераометр',3,'2000-01-01','34758','237589',2);
/*!40000 ALTER TABLE `equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equiptype`
--

DROP TABLE IF EXISTS `equiptype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equiptype` (
  `idEquipType` int NOT NULL,
  `ETypeName` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`idEquipType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equiptype`
--

LOCK TABLES `equiptype` WRITE;
/*!40000 ALTER TABLE `equiptype` DISABLE KEYS */;
INSERT INTO `equiptype` VALUES (1,'Формообразующее оборудование'),(2,'Сушилка'),(3,'Аналитическое оборудование'),(4,'Другое');
/*!40000 ALTER TABLE `equiptype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipusage`
--

DROP TABLE IF EXISTS `equipusage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipusage` (
  `idEquipUsage` int NOT NULL,
  `TimeStart` time DEFAULT NULL,
  `TimeFinish` time DEFAULT NULL,
  `Equipment_idEquipment` int NOT NULL,
  `ExperimentDate_idExperimentDate` int NOT NULL,
  PRIMARY KEY (`idEquipUsage`,`Equipment_idEquipment`,`ExperimentDate_idExperimentDate`),
  KEY `fk_EquipUsage_Equipment1_idx` (`Equipment_idEquipment`),
  KEY `fk_equipusage_experimentDate1_idx` (`ExperimentDate_idExperimentDate`),
  CONSTRAINT `fk_EquipUsage_Equipment1` FOREIGN KEY (`Equipment_idEquipment`) REFERENCES `equipment` (`idEquipment`),
  CONSTRAINT `fk_equipusage_experimentDate1` FOREIGN KEY (`ExperimentDate_idExperimentDate`) REFERENCES `experimentdate` (`idExperimentDate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipusage`
--

LOCK TABLES `equipusage` WRITE;
/*!40000 ALTER TABLE `equipusage` DISABLE KEYS */;
INSERT INTO `equipusage` VALUES (13,'13:00:00','15:00:00',13,25),(14,'11:00:00','18:00:00',6,28),(15,'11:00:00','13:00:00',13,30),(16,'13:00:00','15:00:00',13,42);
/*!40000 ALTER TABLE `equipusage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipverifinfo`
--

DROP TABLE IF EXISTS `equipverifinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipverifinfo` (
  `idEquipVerifInfo` int NOT NULL,
  `Calibration` varchar(200) DEFAULT NULL,
  `Verification` varchar(200) DEFAULT NULL,
  `Attestation` varchar(200) DEFAULT NULL,
  `Qualification` varchar(200) DEFAULT NULL,
  `Documentation` varchar(200) DEFAULT NULL,
  `Equipment_idEquipment` int NOT NULL,
  PRIMARY KEY (`idEquipVerifInfo`,`Equipment_idEquipment`),
  KEY `fk_EquipVerifInfo_Equipment1_idx` (`Equipment_idEquipment`),
  CONSTRAINT `fk_EquipVerifInfo_Equipment1` FOREIGN KEY (`Equipment_idEquipment`) REFERENCES `equipment` (`idEquipment`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipverifinfo`
--

LOCK TABLES `equipverifinfo` WRITE;
/*!40000 ALTER TABLE `equipverifinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `equipverifinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiment`
--

DROP TABLE IF EXISTS `experiment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiment` (
  `idExperiment` int NOT NULL,
  `ExpName` varchar(300) DEFAULT NULL,
  `ResearchProject_idResearchProject` int NOT NULL,
  PRIMARY KEY (`idExperiment`,`ResearchProject_idResearchProject`),
  KEY `fk_Experiment_ResearchProject1_idx` (`ResearchProject_idResearchProject`),
  CONSTRAINT `fk_Experiment_ResearchProject1` FOREIGN KEY (`ResearchProject_idResearchProject`) REFERENCES `researchproject` (`idResearchProject`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiment`
--

LOCK TABLES `experiment` WRITE;
/*!40000 ALTER TABLE `experiment` DISABLE KEYS */;
INSERT INTO `experiment` VALUES (11,'Образец 1',1),(12,'Образец 2',1),(13,'Образец 3',1),(14,'Образец 4',1),(15,'Образец 5',1),(16,'Образец 6',1),(17,'Образец 7',1),(18,'Образец 8',1),(19,'Образец 9',1),(20,'Образец 10',1),(21,'Образец 11',1),(22,'Образец 12',1),(23,'Образец 13',1);
/*!40000 ALTER TABLE `experiment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiment_has_analyticaldata`
--

DROP TABLE IF EXISTS `experiment_has_analyticaldata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiment_has_analyticaldata` (
  `idExperiment_has_AnalyticalData` int NOT NULL,
  `Experiment_idExperiment` int NOT NULL,
  `sample` varchar(100) DEFAULT NULL,
  `ADValue` float DEFAULT NULL,
  `chosen` int DEFAULT NULL,
  `AnalyticalData_idAnalyticalData` int NOT NULL,
  PRIMARY KEY (`idExperiment_has_AnalyticalData`,`Experiment_idExperiment`,`AnalyticalData_idAnalyticalData`),
  KEY `fk_Experiment_has_AnalyticalData_Experiment1_idx` (`Experiment_idExperiment`),
  KEY `fk_Experiment_has_AnalyticalData_AnalyticalData1_idx` (`AnalyticalData_idAnalyticalData`),
  CONSTRAINT `fk_Experiment_has_AnalyticalData_AnalyticalData1` FOREIGN KEY (`AnalyticalData_idAnalyticalData`) REFERENCES `analyticaldata` (`idAnalyticalData`),
  CONSTRAINT `fk_Experiment_has_AnalyticalData_Experiment1` FOREIGN KEY (`Experiment_idExperiment`) REFERENCES `experiment` (`idExperiment`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiment_has_analyticaldata`
--

LOCK TABLES `experiment_has_analyticaldata` WRITE;
/*!40000 ALTER TABLE `experiment_has_analyticaldata` DISABLE KEYS */;
INSERT INTO `experiment_has_analyticaldata` VALUES (44,11,'1',2050.1,1,2),(46,11,'1',24.1,1,4),(47,11,'1',275,1,5),(49,12,'1',67,1,2),(51,12,'1',NULL,1,4),(53,13,'1',NULL,1,2),(55,13,'1',NULL,1,4),(57,14,'1',NULL,1,2),(60,15,'1',NULL,1,2),(63,16,'1',NULL,1,2),(66,17,'1',NULL,1,2),(68,18,'1',NULL,1,2),(70,19,'1',NULL,1,2),(72,20,'1',NULL,1,2),(73,21,'1',NULL,1,1),(74,21,'1',NULL,1,2),(77,11,'1',17.31,1,7),(78,11,'1',1.28,1,6),(79,11,'1',7.09,1,8),(80,11,'1',8.79,1,9),(81,11,'1',55.9,1,11),(82,11,'1',97.3,1,10),(83,21,'1',347,1,5),(84,21,'1',22.97,1,7),(85,21,'1',NULL,1,10),(86,21,'1',NULL,1,9),(87,21,'1',2.26,1,6),(88,21,'1',NULL,1,8),(89,21,'1',NULL,1,11),(90,22,'1',NULL,1,2),(92,22,'1',135,1,5),(93,22,'1',0.93,1,6),(94,22,'1',26.07,1,7),(95,22,'1',NULL,1,8),(96,22,'1',NULL,1,9),(97,22,'1',NULL,1,10),(98,22,'1',NULL,1,11),(99,22,'1',NULL,1,4),(100,12,'1',97.4,1,9),(101,12,'1',9.63,1,10),(102,13,'1',96.5,1,9),(103,13,'1',4.15,1,10),(109,12,'1',270,1,5),(110,12,'1',NULL,1,11),(111,12,'1',NULL,1,8),(112,12,'1',1.32,1,6),(113,13,'1',16.83,1,7),(114,13,'1',166,1,5),(115,13,'1',NULL,1,11),(116,13,'1',NULL,1,8),(117,13,'1',0.74,1,6),(118,14,'1',NULL,1,4),(119,14,'1',NULL,1,10),(120,14,'1',22.23,1,7),(121,14,'1',192,1,5),(122,14,'1',NULL,1,11),(123,14,'1',NULL,1,8),(124,14,'1',NULL,1,9),(125,14,'1',1.07,1,6),(126,15,'1',NULL,1,4),(127,15,'1',NULL,1,10),(128,15,'1',17.82,1,7),(129,15,'1',151,1,5),(130,15,'1',NULL,1,11),(131,15,'1',NULL,1,8),(132,15,'1',NULL,1,9),(133,15,'1',0.07,1,6),(134,16,'1',NULL,1,4),(135,16,'1',NULL,1,10),(136,16,'1',19.06,1,7),(137,16,'1',360,1,5),(138,16,'1',NULL,1,11),(139,16,'1',NULL,1,8),(140,16,'1',NULL,1,9),(141,16,'1',1.8,1,6),(142,17,'1',NULL,1,4),(143,17,'1',NULL,1,10),(144,17,'1',22.05,1,7),(145,17,'1',143,1,5),(146,17,'1',NULL,1,11),(147,17,'1',NULL,1,8),(148,17,'1',NULL,1,9),(149,17,'1',0.79,1,6),(150,18,'1',NULL,1,4),(151,18,'1',NULL,1,10),(152,18,'1',26.14,1,7),(153,18,'1',237,1,5),(154,18,'1',NULL,1,11),(155,18,'1',NULL,1,8),(156,18,'1',NULL,1,9),(157,18,'1',1.43,1,6),(158,19,'1',NULL,1,4),(159,19,'1',NULL,1,10),(160,19,'1',20.48,1,7),(161,19,'1',261,1,5),(162,19,'1',NULL,1,11),(163,19,'1',NULL,1,8),(164,19,'1',NULL,1,9),(165,19,'1',1.5,1,6),(166,20,'1',NULL,1,4),(167,20,'1',NULL,1,10),(168,20,'1',25.63,1,7),(169,20,'1',323,1,5),(170,20,'1',NULL,1,11),(171,20,'1',NULL,1,8),(172,20,'1',NULL,1,9),(173,20,'1',2.25,1,6),(183,23,'1',275,1,5),(184,23,'1',17.31,1,7),(185,23,'1',7.09,1,8),(186,23,'1',8.79,1,9),(187,23,'1',1.28,1,6),(188,23,'1',2050.1,1,2),(189,23,'1',24.1,1,4),(190,23,'1',55.9,1,11),(191,23,'1',97.3,1,10);
/*!40000 ALTER TABLE `experiment_has_analyticaldata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experimentdate`
--

DROP TABLE IF EXISTS `experimentdate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experimentdate` (
  `idExperimentDate` int NOT NULL,
  `ExpDate` date DEFAULT NULL,
  `Comment_ed` text,
  `Experiment_idExperiment` int NOT NULL,
  `StageType_idStageType` int NOT NULL,
  PRIMARY KEY (`idExperimentDate`,`Experiment_idExperiment`,`StageType_idStageType`),
  KEY `fk_experimentDate_Experiment1_idx` (`Experiment_idExperiment`),
  KEY `fk_experimentdate_stagetype1_idx` (`StageType_idStageType`) /*!80000 INVISIBLE */,
  CONSTRAINT `fk_experimentDate_Experiment1` FOREIGN KEY (`Experiment_idExperiment`) REFERENCES `experiment` (`idExperiment`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experimentdate`
--

LOCK TABLES `experimentdate` WRITE;
/*!40000 ALTER TABLE `experimentdate` DISABLE KEYS */;
INSERT INTO `experimentdate` VALUES (24,'2023-06-12',NULL,11,13),(25,'2023-06-12','Скорость подачи раствора из шприцевого насоса \n1 мл/мин, объем шприца 10 мл.\nБыло получено 160 мл частиц аэрогеля.\n',11,6),(26,'2023-06-13','Была частично реализована многоступенчатая \nзамена растворителя (10%, 30%, 60%).',11,2),(27,'2023-06-14','Была проведена вторая часть процесса замены\nрастворителя (90%, 100%, 100%).\n',11,2),(28,'2023-06-15',NULL,11,9),(29,'2023-06-20',NULL,22,13),(30,'2023-06-20','Скорость подачи раствора из шприцевого насоса \n1 мл/мин, объем шприца 10 мл.\nБыло получено 160 мл частиц аэрогеля.\n',22,5),(31,'2023-06-24',NULL,12,13),(32,'2023-06-24',NULL,13,13),(33,'2023-06-24',NULL,14,13),(34,'2023-06-24',NULL,15,13),(35,'2023-06-24',NULL,16,13),(36,'2023-06-24',NULL,17,13),(37,'2023-06-24',NULL,18,13),(38,'2023-06-24',NULL,19,13),(39,'2023-06-24',NULL,20,13),(40,'2023-06-24',NULL,21,13),(41,'2023-06-25',NULL,23,13),(42,'2023-06-25','Скорость подачи раствора из шприцевого насоса\n1 мл/мин, объем шприца 10 мл.\nБыло получено 160 мл частиц аэрогеля.\n',23,5);
/*!40000 ALTER TABLE `experimentdate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experimentdate_has_parameters`
--

DROP TABLE IF EXISTS `experimentdate_has_parameters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experimentdate_has_parameters` (
  `idExperimentdate_has_Parameters` int NOT NULL,
  `value` float DEFAULT NULL,
  `experimentdate_idExperimentDate` int NOT NULL,
  `parameters_idParameters` int NOT NULL,
  `chosen` int DEFAULT NULL,
  PRIMARY KEY (`idExperimentdate_has_Parameters`,`experimentdate_idExperimentDate`,`parameters_idParameters`),
  KEY `fk_experimentdate_has_parameters_parameters1_idx` (`parameters_idParameters`),
  KEY `fk_experimentdate_has_parameters_experimentdate1_idx` (`experimentdate_idExperimentDate`),
  CONSTRAINT `fk_experimentdate_has_parameters_experimentdate1` FOREIGN KEY (`experimentdate_idExperimentDate`) REFERENCES `experimentdate` (`idExperimentDate`),
  CONSTRAINT `fk_experimentdate_has_parameters_parameters1` FOREIGN KEY (`parameters_idParameters`) REFERENCES `parameters` (`idParameters`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experimentdate_has_parameters`
--

LOCK TABLES `experimentdate_has_parameters` WRITE;
/*!40000 ALTER TABLE `experimentdate_has_parameters` DISABLE KEYS */;
/*!40000 ALTER TABLE `experimentdate_has_parameters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `level`
--

DROP TABLE IF EXISTS `level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `level` (
  `idLevel` int NOT NULL,
  `Lev_Type` varchar(100) DEFAULT NULL,
  `AvailableInfo` text,
  PRIMARY KEY (`idLevel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `level`
--

LOCK TABLES `level` WRITE;
/*!40000 ALTER TABLE `level` DISABLE KEYS */;
INSERT INTO `level` VALUES (1,'Уровень 1','Заполнение экспериментов, формирование отчетов, поиск информации'),(2,'Уровень 2','Редактирование информации о пользователях, научных работах, реагентах и оборудовании');
/*!40000 ALTER TABLE `level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `literature`
--

DROP TABLE IF EXISTS `literature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `literature` (
  `idLiterature` int NOT NULL,
  `LitName` varchar(500) DEFAULT NULL,
  `DOI` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`idLiterature`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `literature`
--

LOCK TABLES `literature` WRITE;
/*!40000 ALTER TABLE `literature` DISABLE KEYS */;
INSERT INTO `literature` VALUES (5,'Chitosan-Based Aerogel Particles as Highly Effective Local Hemostatic Agents. Production Process and In Vivo Evaluations','https://doi.org/10.3390/polym12092055'),(6,'Cellular Automata Modeling of Three-Dimensional Chitosan-Based Aerogels Fiberous Structures with Bezier Curves','https://doi.org/10.3390/polym13152511');
/*!40000 ALTER TABLE `literature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `idLocation` int NOT NULL,
  `Loc_Name` varchar(200) NOT NULL,
  PRIMARY KEY (`idLocation`),
  UNIQUE KEY `Loc_Name_UNIQUE` (`Loc_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'Лаб. 701'),(2,'Лаб. 702'),(3,'Лаб. 703'),(4,'Лаб. 704');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `methodology`
--

DROP TABLE IF EXISTS `methodology`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `methodology` (
  `idMethodology` int NOT NULL,
  `MetName` varchar(200) DEFAULT NULL,
  `Meth_text` longtext,
  `Experiment_idExperiment` int NOT NULL,
  PRIMARY KEY (`idMethodology`,`Experiment_idExperiment`),
  KEY `fk_Methodology_Experiment1_idx` (`Experiment_idExperiment`),
  CONSTRAINT `fk_Methodology_Experiment1` FOREIGN KEY (`Experiment_idExperiment`) REFERENCES `experiment` (`idExperiment`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `methodology`
--

LOCK TABLES `methodology` WRITE;
/*!40000 ALTER TABLE `methodology` DISABLE KEYS */;
INSERT INTO `methodology` VALUES (11,'Методика Образец 1','С(хит) = 1 масс%\nС(к-та) = 0.1 М\nС(щелочь) = 1 М\nC(полимер) = 0 масс%',11),(12,'Методика Образец 2','врррр',12),(13,'Методика Образец 3','врврвррвррв',13),(14,'Методика Образец 4','арааовопр',14),(15,'Методика Образец 5','врврврврв',15),(16,'Методика Образец 6','врвррврвр',16),(17,'Методика Образец 7','врррврврвр',17),(18,'Методика Образец 8','араара',18),(19,'Методика Образец 9','вррвврвр',19),(20,'Методика Образец 10','врврврр',20),(21,'Методика Образец 11','врврвврвр',21),(22,'Методика Образец 12','С(хит) = 2 масс%\nС(к-ты) = 0,2М\nС(щелочь) = 0,1М\nМногоступенчатая замена растворителя\n(10%, 30%, 60%, 90%, 100%, 100%)\nЗамена растворителя будет проходить в два дня.',22),(23,'Методика Образец 13','С(хит) = 2 масс%\nС(к-ты) = 0,2М\nС(щелочь) = 0,1М\nМногоступенчатая замена растворителя\n(10%, 30%, 60%, 90%, 100%, 100%)\nМногоступенчатая замена растворителя будет проводиться в два дня.',23);
/*!40000 ALTER TABLE `methodology` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `methodology_has_literature`
--

DROP TABLE IF EXISTS `methodology_has_literature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `methodology_has_literature` (
  `idMethodology_has_Literature` int NOT NULL,
  `Methodology_idMethodology` int NOT NULL,
  `Literature_idLiterature` int NOT NULL,
  PRIMARY KEY (`idMethodology_has_Literature`,`Methodology_idMethodology`,`Literature_idLiterature`),
  KEY `fk_Methodology_has_Literature_Literature1_idx` (`Literature_idLiterature`),
  KEY `fk_Methodology_has_Literature_Methodology1_idx` (`Methodology_idMethodology`),
  CONSTRAINT `fk_Methodology_has_Literature_Literature1` FOREIGN KEY (`Literature_idLiterature`) REFERENCES `literature` (`idLiterature`),
  CONSTRAINT `fk_Methodology_has_Literature_Methodology1` FOREIGN KEY (`Methodology_idMethodology`) REFERENCES `methodology` (`idMethodology`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `methodology_has_literature`
--

LOCK TABLES `methodology_has_literature` WRITE;
/*!40000 ALTER TABLE `methodology_has_literature` DISABLE KEYS */;
INSERT INTO `methodology_has_literature` VALUES (4,11,5),(6,12,5),(8,13,5),(10,14,5),(12,15,5),(14,16,5),(16,17,5),(18,18,5),(20,19,5),(22,20,5),(24,21,5),(26,22,5),(27,23,5),(5,11,6),(7,12,6),(9,13,6),(11,14,6),(13,15,6),(15,16,6),(17,17,6),(19,18,6),(21,19,6),(23,20,6),(25,21,6);
/*!40000 ALTER TABLE `methodology_has_literature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parameters`
--

DROP TABLE IF EXISTS `parameters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parameters` (
  `idParameters` int NOT NULL,
  `ParName` varchar(200) DEFAULT NULL,
  `ParSN` varchar(200) DEFAULT NULL,
  `ParUnits` varchar(200) DEFAULT NULL,
  `ParUnitsSN` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idParameters`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parameters`
--

LOCK TABLES `parameters` WRITE;
/*!40000 ALTER TABLE `parameters` DISABLE KEYS */;
INSERT INTO `parameters` VALUES (1,'Температура','T','Градус Цельсия','C'),(2,'Давление','P','Паскаль','Па');
/*!40000 ALTER TABLE `parameters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personnel`
--

DROP TABLE IF EXISTS `personnel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personnel` (
  `idPersonnel` int NOT NULL,
  `Pers_Name` varchar(200) NOT NULL,
  `Position` varchar(200) DEFAULT NULL,
  `Login` varchar(200) DEFAULT NULL,
  `Password` varchar(200) DEFAULT NULL,
  `Level_idLevel` int NOT NULL,
  PRIMARY KEY (`idPersonnel`,`Level_idLevel`),
  UNIQUE KEY `Pers_Name_UNIQUE` (`Pers_Name`),
  KEY `fk_Personnel_Level_idx` (`Level_idLevel`),
  CONSTRAINT `fk_Personnel_Level` FOREIGN KEY (`Level_idLevel`) REFERENCES `level` (`idLevel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personnel`
--

LOCK TABLES `personnel` WRITE;
/*!40000 ALTER TABLE `personnel` DISABLE KEYS */;
INSERT INTO `personnel` VALUES (1,'Мочалова М.',NULL,'mochalova82','mochalova82',2),(2,'Суслова Е. Н.',NULL,'suslova54','suslova54',2),(3,'Цыганков П. Ю.',NULL,'tsygankov43','tsygankov43',2),(4,'Уварова А. А.',NULL,'uvarova21','uvarova21',2),(5,'Комарова Д.',NULL,'komarova26','komarova26',1),(6,'Дёмкин К.',NULL,'demkin44','demkin44',2),(7,'Пилоян А.',NULL,'piloyan28','piloyan28',1),(8,'Платонов Д.',NULL,'platonov84','platonov84',1),(9,'Фаустова А.',NULL,'faust65','faust65',1),(10,'Корнеев Д.',NULL,'korneev45','korneev45',1),(11,'Березовская Е.',NULL,'berezovskaya32','berezovskaya32',1),(12,'Голубев Э.',NULL,'golubev65','golubev65',1),(13,'Агафонова А.',NULL,'agafonova31','agafonova31',1),(14,'Черевко С.',NULL,'cherevko49','cherevko49',1),(15,'Прописнова А.',NULL,'propisnova18','propisnova18',1),(16,'Лебедева М.',NULL,'lebedeva77','lebedeva77',1),(17,'Трофимова К.',NULL,'trofimova11','trofimova11',1),(18,'Васютина А.','Главный','god1000','god1000',2),(19,'Васютина А','Дурачок','ivan20','ivan20',1),(20,'Ловская Д. Д.',NULL,'lovskaya76','lovskaya76',2),(21,'Лебедев А. Е.',NULL,'lebedev12','lebedev12',2),(22,'Федотова О.',NULL,'fedotova87','fedotova87',2),(23,'Меньшутина Н. В.',NULL,'menshutina08','menshutina08',2),(24,'Кунаев Д.',NULL,'kunaev98','kunaev98',1),(25,'Гордионок И.',NULL,'gordionok29','gordionok29',1),(26,'Абрамов А.',NULL,'abramov45','abramov45',2),(27,'Нгуен З.',NULL,'nguen58','nguen58',1),(28,'Кислинская А.',NULL,'kislinskaya39','kislinskaya39',2);
/*!40000 ALTER TABLE `personnel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `physchemproperties`
--

DROP TABLE IF EXISTS `physchemproperties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `physchemproperties` (
  `idPhysChemProperties` int NOT NULL,
  `PropName` varchar(200) DEFAULT NULL,
  `PropSN` varchar(200) DEFAULT NULL,
  `PrUnits` varchar(200) DEFAULT NULL,
  `PrUnitSN` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idPhysChemProperties`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `physchemproperties`
--

LOCK TABLES `physchemproperties` WRITE;
/*!40000 ALTER TABLE `physchemproperties` DISABLE KEYS */;
INSERT INTO `physchemproperties` VALUES (1,'Концентрация','C',NULL,NULL),(2,'Чистота',NULL,NULL,NULL),(3,'ГОСТ/ТУ',NULL,NULL,NULL);
/*!40000 ALTER TABLE `physchemproperties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `processstage`
--

DROP TABLE IF EXISTS `processstage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `processstage` (
  `idProcessStage` int NOT NULL,
  `PSName` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idProcessStage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `processstage`
--

LOCK TABLES `processstage` WRITE;
/*!40000 ALTER TABLE `processstage` DISABLE KEYS */;
INSERT INTO `processstage` VALUES (1,'Получение раствора'),(2,'Гелеобразование'),(3,'Замена растворителя'),(4,'Сушка'),(5,'Адсорбция');
/*!40000 ALTER TABLE `processstage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reagent`
--

DROP TABLE IF EXISTS `reagent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reagent` (
  `idReagent` int NOT NULL,
  `CatNumber` varchar(200) DEFAULT NULL,
  `DateReceived` date DEFAULT NULL,
  `EndDateReag` date DEFAULT NULL,
  `Amount` float DEFAULT NULL,
  `MinAmount` float DEFAULT NULL,
  `InStock` int DEFAULT NULL,
  `Units_idUnits` int NOT NULL,
  `ReagType_idReagType` int NOT NULL,
  `Location_idLocation` int NOT NULL,
  `ReagInfo_idReagInfo` int NOT NULL,
  PRIMARY KEY (`idReagent`,`Units_idUnits`,`ReagType_idReagType`,`Location_idLocation`,`ReagInfo_idReagInfo`),
  KEY `fk_Reagent_Location1_idx` (`Location_idLocation`),
  KEY `fk_reagent_ReagType1_idx` (`ReagType_idReagType`),
  KEY `fk_reagent_Units1_idx` (`Units_idUnits`),
  KEY `fk_reagent_reaginfo1_idx` (`ReagInfo_idReagInfo`),
  CONSTRAINT `fk_Reagent_Location1` FOREIGN KEY (`Location_idLocation`) REFERENCES `location` (`idLocation`),
  CONSTRAINT `fk_reagent_ReagType1` FOREIGN KEY (`ReagType_idReagType`) REFERENCES `reagtype` (`idReagType`),
  CONSTRAINT `fk_reagent_Units1` FOREIGN KEY (`Units_idUnits`) REFERENCES `units` (`idUnits`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reagent`
--

LOCK TABLES `reagent` WRITE;
/*!40000 ALTER TABLE `reagent` DISABLE KEYS */;
INSERT INTO `reagent` VALUES (1,'Хитозан','2022-09-08','2024-09-08',160,20,1,1,1,1,1),(2,'Белок молочный','2022-07-08','2024-07-08',1000,100,1,1,1,2,2),(3,'Белок яичный','2022-02-03','2024-02-03',1500,100,1,1,1,4,3),(4,'Альгинат натрия','2022-07-07','2024-07-07',1000,100,1,1,1,1,4),(5,'Тетраэтоксисилан','2022-05-03','2025-05-03',1000,100,1,3,1,3,5),(7,'Уксусная кислота','2022-04-05','2025-04-05',5000,500,1,3,2,3,7),(8,'Гидроксид натрия','2022-06-02','2024-06-02',5000,500,1,1,2,2,8),(9,'Изопропиловый спирт','2022-04-03','2024-04-03',100000,5000,1,3,3,4,9),(10,'Аммиак','2022-05-05','2024-05-05',2500,200,1,3,2,3,10),(11,'Соляная кислота','2022-03-09','2024-03-09',200,100,1,3,2,1,11),(12,'Хлорид кальция','2022-01-08','2023-07-08',1000,100,1,1,2,2,12),(13,'Этиловый спирт','2022-05-09','2024-05-09',5,1,1,2,3,3,13),(14,'Ацетон','2022-01-02','2023-07-22',2,1,0,2,3,2,14),(15,'Гексан','2000-01-01','2023-07-16',1.5,1,1,2,3,1,15),(16,'Ацетонитрил','2000-01-01','2023-06-27',400,100,1,3,2,2,16),(17,'ДМСО','2000-01-01','2025-04-04',300,100,1,3,2,3,17),(18,'Крахмал рисовый','2000-01-01','2023-07-29',600,100,1,1,1,1,18),(19,'Желатин','2000-01-01','2024-11-01',400,50,1,1,1,2,19),(20,'Коллаген','2000-01-01','2023-07-04',2000,100,1,1,1,3,20),(21,'Лидокаин','2000-01-01','2025-06-01',200,50,1,1,4,3,21),(22,'Гиалуроновая кислота','2000-01-01','2029-03-03',35,5,1,1,1,1,22),(23,'Крахмал кукурузный','2022-02-04','2027-03-04',1000,100,1,1,1,1,23);
/*!40000 ALTER TABLE `reagent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reagent_has_physchemproperties`
--

DROP TABLE IF EXISTS `reagent_has_physchemproperties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reagent_has_physchemproperties` (
  `idreagent_has_PhysChemProperties` int NOT NULL,
  `reagent_idReagent` int NOT NULL,
  `PhysChemProperties_idPhysChemProperties` int NOT NULL,
  `value` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idreagent_has_PhysChemProperties`,`reagent_idReagent`,`PhysChemProperties_idPhysChemProperties`),
  KEY `fk_reagent_has_PhysChemProperties_PhysChemProperties1_idx` (`PhysChemProperties_idPhysChemProperties`),
  KEY `fk_reagent_has_PhysChemProperties_reagent1_idx` (`reagent_idReagent`),
  CONSTRAINT `fk_reagent_has_PhysChemProperties_PhysChemProperties1` FOREIGN KEY (`PhysChemProperties_idPhysChemProperties`) REFERENCES `physchemproperties` (`idPhysChemProperties`),
  CONSTRAINT `fk_reagent_has_PhysChemProperties_reagent1` FOREIGN KEY (`reagent_idReagent`) REFERENCES `reagent` (`idReagent`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reagent_has_physchemproperties`
--

LOCK TABLES `reagent_has_physchemproperties` WRITE;
/*!40000 ALTER TABLE `reagent_has_physchemproperties` DISABLE KEYS */;
/*!40000 ALTER TABLE `reagent_has_physchemproperties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reaginfo`
--

DROP TABLE IF EXISTS `reaginfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reaginfo` (
  `idReagInfo` int NOT NULL,
  `ReagName1` varchar(200) DEFAULT NULL,
  `ReagName2` varchar(200) DEFAULT NULL,
  `ReagName3` varchar(200) DEFAULT NULL,
  `ReagNameENG` varchar(200) DEFAULT NULL,
  `ReagFormula` varchar(200) DEFAULT NULL,
  `CodeReag` varchar(200) DEFAULT NULL,
  `SerialNumber` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idReagInfo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reaginfo`
--

LOCK TABLES `reaginfo` WRITE;
/*!40000 ALTER TABLE `reaginfo` DISABLE KEYS */;
INSERT INTO `reaginfo` VALUES (1,'Хитозан','-','-','-','-','-','-'),(2,'Белок молочный',NULL,NULL,NULL,NULL,NULL,NULL),(3,'Белок яичный',NULL,NULL,NULL,NULL,NULL,NULL),(4,'Альгинат натрия',NULL,NULL,NULL,NULL,NULL,NULL),(5,'Тетраэтоксисилан',NULL,NULL,NULL,NULL,NULL,NULL),(6,'Дистиллированная вода',NULL,NULL,NULL,NULL,NULL,NULL),(7,'Уксусная кислота',NULL,NULL,NULL,NULL,NULL,NULL),(8,'Гидроксид натрия',NULL,NULL,NULL,NULL,NULL,NULL),(9,'Изопропиловый спирт',NULL,NULL,NULL,NULL,NULL,NULL),(10,'Аммиак',NULL,NULL,NULL,NULL,NULL,NULL),(11,'Соляная кислота',NULL,NULL,NULL,NULL,NULL,NULL),(12,'Хлорид кальция',NULL,NULL,NULL,NULL,NULL,NULL),(13,'Этиловый спирт',NULL,NULL,NULL,NULL,NULL,NULL),(14,'Ацетон',NULL,NULL,NULL,NULL,NULL,NULL),(15,'Гексан',NULL,NULL,NULL,NULL,NULL,NULL),(16,'Ацетонитрил',NULL,NULL,NULL,NULL,NULL,NULL),(17,'ДМСО',NULL,NULL,NULL,NULL,NULL,NULL),(18,'Крахмал рисовый',NULL,NULL,NULL,NULL,NULL,NULL),(19,'Желатин',NULL,NULL,NULL,NULL,NULL,NULL),(20,'Коллаген',NULL,NULL,NULL,NULL,NULL,NULL),(21,'Лидокаин',NULL,NULL,NULL,NULL,NULL,NULL),(22,'Гиалуроновая кислота',NULL,NULL,NULL,NULL,NULL,NULL),(23,'Крахмал кукурузный',NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `reaginfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reagtype`
--

DROP TABLE IF EXISTS `reagtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reagtype` (
  `idReagType` int NOT NULL,
  `RTypeName` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idReagType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reagtype`
--

LOCK TABLES `reagtype` WRITE;
/*!40000 ALTER TABLE `reagtype` DISABLE KEYS */;
INSERT INTO `reagtype` VALUES (1,'Исходное вещество'),(2,'Вспомогательное вещество'),(3,'Растворитель'),(4,'АФИ');
/*!40000 ALTER TABLE `reagtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reagusage`
--

DROP TABLE IF EXISTS `reagusage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reagusage` (
  `idReagUsage` int NOT NULL,
  `AmUsed` float DEFAULT NULL,
  `Reagent_idReagent` int NOT NULL,
  `ExperimentDate_idExperimentDate` int NOT NULL,
  PRIMARY KEY (`idReagUsage`,`Reagent_idReagent`,`ExperimentDate_idExperimentDate`),
  KEY `fk_ReagUsage_Reagent1_idx` (`Reagent_idReagent`),
  KEY `fk_reagusage_experimentDate1_idx` (`ExperimentDate_idExperimentDate`),
  CONSTRAINT `fk_ReagUsage_Reagent1` FOREIGN KEY (`Reagent_idReagent`) REFERENCES `reagent` (`idReagent`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reagusage`
--

LOCK TABLES `reagusage` WRITE;
/*!40000 ALTER TABLE `reagusage` DISABLE KEYS */;
INSERT INTO `reagusage` VALUES (38,1,1,24),(39,0.6,7,24),(40,16,8,25),(41,64,9,26),(42,192,9,26),(43,384,9,26),(44,576,9,27),(45,640,9,27),(46,640,9,27),(47,10,9,28),(48,2,1,29),(49,1.2,7,29),(50,1.6,8,30),(51,1,1,31),(52,2,1,32),(53,2,1,33),(54,1,1,34),(55,1,1,35),(56,2,1,36),(57,2,1,37),(58,1,1,38),(59,1,1,39),(60,2,1,40),(61,2,1,41),(62,1.2,7,41),(63,1.6,8,42);
/*!40000 ALTER TABLE `reagusage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `researchproject`
--

DROP TABLE IF EXISTS `researchproject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `researchproject` (
  `idResearchProject` int NOT NULL,
  `RPName` varchar(300) DEFAULT NULL,
  `Secrecy` int DEFAULT NULL,
  PRIMARY KEY (`idResearchProject`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `researchproject`
--

LOCK TABLES `researchproject` WRITE;
/*!40000 ALTER TABLE `researchproject` DISABLE KEYS */;
INSERT INTO `researchproject` VALUES (1,'Исследование процессов получения частиц хитозановых аэрогелей',0),(2,'Земля за 6 дней',1),(3,'Печка на своем ходу',1),(4,'Украсть царевну',1),(5,'Внедрение гидрохлорида лидокаина в структуру хитозановых аэрогелей',0),(6,'Получение функциональных аэрогелей из оксидов металлов и неметаллов',0),(7,'Исследование методов получения нанопористых материалов для теплоизоляции',0),(8,'Сверхкритическая адсорбция',0),(9,'Исследование процессов получения аэрогелей на основе целлюлозы с использованием различных методов гелеобразования',0),(10,'Экспериментальное исследование процесса получения аэрогелей на основе диоксида кремния с люминофорами',0),(11,'Гибридные материалы на основе хитозана и целлюлозы, их получение и применение',0),(12,'Исследование процессов получения аэрогелей на основе оксидов металлов',0),(13,'Исследование процессов под давлением при получении нанопористых материалов на основе альгината натрия',0),(14,'Процессы получения гетерофазной системы на основе желатина для реализации 3D-печати вязкими материалами',0),(15,'Исследование процесса получения частиц белковых аэрогелей',0),(16,'Исследование процессов получения гибридных аэрогелей на основе оксидов кремния и железа',0),(17,'Исследование процесса получения микрочастиц хитозановых аэроегелей nn',0);
/*!40000 ALTER TABLE `researchproject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `researchproject_has_personnel`
--

DROP TABLE IF EXISTS `researchproject_has_personnel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `researchproject_has_personnel` (
  `idResearchProject_has_Personnel` int NOT NULL,
  `status_rp_idstatus_rp` int NOT NULL,
  `researchproject_idResearchProject` int NOT NULL,
  `personnel_idPersonnel` int NOT NULL,
  PRIMARY KEY (`idResearchProject_has_Personnel`,`status_rp_idstatus_rp`,`researchproject_idResearchProject`,`personnel_idPersonnel`),
  KEY `fk_researchproject_has_personnel_personnel1_idx` (`personnel_idPersonnel`),
  KEY `fk_researchproject_has_personnel_researchproject1_idx` (`researchproject_idResearchProject`),
  KEY `fk_researchproject_has_personnel_status_rp1_idx` (`status_rp_idstatus_rp`),
  CONSTRAINT `fk_researchproject_has_personnel_personnel1` FOREIGN KEY (`personnel_idPersonnel`) REFERENCES `personnel` (`idPersonnel`),
  CONSTRAINT `fk_researchproject_has_personnel_researchproject1` FOREIGN KEY (`researchproject_idResearchProject`) REFERENCES `researchproject` (`idResearchProject`),
  CONSTRAINT `fk_researchproject_has_personnel_status_rp1` FOREIGN KEY (`status_rp_idstatus_rp`) REFERENCES `status_rp` (`idstatus_rp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `researchproject_has_personnel`
--

LOCK TABLES `researchproject_has_personnel` WRITE;
/*!40000 ALTER TABLE `researchproject_has_personnel` DISABLE KEYS */;
INSERT INTO `researchproject_has_personnel` VALUES (1,1,1,1),(6,2,5,1),(38,1,17,1),(9,2,6,2),(12,2,7,2),(22,2,10,2),(30,2,13,2),(18,2,9,3),(15,2,8,4),(25,2,11,4),(5,1,5,5),(32,1,14,7),(36,1,16,8),(27,1,12,9),(8,1,6,10),(11,1,7,12),(14,1,8,13),(24,1,11,14),(34,1,15,16),(17,1,9,17),(2,1,2,18),(3,1,3,19),(4,1,4,19),(7,3,5,20),(10,3,6,21),(13,3,7,21),(23,3,10,21),(28,3,12,21),(31,3,13,21),(37,3,16,21),(20,2,9,22),(16,3,8,23),(19,3,9,23),(26,3,11,23),(35,3,15,23),(21,1,10,24),(29,1,13,25),(33,3,14,26);
/*!40000 ALTER TABLE `researchproject_has_personnel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stagetype`
--

DROP TABLE IF EXISTS `stagetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stagetype` (
  `idStageType` int NOT NULL,
  `STName` varchar(200) DEFAULT NULL,
  `Variant` varchar(200) DEFAULT NULL,
  `ProcessStage_idProcessStage` int NOT NULL,
  PRIMARY KEY (`idStageType`,`ProcessStage_idProcessStage`),
  KEY `fk_StageType_ProcessStage1_idx` (`ProcessStage_idProcessStage`),
  CONSTRAINT `fk_StageType_ProcessStage1` FOREIGN KEY (`ProcessStage_idProcessStage`) REFERENCES `processstage` (`idProcessStage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stagetype`
--

LOCK TABLES `stagetype` WRITE;
/*!40000 ALTER TABLE `stagetype` DISABLE KEYS */;
INSERT INTO `stagetype` VALUES (1,'Одноэтапная','-',3),(2,'Многоступенчатая','-',3),(4,'Монолиты','-',2),(5,'Микрочастицы','-',2),(6,'Частицы','-',2),(7,'Лиофильная','-',4),(8,'Термическая','-',4),(9,'Сверхкритическая','-',4),(10,'Пленки','-',2),(11,'-','-',5),(12,'Золь','-',1),(13,'Раствор','-',1);
/*!40000 ALTER TABLE `stagetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status_rp`
--

DROP TABLE IF EXISTS `status_rp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status_rp` (
  `idstatus_rp` int NOT NULL,
  `Status_Name` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idstatus_rp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status_rp`
--

LOCK TABLES `status_rp` WRITE;
/*!40000 ALTER TABLE `status_rp` DISABLE KEYS */;
INSERT INTO `status_rp` VALUES (1,'Исполнитель'),(2,'Куратор'),(3,'Научный руководитель');
/*!40000 ALTER TABLE `status_rp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stockstatus`
--

DROP TABLE IF EXISTS `stockstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stockstatus` (
  `idStockStatus` int NOT NULL,
  `StatName` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idStockStatus`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stockstatus`
--

LOCK TABLES `stockstatus` WRITE;
/*!40000 ALTER TABLE `stockstatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `stockstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `units`
--

DROP TABLE IF EXISTS `units`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `units` (
  `idUnits` int NOT NULL,
  `UName` varchar(200) DEFAULT NULL,
  `UUnitSN` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idUnits`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `units`
--

LOCK TABLES `units` WRITE;
/*!40000 ALTER TABLE `units` DISABLE KEYS */;
INSERT INTO `units` VALUES (1,'Граммы','г'),(2,'Литры','л'),(3,'Миллилитры','мл'),(4,'Пять литров','5л'),(5,'Количество штук','шт'),(6,'Килограмм','кг'),(7,'Неопр','');
/*!40000 ALTER TABLE `units` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'mydb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-27  9:04:17
