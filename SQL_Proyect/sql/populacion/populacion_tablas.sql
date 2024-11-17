-- 3.1. Insertar Viñedos
INSERT INTO Vinedo (Nombre, Contacto) VALUES
('Viña Santa Rita', '555-1234'),
('Viña Concha y Toro', '555-5678'),
('Viña Montes', '555-9012');

-- 3.2. Insertar Direcciones
INSERT INTO Direccion (Codigo_postal, Region, Calle, Ciudad, ID_vinedo) VALUES
('8320000', 'Valparaíso', 'Av. Libertad 123', 'Valparaíso', 1),
('7500000', 'Metropolitana', 'Calle Larga 456', 'Santiago', 2),
('9200000', 'Bio-Bío', 'Ruta 5 km 789', 'Concepción', 3);

-- 3.3. Insertar Salas de Venta
INSERT INTO Sala_de_Venta (Nombre, Stock, ID_vinedo) VALUES
('Sala Principal', 100, 1),
('Sala VIP', 50, 2),
('Sala de Degustación', 30, 3);

-- 3.4. Insertar Vinos
INSERT INTO Vino (Nombre, Stock, Precio) VALUES
('Cabernet Sauvignon', 200, 15.50),
('Merlot', 150, 13.75),
('Chardonnay', 180, 14.00);

-- 3.5. Insertar Sala_Venta_Vino (Relacionando Vinos con Salas de Venta)
-- Sala Principal (Codigo=1)
INSERT INTO Sala_Venta_Vino (Codigo, ID_vino, Stock) VALUES
(1, 1, 50),
(1, 2, 50),
(1, 3, 100);

-- Sala VIP (Codigo=2)
INSERT INTO Sala_Venta_Vino (Codigo, ID_vino, Stock) VALUES
(2, 1, 20),
(2, 2, 15),
(2, 3, 15);

-- Sala de Degustación (Codigo=3)
INSERT INTO Sala_Venta_Vino (Codigo, ID_vino, Stock) VALUES
(3, 1, 30),
(3, 3, 30);

-- 3.6. Insertar Clientes
INSERT INTO Cliente (Rut, Nombre, Numero_contacto, Correo_personal) VALUES
('12345678-9', 'Juan Pérez', '555-0001', 'juan.perez@example.com'),
('98765432-1', 'María López', '555-0002', 'maria.lopez@example.com'),
('11223344-5', 'Carlos Sánchez', '555-0003', 'carlos.sanchez@example.com');

-- 3.7. Insertar Correos
INSERT INTO Correo (Destinatario, Fecha, Hora, Rut) VALUES
('juan.perez@example.com', '2024-04-01', '10:30:00', '12345678-9'),
('maria.lopez@example.com', '2024-04-02', '11:00:00', '98765432-1'),
('carlos.sanchez@example.com', '2024-04-03', '09:45:00', '11223344-5');

-- 3.8. Insertar Compras
INSERT INTO Compra (Fecha, Hora, Tipo_pago, Descuentos, Codigo, Rut) VALUES
('2024-04-10', '14:30:00', 'Tarjeta', 5.00, 1, '12345678-9'),
('2024-04-11', '15:00:00', 'Efectivo', 0.00, 2, '98765432-1'),
('2024-04-12', '16:15:00', 'Transferencia', 10.00, 3, '11223344-5');

-- 3.9. Insertar Boleta_Factura
INSERT INTO Boleta_Factura (N_operacion, Descripcion_compra, ID_compra) VALUES
(1001, 'Compra de vinos y degustación', 1),
(1002, 'Compra de vino Merlot', 2),
(1003, 'Compra de vinos y tour', 3);

-- 3.10. Insertar Detalle (Detalle de Compras)
INSERT INTO Detalle (ID_compra, ID_vino, Cantidad) VALUES
(1, 1, 2), -- Compra 1: 2 Cabernet Sauvignon
(1, 3, 1), -- Compra 1: 1 Chardonnay
(2, 2, 3), -- Compra 2: 3 Merlot
(3, 1, 1), -- Compra 3: 1 Cabernet Sauvignon
(3, 3, 2); -- Compra 3: 2 Chardonnay

-- 3.11. Insertar Tours
INSERT INTO Tour (Horario, Precio, Cupos, ID_vinedo) VALUES
('09:00:00', 50.00, 20, 1),
('14:00:00', 60.00, 15, 2),
('11:00:00', 55.00, 10, 3);

-- 3.12. Insertar Servicios
INSERT INTO Servicios (Tipo) VALUES
('Degustación'),
('Visita Guiada'),
('Maridaje de Vinos');

-- 3.13. Insertar Tour_Servicio (Relacionando Tours con Servicios)
INSERT INTO Tour_Servicio (ID_tour, ID_servicio) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 2),
(3, 3);

-- 3.14. Insertar Tour_Programado
INSERT INTO Tour_Programado (ID_tour, Fecha, Hora) VALUES
(1, '2024-05-15', '09:00:00'),
(2, '2024-06-20', '14:00:00'),
(3, '2024-07-10', '11:00:00');

-- 3.15. Insertar Reservas
INSERT INTO Reserva (Codigo_descuento, Tipo_pago, Fecha, Numero_acompanantes, Lista_de_acompanantes, Rut) VALUES
('DESCUENTO10', 'Tarjeta', '2024-05-10', 2, 'Ana Gómez, Luis Martínez', '12345678-9'),
(NULL, 'Efectivo', '2024-06-18', 0, NULL, '98765432-1'),
('DESCUENTO5', 'Transferencia', '2024-07-05', 1, 'Sofía Díaz', '11223344-5');

-- 3.16. Insertar Reserva_Tour_Programado (Relacionando Reservas con Tours Programados)
INSERT INTO Reserva_Tour_Programado (N_operacion, ID_tour_programado) VALUES
(1, 1), -- Reserva 1: Tour Programado 1
(2, 2), -- Reserva 2: Tour Programado 2
(3, 3); -- Reserva 3: Tour Programado 3

-- 3.17. Insertar Reseñas
INSERT INTO Resena (Valoracion, Descripcion, Rut, ID_tour_programado) VALUES
(5, 'Excelente tour y servicio.', '12345678-9', 1),
(4, 'Muy buen tour, pero podría mejorar la organización.', '98765432-1', 2),
(3, 'El tour estuvo bien, pero esperaba más actividades.', '11223344-5', 3);