-- MySQL dump 10.13  Distrib 8.0.37, for Win64 (x86_64)
--
-- Host: localhost    Database: store
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock` (
  `Item_No` int NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `Price` int DEFAULT NULL,
  PRIMARY KEY (`Item_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock`
--

LOCK TABLES `stock` WRITE;
/*!40000 ALTER TABLE `stock` DISABLE KEYS */;
INSERT INTO `stock` VALUES (1,'Apples (1 kg)',50,120),(2,'Bananas (1 dozen)',50,50),(3,'Spinach (1 bunch)',50,30),(4,'Whole Wheat Bread (1 loaf)',50,40),(5,'Chocolate Cake (500g)',50,250),(6,'Milk (1 litre)',50,50),(7,'Cheddar Cheese (200g)',50,180),(8,'Orange Juice (1 litre)',50,90),(9,'Mineral Water (1 litre)',50,20),(10,'Potato Chips (100g)',50,30),(11,'Dark Chocolate Bar (100g)',50,100),(12,'Laundry Detergent (1 kg)',50,200),(13,'Dishwashing Liquid (500ml)',50,150),(14,'Shampoo (200ml)',50,120),(15,'Toothpaste (100g)',50,60),(16,'Chicken Breast (1 kg)',50,220),(17,'Fresh Salmon Fillet (500g)',50,450),(18,'Shrimp (500g)',50,350),(19,'Mixed Vegetables (500g)',50,100),(20,'Ice Cream (1 tub)',50,150),(21,'Chicken Nuggets (300g)',50,200),(22,'Olive Oil (500ml)',50,350),(23,'Pasta (500g)',50,80),(24,'Canned Tomatoes (400g)',50,60),(25,'Cornflakes (500g)',50,150),(26,'Oatmeal (500g)',50,120),(27,'Pancake Mix (250g)',50,90),(28,'Tomato Ketchup (500g)',50,120),(29,'Mixed Herbs (50g)',50,60),(30,'Chili Powder (100g)',50,40),(31,'Multivitamin Tablets (60 count)',50,500),(32,'Protein Powder (1 kg)',50,3000),(33,'Green Tea Bags (25 count)',50,150);
/*!40000 ALTER TABLE `stock` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-05 20:46:47
