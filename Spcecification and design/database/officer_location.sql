-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 26, 2022 at 01:25 PM
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
-- Table structure for table `officer_location`
--

CREATE TABLE `officer_location` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `district_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `officer_location`
--

INSERT INTO `officer_location` (`id`, `name`, `district_id`) VALUES
(1, 'Location1', 1),
(2, 'Location2', 1),
(3, 'Location3', 1),
(4, 'Location1', 2),
(5, 'Location2', 2),
(6, 'Location3', 2),
(7, 'Location1', 3),
(8, 'Location2', 3),
(9, 'Location3', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `officer_location`
--
ALTER TABLE `officer_location`
  ADD PRIMARY KEY (`id`),
  ADD KEY `officer_location_district_id_bcc98907_fk_officer_district_id` (`district_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `officer_location`
--
ALTER TABLE `officer_location`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `officer_location`
--
ALTER TABLE `officer_location`
  ADD CONSTRAINT `officer_location_district_id_bcc98907_fk_officer_district_id` FOREIGN KEY (`district_id`) REFERENCES `officer_district` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
