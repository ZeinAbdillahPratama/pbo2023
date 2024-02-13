-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 13, 2024 at 03:22 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbsewakomik`
--

-- --------------------------------------------------------

--
-- Table structure for table `kembalikankomik`
--

CREATE TABLE `kembalikankomik` (
  `Id` int(11) NOT NULL,
  `Nama_Konsumen` varchar(100) DEFAULT NULL,
  `Judul_Komik` varchar(100) DEFAULT NULL,
  `Jumlah_Komik` int(11) DEFAULT NULL,
  `Tanggal_Dikembalikan` date DEFAULT NULL,
  `Tarif_PerHari` int(11) DEFAULT NULL,
  `Total_Bayar` int(11) DEFAULT NULL,
  `Status_Bayar` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `sewakomik`
--

CREATE TABLE `sewakomik` (
  `Id` int(11) NOT NULL,
  `Nama_Konsumen` varchar(100) DEFAULT NULL,
  `Judul_Komik` varchar(100) DEFAULT NULL,
  `Jumlah_Komik` int(11) DEFAULT NULL,
  `Tanggal_Disewakan` date DEFAULT NULL,
  `Tarif_PerHari` int(11) DEFAULT NULL,
  `Total_Bayar` int(11) DEFAULT NULL,
  `Status_Bayar` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sewakomik`
--

INSERT INTO `sewakomik` (`Id`, `Nama_Konsumen`, `Judul_Komik`, `Jumlah_Komik`, `Tanggal_Disewakan`, `Tarif_PerHari`, `Total_Bayar`, `Status_Bayar`) VALUES
(1, 'zein', 'naruto', 2, '2024-02-13', 1000, 2000, 'lunas');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kembalikankomik`
--
ALTER TABLE `kembalikankomik`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `Nama_Konsumen` (`Nama_Konsumen`);

--
-- Indexes for table `sewakomik`
--
ALTER TABLE `sewakomik`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `Nama_Konsumen` (`Nama_Konsumen`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kembalikankomik`
--
ALTER TABLE `kembalikankomik`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sewakomik`
--
ALTER TABLE `sewakomik`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
