-- Deshabilitar temporalmente las restricciones de claves foráneas
SET session_replication_role = 'replica';

-- Eliminar tablas en el orden inverso al de su creación para evitar conflictos
DROP TABLE IF EXISTS Resena CASCADE;
DROP TABLE IF EXISTS Reserva_Tour_Programado CASCADE;
DROP TABLE IF EXISTS Reserva CASCADE;
DROP TABLE IF EXISTS Tour_Programado CASCADE;
DROP TABLE IF EXISTS Tour_Servicio CASCADE;
DROP TABLE IF EXISTS Servicios CASCADE;
DROP TABLE IF EXISTS Tour CASCADE;
DROP TABLE IF EXISTS Detalle CASCADE;
DROP TABLE IF EXISTS Boleta_Factura CASCADE;
DROP TABLE IF EXISTS Compra CASCADE;
DROP TABLE IF EXISTS Correo CASCADE;
DROP TABLE IF EXISTS Cliente CASCADE;
DROP TABLE IF EXISTS Sala_Venta_Vino CASCADE;
DROP TABLE IF EXISTS Vino CASCADE;
DROP TABLE IF EXISTS Sala_de_Venta CASCADE;
DROP TABLE IF EXISTS Direccion CASCADE;
DROP TABLE IF EXISTS Vinedo CASCADE;

-- Reactivar las restricciones de claves foráneas
SET session_replication_role = 'origin';

-- ==============================================
-- 2. Creación de todas las tablas sin restricciones de formato de texto
-- ==============================================

-- 2.1. Tabla Vinedo
CREATE TABLE Vinedo (
    ID_vinedo SERIAL PRIMARY KEY,
    Nombre VARCHAR(150) NOT NULL UNIQUE,
    Contacto VARCHAR(20) NOT NULL
);

-- 2.2. Tabla Direccion
CREATE TABLE Direccion (
    Codigo_postal VARCHAR(10) PRIMARY KEY,
    Region VARCHAR(100) NOT NULL,
    Calle VARCHAR(200) NOT NULL,
    Ciudad VARCHAR(100) NOT NULL,
    ID_vinedo INT UNIQUE,
    FOREIGN KEY (ID_vinedo) REFERENCES Vinedo(ID_vinedo)
);

-- 2.3. Tabla Sala_de_Venta
CREATE TABLE Sala_de_Venta (
    Codigo SERIAL PRIMARY KEY,
    Nombre VARCHAR(150) NOT NULL,
    Stock INT NOT NULL CHECK (Stock >= 0),
    ID_vinedo INT UNIQUE,
    FOREIGN KEY (ID_vinedo) REFERENCES Vinedo(ID_vinedo),
    CONSTRAINT unique_nombre_sala UNIQUE (Nombre, ID_vinedo)
);

-- 2.4. Tabla Vino
CREATE TABLE Vino (
    ID_vino SERIAL PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL UNIQUE,
    Stock INT NOT NULL CHECK (Stock >= 0),
    Precio NUMERIC(10, 2) NOT NULL CHECK (Precio >= 0)
);

-- 2.5. Tabla Sala_Venta_Vino (relación N:M entre Sala_de_Venta y Vino)
CREATE TABLE Sala_Venta_Vino (
    Codigo INT NOT NULL,
    ID_vino INT NOT NULL,
    Stock INT NOT NULL CHECK (Stock >= 0),
    PRIMARY KEY (Codigo, ID_vino),
    FOREIGN KEY (Codigo) REFERENCES Sala_de_Venta(Codigo),
    FOREIGN KEY (ID_vino) REFERENCES Vino(ID_vino)
);

-- 2.6. Tabla Cliente
CREATE TABLE Cliente (
    Rut CHAR(12) PRIMARY KEY,
    Nombre VARCHAR(150) NOT NULL,
    Numero_contacto VARCHAR(20) NOT NULL,
    Correo_personal VARCHAR(150) UNIQUE NOT NULL
);

-- 2.7. Tabla Correo (1:1 relación con Cliente)
CREATE TABLE Correo (
    ID_correo SERIAL PRIMARY KEY,
    Destinatario VARCHAR(150) NOT NULL,
    Fecha DATE NOT NULL,
    Hora TIME NOT NULL,
    Rut CHAR(12) UNIQUE,
    FOREIGN KEY (Rut) REFERENCES Cliente(Rut)
);

