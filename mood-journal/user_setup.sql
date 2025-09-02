-- user_setup.sql
-- Run this file once as root in MySQL:  mysql -u root -p < user_setup.sql

-- 1. Create the database
CREATE DATABASE IF NOT EXISTS mood_journal CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 2. Create dedicated user (change password if you like)
CREATE USER IF NOT EXISTS 'mooduser'@'localhost' IDENTIFIED BY 'moodpass123';

-- 3. Grant privileges
GRANT ALL PRIVILEGES ON mood_journal.* TO 'mooduser'@'localhost';
FLUSH PRIVILEGES;

-- 4. Create the entries table
USE mood_journal;
CREATE TABLE IF NOT EXISTS entries (
  id INT AUTO_INCREMENT PRIMARY KEY,
  content TEXT NOT NULL,
  emotions JSON NOT NULL,
  top_label VARCHAR(50) NOT NULL,
  top_score DECIMAL(5,4) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;
