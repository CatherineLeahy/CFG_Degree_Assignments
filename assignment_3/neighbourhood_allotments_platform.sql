
-- Create database
CREATE DATABASE IF NOT EXISTS neighbourhood_allotments;
USE neighbourhood_allotments;

DROP TABLE IF EXISTS plant_care;
DROP TABLE IF EXISTS plants;
DROP TABLE IF EXISTS neighbours;
DROP TABLE IF EXISTS growing_plots;
DROP PROCEDURE IF EXISTS generate_plant_care_report;

-- Create growing_plots table
CREATE TABLE IF NOT EXISTS growing_plots (
	plot_id CHAR(4) NOT NULL UNIQUE,
    location VARCHAR(2) NOT NULL UNIQUE,
    size DECIMAL(5,2) NOT NULL, -- 5 characters total, accurate to 2 d.p (in m2)
    soil_type VARCHAR(8) NOT NULL,
    PRIMARY KEY (plot_id) );
    
-- Create plants table
CREATE TABLE IF NOT EXISTS plants (
	plant_id VARCHAR(3) NOT NULL UNIQUE,
    plot_id CHAR(4) NOT NULL, -- foreign key
    species VARCHAR(50) NOT NULL,
    planting_date DATE NOT NULL DEFAULT (CURRENT_DATE()), -- if a date isn't entered, the inbuild function getDate is called to give todays date
    growth_stage VARCHAR(15) NOT NULL,
    PRIMARY KEY (plant_id),
    FOREIGN KEY (plot_id) REFERENCES growing_plots (plot_id) );

-- Originally, the plant_care table referred to neighbours by their forename, surname and email. To normalise the database I chose to create a 4th table (neighbours) for all the neighbours information. This avoided duplication of neighbours information for each plant care action, and instead assigned each neighbour a unique ID. 
-- CREATE TABLE IF NOT EXISTS plant_care (
-- 	care_id VARCHAR(3) NOT NULL UNIQUE,
--     plant_id VARCHAR(3), -- foreign key
--     neighbour_forename VARCHAR(50),
--     neighbour_surname VARCHAR(50),
--     neighbour_email VARCHAR(50),
--     care_date DATE,
--     activity_type VARCHAR(25),
--     PRIMARY KEY (care_id),
--     FOREIGN KEY (plant_id) REFERENCES plants (plant_id),
--     FOREIGN KEY (neighbour_id) REFERENCES neighbours (neighbour_id) ON DELETE CASCADE ); -- ON DELETE CASCADE ensures that when a neighbour_id is deleted from the parent table (neighbours), it is also deleted in the child table (plant_care). One limitation of this database design is that upon removing a neighbour from the neighbours table, you then lose all their plant care entries.

-- Create neighbours table
CREATE TABLE IF NOT EXISTS neighbours (
	neighbour_id VARCHAR(3) NOT NULL UNIQUE,
    forename VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    mobile_number VARCHAR(15) NOT NULL UNIQUE, -- allows for UK mobile numbers to be entered with or without country code and spaces. 
	PRIMARY KEY (neighbour_id) );

-- Create plant_care table
CREATE TABLE IF NOT EXISTS plant_care (
	care_id VARCHAR(3) NOT NULL UNIQUE,
    plant_id VARCHAR(3) NOT NULL, -- foreign key
    neighbour_id VARCHAR(3) NOT NULL, -- foreign key
    care_date DATE NOT NULL DEFAULT(CURRENT_DATE()), -- if a date isn't entered, the inbuild function getDate is called to give todays date
    activity_type VARCHAR(25) NOT NULL,
    PRIMARY KEY (care_id),
    FOREIGN KEY (plant_id) REFERENCES plants (plant_id),
    FOREIGN KEY (neighbour_id) REFERENCES neighbours (neighbour_id) ON DELETE CASCADE ); -- ON DELETE CASCADE ensures that when a neighbour_id is deleted from the parent table (neighbours), it is also deleted in the child table (plant_care). One limitation of this database design is that upon removing a neighbour from the neighbours table, you then lose all their plant care entries.

-- Insert example data sets into growing_plots
INSERT INTO growing_plots 
(plot_id,location,size,soil_type)
VALUES 
('GP01', 'C', 1.62,'acidic'),
('GP02', 'N', 1.79,'acidic'),
('GP03', 'NE', 1.96,'acidic'),
('GP04', 'E', 2.13,'alkaline'),
('GP05', 'SE', 2.25,'alkaline'),
('GP06', 'S', 2.42,'alkaline'),
('GP07', 'SW', 2.57,'alkaline'),
('GP08', 'W', 2.74,'alkaline'),
('GP09', 'NW', 2.88,'acidic');

-- Insert example data sets into plants 
INSERT INTO plants
(plant_id,plot_id,species,planting_date,growth_stage)
VALUES
('P01','GP06','sweet pepper','2024-04-15','growing'),
('P02','GP09','kale','2024-04-07','mature'),
('P03','GP07','rocket','2024-04-01','mature'),
('P04','GP01','lavendar','2024-05-07','flowering'),
('P05','GP06','tomato','2024-05-15','flowering'),
('P06','GP07','basil','2024-05-01','mature'),
('P07','GP01','dwarf bean','2024-03-28','flowering'),
('P08','GP02','potato','2024-03-28','growing'),
('P09','GP03','carrot','2024-04-21','growing'),
('P10','GP03','beetroot','2024-04-01','growing'),
('P11','GP01','lavendar','2024-05-07','flowering'),
('P12','GP06','lavendar','2024-05-07','flowering'),
('P13','GP07','lavendar','2024-05-07','flowering'),
('P14','GP02','kale','2024-04-07','mature'),
('P15','GP03','kale','2024-04-07','mature'),
('P16','GP01','kale','2024-04-07','mature');

