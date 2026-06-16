-- 1. Tabla de Turnos (Definimos los tipos y su capacidad)
CREATE TABLE IF NOT EXISTS turnos (
    id SERIAL PRIMARY KEY,
    nombre_turno VARCHAR(20) UNIQUE NOT NULL, -- Ej: 'Mañana', 'Tarde', 'Noche'
    capacidad_maxima INTEGER NOT NULL
);

-- 2. Tabla de Usuarios (Empleados)
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    turno_id INTEGER REFERENCES turnos(id) -- Relación con la tabla turnos
);

-- 3. Insertar los turnos con sus capacidades definidas
INSERT INTO turnos (nombre_turno, capacidad_maxima) VALUES 
('Mañana', 40),
('Tarde', 25),
('Noche', 15)
ON CONFLICT (nombre_turno) DO NOTHING;

-- 4. Insertar algunos usuarios de prueba para tu laboratorio
INSERT INTO usuarios (nombre, email, turno_id) VALUES
('Ana García López', 'ana.garcia@empresa.com', 1),
('Carlos Martínez Ruiz', 'carlos.martinez@empresa.com', 1),
('Sofía Hernández Torres', 'sofia.hernandez@empresa.com', 2),
('Luis Ramírez Vega', 'luis.ramirez@empresa.com', 2),
('María Fernández Díaz', 'maria.fernandez@empresa.com', 3),
('Jorge Sánchez Morales', 'jorge.sanchez@empresa.com', 1),
('Laura Jiménez Castillo', 'laura.jimenez@empresa.com', 3),
('Pedro Álvarez Romero', 'pedro.alvarez@empresa.com', 2)
ON CONFLICT (email) DO NOTHING;
