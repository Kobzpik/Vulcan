-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 29, 2022 at 03:54 PM
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
-- Table structure for table `authenticate_user`
--

CREATE TABLE `authenticate_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_driver` tinyint(1) NOT NULL,
  `is_officer` tinyint(1) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `authenticate_user`
--

INSERT INTO `authenticate_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `email`, `is_staff`, `is_active`, `date_joined`, `is_driver`, `is_officer`, `first_name`, `last_name`) VALUES
(1, 'pbkdf2_sha256$216000$unrClJfvLBfo$aG3kRvW9CNkPVoQZvhkIsOgibdkbRjdr7Xtpz6NmnQk=', '2022-01-29 14:30:36.774187', 0, 'driver1', '', 0, 1, '2022-01-29 13:30:37.931704', 1, 0, 'driv', 'ver1'),
(2, 'pbkdf2_sha256$216000$fc4OszteP9CC$XOFWoxivw12S/vvEHQaMJ3I56Y4EefpByI62qMe9qtw=', '2022-01-29 14:27:35.427999', 0, 'kobz', '', 1, 1, '2022-01-26 07:02:48.870441', 1, 1, 'prabath', 'indrajith'),
(3, 'pbkdf2_sha256$216000$X5Jo3Lpvy3Kd$k5JHsHg6O87jhzcgMBmG71vyJgkBEf0stLJlEn/yfdY=', '2022-01-29 14:33:39.145833', 0, 'driver2', '', 0, 1, '2022-01-29 14:29:20.795087', 1, 0, 'dri', 'ver2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authenticate_user`
--
ALTER TABLE `authenticate_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `authenticate_user`
--
ALTER TABLE `authenticate_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
