-- Hospital Management System Database Schema
-- Run this script to create the database and tables

CREATE DATABASE IF NOT EXISTS hospital;
USE hospital;

-- Employee table (base table for all hospital staff)
CREATE TABLE IF NOT EXISTS Employee (
    employee_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(50),
    salary DECIMAL(10,2),
    shift VARCHAR(50)
);

-- Doctors table (extends Employee)
CREATE TABLE IF NOT EXISTS Doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    specialty VARCHAR(100),
    phno VARCHAR(20),
    email VARCHAR(100),
    address VARCHAR(255),
    employee_id VARCHAR(20) UNIQUE NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
);

-- Nurses table (extends Employee)
CREATE TABLE IF NOT EXISTS Nurses (
    nurse_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(1) CHECK(gender IN ('m', 'f')),
    employee_id VARCHAR(20) UNIQUE NOT NULL,
    contact_number VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    hire_date VARCHAR(25),
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
);

-- Patient table (connected to Doctors)
CREATE TABLE IF NOT EXISTS Patient (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    dob DATE,
    gender VARCHAR(1) CHECK (gender IN ('m','f')),
    blood_grp VARCHAR(5),
    illness VARCHAR(255),
    doc_id INT,
    doc_name VARCHAR(100),
    address VARCHAR(255),
    contact_number VARCHAR(20),
    email VARCHAR(100),
    FOREIGN KEY (doc_id) REFERENCES Doctors(doctor_id)
);

-- Visitor table
CREATE TABLE IF NOT EXISTS Visitor (
    visitor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    phone_number VARCHAR(50),
    time_of_arrival TIME,
    time_of_departure TIME,
    patient_id INT,
    patient_name VARCHAR(100),
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
);

-- Sample data insertion
INSERT INTO Employee (employee_id, name, city, salary, shift) VALUES
('EMP001', 'Dr. John Smith', 'New York', 120000.00, 'Day'),
('EMP002', 'Dr. Sarah Johnson', 'Los Angeles', 115000.00, 'Night'),
('EMP003', 'Nurse Mary Brown', 'Chicago', 65000.00, 'Day'),
('EMP004', 'Nurse David Wilson', 'Houston', 62000.00, 'Night');

INSERT INTO Doctors (name, specialty, phno, email, address, employee_id) VALUES
('Dr. John Smith', 'Cardiology', '555-0101', 'john.smith@hospital.com', '123 Main St, New York', 'EMP001'),
('Dr. Sarah Johnson', 'Neurology', '555-0102', 'sarah.johnson@hospital.com', '456 Oak Ave, Los Angeles', 'EMP002');

INSERT INTO Nurses (first_name, last_name, gender, employee_id, contact_number, email, hire_date) VALUES
('Mary', 'Brown', 'f', 'EMP003', '555-0201', 'mary.brown@hospital.com', '15/01/20'),
('David', 'Wilson', 'm', 'EMP004', '555-0202', 'david.wilson@hospital.com', '20/03/20');


-- Sample Patients
INSERT INTO Patient (name, dob, gender, blood_grp, illness, doc_id, doc_name, address, contact_number, email) VALUES
('Alice Green', '1990-05-12', 'f', 'A+', 'Flu', 1, 'Dr. John Smith', '789 Pine St, New York', '555-0301', 'alice.green@hospital.com'),
('Bob White', '1985-11-23', 'm', 'B-', 'Diabetes', 2, 'Dr. Sarah Johnson', '321 Maple Ave, Los Angeles', '555-0302', 'bob.white@hospital.com');

-- Sample Visitors
INSERT INTO Visitor (first_name, last_name, email, phone_number, time_of_arrival, time_of_departure, patient_id, patient_name) VALUES
('Emma', 'Green', 'emma.green@gmail.com', '555-0401', '09:00', '10:00', 1, 'Alice Green'),
('Charlie', 'White', 'charlie.white@gmail.com', '555-0402', '11:00', '12:00', 2, 'Bob White');
