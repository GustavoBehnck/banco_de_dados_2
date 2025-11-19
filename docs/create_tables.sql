-- 1. Create `clients` first (referenced by farms and contracts)
CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cnpj VARCHAR(255) NOT NULL UNIQUE,
    status ENUM('active', 'inactive', 'suspended') NOT NULL,
    trade_name VARCHAR(255) NOT NULL,
    company_name VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 2. Create `farms` (references clients)
CREATE TABLE farms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    client_id INT NOT NULL,
    cep VARCHAR(20) NOT NULL,
    address VARCHAR(255) NULL, -- NotNull? was 'no'
    area FLOAT NOT NULL,
    status ENUM('active', 'inactive', 'suspended') NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- 3. Create `models` (referenced by vehicles)
CREATE TABLE models (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type ENUM('planting', 'spraying', 'harvesting') NOT NULL,
    batery_capacity FLOAT NOT NULL,
    fabrication_year INT NOT NULL,
    charging_time FLOAT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 4. Create `vehicles` (references models)
CREATE TABLE vehicles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status ENUM('in use', 'ready', 'decommissioned', 'not ready') NOT NULL,
    chassis VARCHAR(255) NOT NULL,
    observation TEXT NULL, -- NotNull? was 'no'
    model INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (model) REFERENCES models(id)
);

-- 5. Create `contracts` (references clients)
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

-- 6. Create `vehicles_contracted` (references contracts and vehicles)
CREATE TABLE vehicles_contracted (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contract_id INT NOT NULL,
    vehicle INT NOT NULL,
    observation TEXT NULL, -- NotNull? was 'no'
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (contract_id) REFERENCES contracts(id),
    FOREIGN KEY (vehicle) REFERENCES vehicles(id)
);

-- 7. Create `jobs_log` (references vehicles)
CREATE TABLE jobs_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL, -- Corrected typo from 'vehile_id'
    started_date TIMESTAMP NOT NULL,
    finished_date TIMESTAMP NOT NULL,
    observation TEXT NULL, -- NotNull? was 'no'
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
);

-- 8. Create `maintenances` (references vehicles)
CREATE TABLE maintenances (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL, -- Corrected typo from 'vehile_id'
    date TIMESTAMP NOT NULL,
    reason TEXT NOT NULL,
    link_to_ticket TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
);