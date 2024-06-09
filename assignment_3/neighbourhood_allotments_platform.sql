-- Create database
CREATE DATABASE IF NOT EXISTS neighbourhood_allotments;
USE neighbourhood_allotments;

-- Create growing_plots table
CREATE TABLE IF NOT EXISTS growing_plots (
	plot_id CHAR(3) NOT NULL,
    location CHAR(2) NOT NULL,
    size FLOAT NOT NULL, -- how to add units of m2? 
    soil_type VARCHAR(8) NOT NULL );

-- Create neighbours table


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





