-- Create database
CREATE DATABASE IF NOT EXISTS neighbourhood_allotments;
USE neighbourhood_allotments;

-- Create growing_plots table
CREATE TABLE IF NOT EXISTS growing_plots (
	plot_id CHAR(3) NOT NULL UNIQUE,
    location VARCHAR(2) NOT NULL UNIQUE,
    size FLOAT NOT NULL, -- how to add units of m2? 
    soil_type VARCHAR(8) NOT NULL );

-- Create neighbours table
CREATE TABLE IF NOT EXISTS neighbours (
	neighbour_ID VARCHAR(3) NOT NULL UNIQUE,
    forename VARCHAR (50) NOT NULL,
    surname VARCHAR (50) NOT NULL,
    email VARCHAR (50) NOT NULL UNIQUE,
    mobile_number VARCHAR(15) NOT NULL UNIQUE ); -- allows for UK mobile numbers to be entered with or without country code and spaces

-- Create plants table


-- Create plant_care table


-- Create events table


-- Create events_rsvp table

-- Insert example data sets into growing_plots
INSERT INTO growing_plots 
(plot_id,location,size,soil_type)
VALUES 
('GP1', 'C', '1.62','acidic'),
('GP2', 'N', '1.79','acidic'),
('GP3', 'NE', '1.96','acidic'),
('GP4', 'E', '2.13','alkaline'),
('GP5', 'SE', '2.25','alkaline'),
('GP6', 'S', '2.42','alkaline'),
('GP7', 'SW', '2.57','alkaline'),
('GP8', 'W', '2.74','alkaline'),
('GP9', 'NW', '2.88','acidic');

-- Insert example data sets into neighbours (random names, emails and phone numbers generated on chatGPT)
INSERT INTO neighbours
(neighbour_ID,forename,surname,email,mobile_number)
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