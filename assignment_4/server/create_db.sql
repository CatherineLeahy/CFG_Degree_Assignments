-- Create database
CREATE DATABASE IF NOT EXISTS corrosion_lab_equipment;
USE corrosion_lab_equipment;

DROP TABLE IF EXISTS chamber_specification;

-- Create chamber_specification table
CREATE TABLE IF NOT EXISTS chamber_specification (
	chamber_id VARCHAR(25) NOT NULL UNIQUE, -- each chamber is a different colour
    capacity INTEGER NOT NULL, -- maximum number of samples
    environment VARCHAR(7) NOT NULL, -- can accommodate neutral or acidic
    calibration_due_date DATE NOT NULL, -- will calibration date interfere with experiment?
    PRIMARY KEY (chamber_info_id) );

-- Create chamber_schedule table


INSERT INTO chamber_specification
(chamber_info_id,capacity, environment, calibration_due_date)
VALUES 
('Red', 75, 'acidic', '2024-08-25'),
('Green', 75, 'neutral', '2024-12-10'),
('Blue', 25, 'neutral', '2024-12-10'),
('Yellow', 50, 'acidic', '2025-06-21');

SELECT * FROM chamber_specification;

