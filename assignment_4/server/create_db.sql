-- Create database
CREATE DATABASE IF NOT EXISTS corrosion_lab_equipment;
USE corrosion_lab_equipment;

DROP TABLE IF EXISTS chamber_schedule;
DROP TABLE IF EXISTS chamber_specification;

-- Create chamber_specification table
CREATE TABLE IF NOT EXISTS chamber_specification (
	chamber_id VARCHAR(25) NOT NULL UNIQUE, -- each chamber is a different colour so ID by colour
    capacity INTEGER NOT NULL, -- maximum number of samples
    environment VARCHAR(7) NOT NULL, -- can accommodate neutral or acidic
    calibration_due_date DATE NOT NULL, -- will calibration date interfere with experiment?
    PRIMARY KEY (chamber_id) );

-- Create chamber_schedule table
CREATE TABLE IF NOT EXISTS chamber_schedule (
    chamber_schedule_id VARCHAR(4) NOT NULL UNIQUE,
    project_name VARCHAR(50) NOT NULL, -- allows for multiple experiments (ie acidic and neutral) under the same project
    sample_quantity INTEGER NOT NULL,
    start_date DATE NOT NULL DEFAULT (CURRENT_DATE()), -- if a start date isn't entered, the inbuild function CURRENT_DATE is called to give todays date
    duration INTEGER NOT NULL, -- in days
    chamber_id VARCHAR(25) NOT NULL, -- foreign key
    PRIMARY KEY (chamber_schedule_id),
    FOREIGN KEY (chamber_id) REFERENCES chamber_specification (chamber_id) );

-- Insert data into chamber_specification
INSERT INTO chamber_specification
(chamber_id,capacity,environment,calibration_due_date)
VALUES 
('red', 75, 'acidic', '2024-08-25'),
('green', 75, 'neutral', '2024-12-10'),
('blue', 25, 'neutral', '2024-12-10'),
('yellow', 50, 'acidic', '2025-06-21');

-- Insert data into chamber_schedule
INSERT INTO chamber_schedule
(chamber_schedule_id,project_name,sample_quantity,start_date,duration,chamber_id)
VALUES
('CS1', 'project_alpha', 10, '2024-06-10', 60, 'red'),
('CS2', 'project_beta', 25, '2024-06-25', 30, 'yellow'),
('CS3', 'project_gamma', 25, '2024-06-30', 7, 'blue'),
('CS4', 'project_delta', 75, '2024-05-28', 60, 'green'),
('CS5', 'project_rho', 10, '2024-07-30', 7, 'yellow'),
('CS6', 'project_lambda', 30, '2024-06-30', 30, 'red'),
('CS7', 'project_theta', 15, '2024-06-30', 45, 'red'),
('CS8', 'project_kappa', 5, '2024-06-30', 7, 'yellow');

SELECT * FROM chamber_specification;
SELECT * FROM chamber_schedule;

