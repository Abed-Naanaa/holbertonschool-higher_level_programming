-- Creates table unique_id with unique id INT default 1 and name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
  id INT NOT NULL DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);
