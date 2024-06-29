-- Create database
CREATE DATABASE IF NOT EXISTS lab;
USE lab;

DROP TABLE IF EXISTS chamber_info;

-- Create growing_plots table
CREATE TABLE IF NOT EXISTS chamber_info (
	chamber_info_id VARCHAR(32) NOT NULL UNIQUE,
    capacity INTEGER NOT NULL,
    PRIMARY KEY (chamber_info_id) );
    
INSERT INTO chamber_info 
(chamber_info_id,capacity)
VALUES 
('Red', 75),
('Yellow', 50);

SELECT * FROM chamber_info;