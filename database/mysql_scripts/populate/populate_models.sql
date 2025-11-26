USE grao_mestre_db;

INSERT INTO models (type, batery_capacity, fabrication_year, charging_time, created_at, updated_at)
VALUES
('planting', 4500.00, 2021, 2.5, NOW(), NOW()),
('spraying', 3200.50, 2020, 1.8, NOW(), NOW()),
('harvesting', 5200.75, 2022, 3.2, NOW(), NOW()),
('planting', 4100.30, 2023, 2.1, NOW(), NOW()),
('spraying', 3500.00, 2024, 1.6, NOW(), NOW());