-- Insert example data sets into neighbours
INSERT INTO neighbours
(neighbour_id,forename,surname,email,mobile_number)
VALUES
('N01','Alice','Johnson','alice.johnson@example.com','+44 7700 900001'),
('N02','Bob','Smith','bob.smith@example.com','07700900002'), 
('N03','Carol','Williams','carol.williams@example.com','+447700900003'), 
('N04','David','Brown','david.brown@example.com','+44 7700 900004'), 
('N05','Eve','Davies','eve.davies@example.com','07700900005'), 
('N06','Frank','Miller','frank.miller@example.com','07700900006'), 
('N07','Grace','Wilson','grace.wilson@example.com','+447700900007'),
('N08','Hank','Martinez','hank.martinez@example.com','+447700900008'), 
('N09','Ivy','Anderson','ivy.anderson@example.com','+44 7700 900009'), 
('N10','Jack','Thompson','jack.thompson@example.com','+44 7700 900010'); 

-- Insert example data sets into plant_care
INSERT INTO plant_care
(care_id,plant_id,neighbour_id,care_date,activity_type)
VALUES
('C01','P02','N07','2024-06-01','harvested'),
('C02','P05','N03','2024-06-13','fertilised'),
('C03','P08','N06','2024-05-31','watered'),
('C04','P07','N05','2024-06-09','harvested'),
('C05','P06','N04','2024-06-12','harvested'),
('C06','P10','N08','2024-05-23','watered'),
('C07','P04','N03','2024-05-14','fertilised'),
('C08','P09','N01','2024-06-04','watered'),
('C09','P01','N08','2024-06-10','fertilised'),
('C10','P03','N07','2024-06-01','harvested');

-- No date entered, queried to check todays date is returned
INSERT INTO plant_care
(care_id,plant_id,neighbour_id,activity_type)
VALUES
('C11','P13','N07','harvested');
SELECT care_date FROM plant_care WHERE care_id = 'C11';

-- The tomato plants are now fruiting so updating growth_stage
UPDATE plants
SET growth_stage = 'fruiting'
WHERE plant_id = 'P05'; 

-- Grace Wilson got married so her surname is now Robinson
UPDATE neighbours
SET surname = 'Robinson',
	email = 'grace.robinson@example.com'
WHERE neighbour_id = 'N07';

-- A acidic soil treatment was applied to the Eastern growing plot
UPDATE growing_plots
SET soil_type = REPLACE(soil_type, 'alkaline','acidic')
WHERE plot_id = 'GP04'; 

-- The neighbourhood decided they only needed one form of contact details (mobile) in the database
ALTER TABLE neighbours
DROP COLUMN email;

-- The allotment manager has a missed call from 07700900002 and wanted to find out who called
SELECT forename, surname FROM neighbours WHERE mobile_number = '07700900006';

-- David Brown has moved out of the neighbourhood so his information should be deleted
SELECT neighbour_id FROM neighbours 
WHERE forename = 'David' AND surname = 'Brown'; -- This query returns David Brown's neighbour_ID to use in the delete query below
DELETE FROM neighbours 
WHERE neighbour_id = 'N04'; -- Deleting David Brown's data from DB using his neighbour_ID

-- Calculate the average size of the growing plots on the allotment
SELECT CAST(AVG(size) AS DECIMAL(5,2)) AS average_growing_plot_size -- Average aggregate function used and CAST inbuilt function returnin the average growing plot size as a 5 character decimal rounded to 2 d.p
FROM growing_plots;

-- Which growing plots have lavendar in?
SELECT gp.plot_id
FROM growing_plots gp
INNER JOIN plants p ON gp.plot_id = p.plot_id -- Joins plants and growing_plots tables by plot_id
WHERE p.species = 'lavendar'
GROUP BY gp.plot_id
ORDER BY plot_id ASC;

-- List all the plants in growing plot GP1?
SELECT plant_id, species 
FROM plants p
INNER JOIN growing_plots gp ON p.plot_id = gp.plot_id
WHERE gp.plot_id = 'GP01'
ORDER BY plant_id ASC;

-- Which plots are currently unoccupied?
SELECT gp.plot_id, 
COUNT(p.plot_id) AS number_plants -- COUNT aggregate function used to count number plants in each plot
FROM growing_plots gp -- growing_plots left table
LEFT JOIN plants p ON gp.plot_id = p.plot_id -- left join here ensures that even plots with 0 plants (excluded from the COUNT) are returned
GROUP BY gp.plot_id -- groups results
HAVING number_plants = 0 -- filters grouped results to only show unoccupied growing plots
ORDER BY plot_id ASC;

-- List neighbours full names
SELECT CONCAT(forename,' ',surname) AS full_name -- combines forename and surname columns
FROM neighbours
ORDER BY full_name ASC;

-- Procedure to generate a complete plant care report
DELIMITER //
CREATE PROCEDURE generate_plant_care_report()
BEGIN
    SELECT p.plant_id, p.species, n.forename, n.surname, pc.care_date, pc.activity_type
    FROM plant_care pc
    INNER JOIN plants p ON pc.plant_id = p.plant_id -- joins plants and plant_care tables by plant_id
    INNER JOIN neighbours n ON pc.neighbour_id = n.neighbour_id -- joins neighbours and plant_care tables by neighbour_id
    ORDER BY pc.care_date DESC;
END //
DELIMITER ;

-- generating plant care report using stored procedure created above
CALL generate_plant_care_report();

-- Viewing tables
SELECT * FROM growing_plots;
SELECT * FROM neighbours;
SELECT * FROM plants;
SELECT * FROM plant_care;
 





