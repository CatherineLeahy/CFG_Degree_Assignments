
-- Create database
CREATE DATABASE IF NOT EXISTS neighbourhood_allotments;
USE neighbourhood_allotments;

-- Create growing_plots table
CREATE TABLE IF NOT EXISTS growing_plots (
	plot_id CHAR(3), -- when adding PRIMARY KEY, is it still good practice to include NOT NULL?
    location VARCHAR(2) NOT NULL UNIQUE,
    size DECIMAL(5,2) NOT NULL, -- how to add units of m2? 5 characters total, accurate to 2 d.p
    soil_type VARCHAR(8) NOT NULL,
    PRIMARY KEY (plot_id) );

-- Create neighbours table
CREATE TABLE IF NOT EXISTS neighbours (
	neighbour_id VARCHAR(3),
    forename VARCHAR (50) NOT NULL,
    surname VARCHAR (50) NOT NULL,
    email VARCHAR (50) NOT NULL UNIQUE,
    mobile_number VARCHAR(15) NOT NULL UNIQUE, -- allows for UK mobile numbers to be entered with or without country code and spaces
	PRIMARY KEY (neighbour_id) );
    
-- Create plants table
CREATE TABLE IF NOT EXISTS plants (
	plant_id VARCHAR(3),
    plot_id CHAR(3) NOT NULL, -- foreign key
    species VARCHAR (50) NOT NULL,
    planting_date DATE NOT NULL,
    growth_stage VARCHAR(15) NOT NULL,
    PRIMARY KEY (plant_id),
    FOREIGN KEY (plot_id) REFERENCES growing_plots (plot_id) );

-- Create plant_care table
CREATE TABLE IF NOT EXISTS plant_care (
	care_id VARCHAR(3),
    plant_id VARCHAR(3), -- foreign key
    neighbour_id VARCHAR(3), -- foreign key
    care_date DATE,
    activity_type VARCHAR(25),
    PRIMARY KEY (care_id),
    FOREIGN KEY (plant_id) REFERENCES plants (plant_id),
    FOREIGN KEY (neighbour_id) REFERENCEs neighbours (neighbour_id) );

-- Create events table


-- Create events_rsvp table

-- Insert example data sets into growing_plots
INSERT INTO growing_plots 
(plot_id,location,size,soil_type)
VALUES 
('GP1', 'C', 1.62,'acidic'),
('GP2', 'N', 1.79,'acidic'),
('GP3', 'NE', 1.96,'acidic'),
('GP4', 'E', 2.13,'alkaline'),
('GP5', 'SE', 2.25,'alkaline'),
('GP6', 'S', 2.42,'alkaline'),
('GP7', 'SW', 2.57,'alkaline'),
('GP8', 'W', 2.74,'alkaline'),
('GP9', 'NW', 2.88,'acidic');

-- Insert example data sets into neighbours
INSERT INTO neighbours
(neighbour_id,forename,surname,email,mobile_number)
VALUES
('N1','Alice','Johnson','alice.johnson@example.com','+44 7700 900001'),
('N2','Bob','Smith','bob.smith@example.com','07700900002'), 
('N3','Carol','Williams','carol.williams@example.com','+447700900003'), 
('N4','David','Brown','david.brown@example.com','+44 7700 900004'), 
('N5','Eve','Davies','eve.davies@example.com','07700900005'), 
('N6','Frank','Miller','frank.miller@example.com','07700900006'), 
('N7','Grace','Wilson','grace.wilson@example.com','+447700900007'),
('N8','Hank','Martinez','hank.martinez@example.com','+447700900008'), 
('N9','Ivy','Anderson','ivy.anderson@example.com','+44 7700 900009'), 
('N10','Jack','Thompson','jack.thompson@example.com','+44 7700 900010'); 

-- Insert example data sets into plants 
INSERT INTO plants
(plant_id,plot_id,species,planting_date,growth_stage)
VALUES
('P1','GP6','sweet pepper','2024-04-15','growing'),
('P2','GP9','kale','2024-04-07','mature'),
('P3','GP7','rocket','2024-04-01','mature'),
('P4','GP1','lavendar','2024-05-07','flowering'),
('P5','GP6','tomato','2024-05-15','flowering'),
('P6','GP7','basil','2024-05-01','mature'),
('P7','GP1','dwarf bean','2024-03-28','flowering'),
('P8','GP2','potato','2024-03-28','growing'),
('P9','GP3','carrot','2024-04-21','growing'),
('P10','GP3','beetroot','2024-04-01','growing');

-- Insert example data sets into plant_care
INSERT INTO plant_care
(care_id,plant_id,neighbour_id,care_date,activity_type)
VALUES
('C1','P2','N7','2024-06-01','harvested'),
('C2','P5','N3','2024-06-13','fertilised'),
('C3','P8','N6','2024-05-31','watered'),
('C4','P7','N5','2024-06-09','harvested'),
('C5','P6','N4','2024-06-12','harvested'),
('C6','P10','N8','2024-05-23','watered'),
('C7','P4','N3','2024-05-14','fertilised'),
('C8','P9','N1','2024-06-04','watered'),
('C9','P1','N8','2024-06-10','fertilised'),
('C10','P3','N7','2024-06-01','harvested');
 
-- 3x queries to insert data

-- 5x queries to retrieve data

-- 1x query to delete data (David Brown has moved out of the neighbourhood so his information should be deleted)
DELETE FROM neighbours 
WHERE forename = 'David' AND surname = 'Brown';


-- 2x aggregate functions

-- 2x joins

-- 2x additional in-built functions

-- data sorting for majority of queries with ORDER BY

-- create and use one stored procedure or function to achieve a goal

-- normalise the DB 

-- Checking above tables for errors
SELECT * FROM growing_plots;
SELECT * FROM neighbours;
SELECT * FROM plants;
SELECT * FROM plant_care;
 
-- First and last names of all neighbours with the phone number 07700900002
SELECT forename, surname FROM neighbours WHERE mobile_number = '07700900002';

-- testing if dropping existing tables fixes error
DROP TABLE IF EXISTS plant_care;
DROP TABLE IF EXISTS plants;
DROP TABLE IF EXISTS neighbours;
DROP TABLE IF EXISTS growing_plots;



