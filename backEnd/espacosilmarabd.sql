CREATE DATABASE  IF NOT EXISTS `espacosilmarabd` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `espacosilmarabd`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: espacosilmarabd
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
-- Table structure for table `agendamentos`
--

DROP TABLE IF EXISTS `agendamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agendamentos` (
  `id_agendamento` int NOT NULL AUTO_INCREMENT,
  `id_servico` int DEFAULT NULL,
  `id_usuario` int DEFAULT NULL,
  `formato` varchar(15) DEFAULT NULL,
  `estado` varchar(20) DEFAULT NULL,
  `data_hora` datetime DEFAULT NULL,
  `observacoes` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id_agendamento`),
  KEY `id_servico` (`id_servico`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `agendamentos_ibfk_1` FOREIGN KEY (`id_servico`) REFERENCES `servicos` (`id_servico`),
  CONSTRAINT `agendamentos_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agendamentos`
--

LOCK TABLES `agendamentos` WRITE;
/*!40000 ALTER TABLE `agendamentos` DISABLE KEYS */;
/*!40000 ALTER TABLE `agendamentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicos`
--

DROP TABLE IF EXISTS `servicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicos` (
  `id_servico` int NOT NULL AUTO_INCREMENT,
  `nome_servico` varchar(50) NOT NULL,
  `descricao` varchar(150) DEFAULT NULL,
  `valor` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_servico`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicos`
--

LOCK TABLES `servicos` WRITE;
/*!40000 ALTER TABLE `servicos` DISABLE KEYS */;
INSERT INTO `servicos` VALUES (1,'Atendimento psicanalítico','Marque uma sessão de psicanálise e cuide de sua saúde mental!',100.00),(2,'Consultoria contábil/financeira','Receba orientações relacionadas a contabilidade e finanças de uma profissional experiente na área',70.00),(3,'Treinamento','Adquiria conhecimento e melhore suas habilidades profissionais',70.00),(4,'Análise comportamental','Melhore sua comunicação com as pessoas ao seu redor e alcanece melhor produtividade de maneira eficiente',70.00),(5,'Inteligência emocional','Aprimore seu autoconhecimento e defina com segurança seus sentimentos para melhorar sua vida profissional e pessoal',70.00),(6,'Terapia Cognitiva Comportamental','Marque já um atendimento e busque entender sua realidade para compreender seus sentimentos e atitudes',100.00);
/*!40000 ALTER TABLE `servicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `email` varchar(30) NOT NULL,
  `senha` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-05 11:14:37