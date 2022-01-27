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
-- Table structure for table `officer_offence`
--

CREATE TABLE `officer_offence` (
  `id` int(11) NOT NULL,
  `offence` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `officer_offence`
--

INSERT INTO `officer_offence` (`id`, `offence`) VALUES
(1, 'offence1'),
(2, 'offence2'),
(3, 'offence3'),
(4, 'offence4'),
(5, 'offence5');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `officer_offence`
--
ALTER TABLE `officer_offence`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `officer_offence`
--
ALTER TABLE `officer_offence`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
