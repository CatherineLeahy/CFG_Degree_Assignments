-- Create database
CREATE DATABASE IF NOT EXISTS corrosion_lab_equipment;
USE corrosion_lab_equipment;

DROP TABLE IF EXISTS chamber_schedule;
DROP TABLE IF EXISTS chamber_specification;

-- Create chamber_specification table
CREATE TABLE IF NOT EXISTS chamber_specification (
	chamber_id VARCHAR(25) NOT NULL UNIQUE, -- each chamber is a different colour so ID by colour
    environment VARCHAR(7) NOT NULL, -- can accommodate neutral or acidic
    calibration_due_date DATE NOT NULL, -- will calibration date interfere with experiment?
    PRIMARY KEY (chamber_id) );

-- Create chamber_schedule table
CREATE TABLE IF NOT EXISTS chamber_schedule (
    chamber_schedule_id VARCHAR(8) NOT NULL UNIQUE,
    project_name VARCHAR(100) NOT NULL, -- allows for multiple experiments (ie acidic and neutral) under the same project
    start_date DATE NOT NULL DEFAULT (CURRENT_DATE()), -- if a start date isn't entered, the inbuild function CURRENT_DATE is called to give todays date
    duration INTEGER NOT NULL, -- in days
    chamber_id VARCHAR(25) NOT NULL, -- foreign key
    PRIMARY KEY (chamber_schedule_id),
    FOREIGN KEY (chamber_id) REFERENCES chamber_specification (chamber_id) );

-- Insert data into chamber_specification
INSERT INTO chamber_specification
(chamber_id,environment,calibration_due_date)
VALUES 
('red', 'acidic', '2024-08-25'),
('green', 'neutral', '2024-12-10'),
('blue', 'neutral', '2024-12-10'),
('yellow', 'acidic', '2025-06-21');

-- Insert data into chamber_schedule
INSERT INTO chamber_schedule
(chamber_schedule_id,project_name,start_date,duration,chamber_id)
VALUES
('djyo94bf', 'project_alpha', '2024-05-01', 30, 'red'),
('sl5h70Al', 'project_beta', '2024-06-25', 30, 'yellow'),
('NH4hSot4', 'project_gamma', '2024-06-30', 7, 'blue'),
('sj7MB4H8', 'project_delta', '2024-05-28', 60, 'green'),
('5sl5nDiB', 'project_rho', '2024-07-30', 7, 'yellow'),
('AjN5Jdbi', 'project_lambda', '2024-06-05', 60, 'red'),
('bN48fsb4', 'project_theta', '2024-11-25', 45, 'red'),
('2DlHne05', 'project_kappa', '2024-08-24', 7, 'yellow');

SELECT * FROM chamber_specification;
SELECT * FROM chamber_schedule;