-- 2.8. Tabla Compra
CREATE TABLE Compra (
    ID_compra SERIAL PRIMARY KEY,
    Fecha DATE NOT NULL,
    Hora TIME NOT NULL,
    Tipo_pago VARCHAR(50) NOT NULL,
    Descuentos NUMERIC(10, 2) CHECK (Descuentos >= 0),
    Codigo INT NOT NULL,
    Rut CHAR(12) NOT NULL,
    FOREIGN KEY (Codigo) REFERENCES Sala_de_Venta(Codigo),
    FOREIGN KEY (Rut) REFERENCES Cliente(Rut)
);

-- 2.9. Tabla Boleta_Factura (1:1 relación con Compra)
CREATE TABLE Boleta_Factura (
    N_operacion INT PRIMARY KEY,
    Descripcion_compra TEXT NOT NULL,
    ID_compra INT UNIQUE,
    FOREIGN KEY (ID_compra) REFERENCES Compra(ID_compra)
);

-- 2.10. Tabla Detalle (relación 1:N con Compra y Vino)
CREATE TABLE Detalle (
    ID_compra INT NOT NULL,
    ID_vino INT NOT NULL,
    Cantidad INT NOT NULL CHECK (Cantidad > 0),
    PRIMARY KEY (ID_compra, ID_vino),
    FOREIGN KEY (ID_compra) REFERENCES Compra(ID_compra),
    FOREIGN KEY (ID_vino) REFERENCES Vino(ID_vino)
);

-- 2.11. Tabla Tour
CREATE TABLE Tour (
    ID_tour SERIAL PRIMARY KEY,
    Horario TIME NOT NULL,
    Precio NUMERIC(10, 2) NOT NULL CHECK (Precio >= 0),
    Cupos INT NOT NULL CHECK (Cupos >= 0),
    ID_vinedo INT NOT NULL,
    FOREIGN KEY (ID_vinedo) REFERENCES Vinedo(ID_vinedo)
);

-- 2.12. Tabla Servicios
CREATE TABLE Servicios (
    ID_servicio SERIAL PRIMARY KEY,
    Tipo VARCHAR(100) NOT NULL UNIQUE
);

-- 2.13. Tabla Tour_Servicio (relación N:M entre Tour y Servicios)
CREATE TABLE Tour_Servicio (
    ID_tour INT NOT NULL,
    ID_servicio INT NOT NULL,
    PRIMARY KEY (ID_tour, ID_servicio),
    FOREIGN KEY (ID_tour) REFERENCES Tour(ID_tour),
    FOREIGN KEY (ID_servicio) REFERENCES Servicios(ID_servicio)
);

-- 2.14. Tabla Tour_Programado
CREATE TABLE Tour_Programado (
    ID_tour_programado SERIAL PRIMARY KEY,
    ID_tour INT NOT NULL,
    Fecha DATE NOT NULL,
    Hora TIME NOT NULL,
    FOREIGN KEY (ID_tour) REFERENCES Tour(ID_tour)
);

-- 2.15. Tabla Reserva
CREATE TABLE Reserva (
    N_operacion SERIAL PRIMARY KEY,
    Codigo_descuento VARCHAR(50),
    Tipo_pago VARCHAR(50) NOT NULL,
    Fecha DATE NOT NULL,
    Numero_acompanantes INT NOT NULL DEFAULT 0 CHECK (Numero_acompanantes >= 0),
    Lista_de_acompanantes TEXT,
    Rut CHAR(12) NOT NULL,
    FOREIGN KEY (Rut) REFERENCES Cliente(Rut)
);

-- 2.16. Tabla Reserva_Tour_Programado (relación N:M entre Reserva y Tour_Programado)
CREATE TABLE Reserva_Tour_Programado (
    N_operacion INT NOT NULL,
    ID_tour_programado INT NOT NULL,
    PRIMARY KEY (N_operacion, ID_tour_programado),
    FOREIGN KEY (N_operacion) REFERENCES Reserva(N_operacion),
    FOREIGN KEY (ID_tour_programado) REFERENCES Tour_Programado(ID_tour_programado)
);

-- 2.17. Tabla Resena
CREATE TABLE Resena (
    N_resena SERIAL PRIMARY KEY,
    Valoracion INT NOT NULL CHECK (Valoracion BETWEEN 1 AND 5),
    Descripcion TEXT,
    Rut CHAR(12) NOT NULL,
    ID_tour_programado INT NOT NULL,
    UNIQUE (Rut, ID_tour_programado),
    FOREIGN KEY (Rut) REFERENCES Cliente(Rut),
    FOREIGN KEY (ID_tour_programado) REFERENCES Tour_Programado(ID_tour_programado)
);
