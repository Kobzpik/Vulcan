-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 01, 2022 at 06:50 PM
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
-- Table structure for table `officer_fine`
--

CREATE TABLE `officer_fine` (
  `id` int(11) NOT NULL,
  `vehicle_No` varchar(50) NOT NULL,
  `driver_license_No` varchar(124) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `Police_station` varchar(130) NOT NULL,
  `Issuing_officer_Name` varchar(20) NOT NULL,
  `Nature_of_Offence_id` int(11) DEFAULT NULL,
  `district_id` int(11) DEFAULT NULL,
  `driver_id` int(11) DEFAULT NULL,
  `location_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `officer_fine`
--

INSERT INTO `officer_fine` (`id`, `vehicle_No`, `driver_license_No`, `date`, `time`, `Police_station`, `Issuing_officer_Name`, `Nature_of_Offence_id`, `district_id`, `driver_id`, `location_id`) VALUES
(1, 'hh-6758', '123456a', '2022-03-20', '19:21:53.000000', 'Gampola', 'officer', 1, 1, 1, 1),
(2, 'hh-6755', '123456a3', '2022-03-20', '19:35:49.000000', 'Colombo', 'officer', 2, 2, 3, 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `officer_fine`
--
ALTER TABLE `officer_fine`
  ADD PRIMARY KEY (`id`),
  ADD KEY `officer_fine_Nature_of_Offence_id_c73be1a4_fk_officer_offence_id` (`Nature_of_Offence_id`),
  ADD KEY `officer_fine_district_id_a78a5ea8_fk_officer_district_id` (`district_id`),
  ADD KEY `officer_fine_driver_id_8142cf3f_fk_authenticate_user_id` (`driver_id`),
  ADD KEY `officer_fine_location_id_2c4c23d8_fk_officer_location_id` (`location_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `officer_fine`
--
ALTER TABLE `officer_fine`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `officer_fine`
--
ALTER TABLE `officer_fine`
  ADD CONSTRAINT `officer_fine_Nature_of_Offence_id_c73be1a4_fk_officer_offence_id` FOREIGN KEY (`Nature_of_Offence_id`) REFERENCES `officer_offence` (`id`),
  ADD CONSTRAINT `officer_fine_district_id_a78a5ea8_fk_officer_district_id` FOREIGN KEY (`district_id`) REFERENCES `officer_district` (`id`),
  ADD CONSTRAINT `officer_fine_driver_id_8142cf3f_fk_authenticate_user_id` FOREIGN KEY (`driver_id`) REFERENCES `authenticate_user` (`id`),
  ADD CONSTRAINT `officer_fine_location_id_2c4c23d8_fk_officer_location_id` FOREIGN KEY (`location_id`) REFERENCES `officer_location` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
