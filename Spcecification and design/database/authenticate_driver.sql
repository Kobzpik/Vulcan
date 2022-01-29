-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 29, 2022 at 03:53 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alpha`
--

-- --------------------------------------------------------

--
-- Table structure for table `authenticate_driver`
--

CREATE TABLE `authenticate_driver` (
  `user_id` int(11) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `driver_license_No` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `authenticate_driver`
--

INSERT INTO `authenticate_driver` (`user_id`, `phone_number`, `driver_license_No`) VALUES
(1, '322222222222', '123456a'),
(3, '124567', '123456a');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authenticate_driver`
--
ALTER TABLE `authenticate_driver`
  ADD PRIMARY KEY (`user_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `authenticate_driver`
--
ALTER TABLE `authenticate_driver`
  ADD CONSTRAINT `authenticate_customer_user_id_0ae7f891_fk_authenticate_user_id` FOREIGN KEY (`user_id`) REFERENCES `authenticate_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
