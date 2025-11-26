-- 0. Create database `grao_mestre_db`
CREATE SCHEMA IF NOT EXISTS `grao_mestre_db` DEFAULT CHARACTER SET utf8 ;
USE `grao_mestre_db` ;

-- 1. Create `clients`
CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cnpj VARCHAR(255) NOT NULL UNIQUE,
    status ENUM('active', 'inactive', 'suspended') NOT NULL,
    trade_name VARCHAR(255) NOT NULL,
    company_name VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 2. Create `farm_addresses`
CREATE TABLE farm_addresses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cep VARCHAR(20) NOT NULL,
    street VARCHAR(255) NOT NULL,
    number VARCHAR(50) NOT NULL,
    complement VARCHAR(255) NULL,
    neighborhood VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    subdivision VARCHAR(255),
    country VARCHAR(255) NOT NULL DEFAULT 'Brazil',
    latitude DECIMAL(10, 7) NULL,
    longitude DECIMAL(10, 7) NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 3. Create `farms`
CREATE TABLE farms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    client_id INT NOT NULL,
    address_id INT NOT NULL,
    area FLOAT NOT NULL,
    status ENUM('active', 'inactive', 'suspended') NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (address_id) REFERENCES farm_addresses(id)
);

-- 4. Create `models`
CREATE TABLE models (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type ENUM('planting', 'spraying', 'harvesting') NOT NULL,
    batery_capacity FLOAT NOT NULL,
    fabrication_year INT NOT NULL,
    charging_time FLOAT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 5. Create `vehicles`
CREATE TABLE vehicles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status ENUM('in use', 'ready', 'decommissioned', 'not ready') NOT NULL,
    chassis VARCHAR(255) NOT NULL,
    observation TEXT,
    model_id INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES models(id)
);

-- 6. Create `contracts`
CREATE TABLE contracts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lease_deed TEXT NOT NULL,
    client_id INT NOT NULL,
    status BOOLEAN NOT NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- 7. Create `vehicles_contracts`
CREATE TABLE vehicles_contracts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contract_id INT NOT NULL,
    vehicle_id INT NOT NULL,
    observation TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (contract_id) REFERENCES contracts(id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
);

-- 8. Create `jobs_log`
CREATE TABLE jobs_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL,
    started_date TIMESTAMP NOT NULL,
    finished_date TIMESTAMP NOT NULL,
    observation TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
);

-- 9. Create `maintenances`
CREATE TABLE maintenances (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL,
    date TIMESTAMP NOT NULL,
    reason TEXT NOT NULL,
    link_to_ticket TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
);
