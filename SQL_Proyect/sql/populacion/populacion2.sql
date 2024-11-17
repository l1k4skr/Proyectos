-- ==============================================
-- Insertar Datos Adicionales
-- ==============================================

-- 1. Insertar Viñedos Adicionales
INSERT INTO Vinedo (Nombre, Contacto) VALUES
('Viña Emiliana', '555-2345'),
('Viña Cousiño Macul', '555-6789');

-- 2. Insertar Direcciones para los Nuevos Viñedos
INSERT INTO Direccion (Codigo_postal, Region, Calle, Ciudad, ID_vinedo) VALUES
('8340000', 'Metropolitana', 'Camino a Melipilla 789', 'Santiago', 4),
('7550000', 'Metropolitana', 'Av. Quilín 1234', 'Santiago', 5);

-- 3. Insertar Salas de Venta para los Nuevos Viñedos
INSERT INTO Sala_de_Venta (Nombre, Stock, ID_vinedo) VALUES
('Sala de Cata', 80, 4),
('Sala Histórica', 60, 5);

-- 4. Insertar Nuevos Vinos
INSERT INTO Vino (Nombre, Stock, Precio) VALUES
('Syrah', 160, 16.00),
('Pinot Noir', 140, 18.50);

-- 5. Insertar Sala_Venta_Vino para las Nuevas Salas
-- Sala de Cata (Codigo=4)
INSERT INTO Sala_Venta_Vino (Codigo, ID_vino, Stock) VALUES
(4, 4, 80),  -- Syrah
(4, 5, 80);  -- Pinot Noir

-- Sala Histórica (Codigo=5)
INSERT INTO Sala_Venta_Vino (Codigo, ID_vino, Stock) VALUES
(5, 1, 30),  -- Cabernet Sauvignon
(5, 5, 30);  -- Pinot Noir

-- 6. Insertar Nuevos Clientes
INSERT INTO Cliente (Rut, Nombre, Numero_contacto, Correo_personal) VALUES
('22334455-6', 'Laura Gómez', '555-0004', 'laura.gomez@example.com'),
('66778899-0', 'Pedro Fernández', '555-0005', 'pedro.fernandez@example.com'),
('33445566-7', 'Ana Martínez', '555-0006', 'ana.martinez@example.com');

-- 7. Insertar Correos para los Nuevos Clientes
INSERT INTO Correo (Destinatario, Fecha, Hora, Rut) VALUES
('laura.gomez@example.com', '2022-03-15', '09:30:00', '22334455-6'),
('pedro.fernandez@example.com', '2023-08-22', '14:45:00', '66778899-0'),
('ana.martinez@example.com', '2026-11-05', '16:20:00', '33445566-7');

-- 8. Insertar Compras en Diferentes Años
INSERT INTO Compra (Fecha, Hora, Tipo_pago, Descuentos, Codigo, Rut) VALUES
('2022-04-18', '13:15:00', 'Efectivo', 0.00, 4, '22334455-6'),
('2023-05-20', '11:40:00', 'Tarjeta', 5.00, 5, '66778899-0'),
('2026-12-01', '17:50:00', 'Transferencia', 0.00, 2, '33445566-7');

-- 9. Insertar Boleta_Factura para las Nuevas Compras
INSERT INTO Boleta_Factura (N_operacion, Descripcion_compra, ID_compra) VALUES
(2001, 'Compra de Syrah y Pinot Noir', 4),
(2002, 'Compra de Cabernet Sauvignon y Pinot Noir', 5),
(2003, 'Compra de Merlot', 6);

-- 10. Insertar Detalle para las Nuevas Compras
INSERT INTO Detalle (ID_compra, ID_vino, Cantidad) VALUES
(4, 4, 2),  -- Compra 4: 2 Syrah
(4, 5, 1),  -- Compra 4: 1 Pinot Noir
(5, 1, 1),  -- Compra 5: 1 Cabernet Sauvignon
(5, 5, 2),  -- Compra 5: 2 Pinot Noir
(6, 2, 4);  -- Compra 6: 4 Merlot

-- 11. Insertar Nuevos Tours
INSERT INTO Tour (Horario, Precio, Cupos, ID_vinedo) VALUES
('10:00:00', 45.00, 25, 4),
('15:00:00', 70.00, 12, 5);

-- 12. Insertar Nuevos Servicios
INSERT INTO Servicios (Tipo) VALUES
('Paseo en Carruaje'),
('Clase de Enología');

-- 13. Insertar Tour_Servicio para los Nuevos Tours
INSERT INTO Tour_Servicio (ID_tour, ID_servicio) VALUES
(4, 4),  -- Tour 4 incluye Paseo en Carruaje
(4, 1),  -- Tour 4 incluye Degustación
(5, 5),  -- Tour 5 incluye Clase de Enología
(5, 2);  -- Tour 5 incluye Visita Guiada

-- 14. Insertar Tour_Programado en Diferentes Fechas y Años
INSERT INTO Tour_Programado (ID_tour, Fecha, Hora) VALUES
(4, '2022-05-20', '10:00:00'),
(5, '2023-09-15', '15:00:00'),
(1, '2026-01-10', '09:00:00');

-- 15. Insertar Reservas para los Nuevos Tours y Clientes
INSERT INTO Reserva (Codigo_descuento, Tipo_pago, Fecha, Numero_acompanantes, Lista_de_acompanantes, Rut) VALUES
('PROMO2022', 'Tarjeta', '2022-05-18', 1, 'Miguel Torres', '22334455-6'),
('SUMMER23', 'Efectivo', '2023-09-10', 3, 'Lucía Díaz, Roberto Gómez, Elena Sánchez', '66778899-0'),
('NEWYEAR26', 'Transferencia', '2026-01-05', 0, NULL, '33445566-7');

-- 16. Insertar Reserva_Tour_Programado para las Nuevas Reservas
INSERT INTO Reserva_Tour_Programado (N_operacion, ID_tour_programado) VALUES
(4, 4),  -- Reserva 4: Tour Programado 4
(5, 5),  -- Reserva 5: Tour Programado 5
(6, 6);  -- Reserva 6: Tour Programado 6 (ID_tour_programado=6)

-- Nota: Como hemos insertado solo 3 tours programados previamente, necesitamos agregar el tour programado con ID 6.

-- Insertar Tour_Programado adicional para Reserva 6
INSERT INTO Tour_Programado (ID_tour, Fecha, Hora) VALUES
(1, '2026-01-10', '09:00:00');  -- Esto generará ID_tour_programado=6

-- 17. Insertar Reseñas Adicionales
INSERT INTO Resena (Valoracion, Descripcion, Rut, ID_tour_programado) VALUES
(5, 'Una experiencia inolvidable en Viña Emiliana.', '22334455-6', 4),
(4, 'Excelente atención y hermosos paisajes.', '66778899-0', 5),
(5, 'Comenzando el año con un tour espectacular.', '33445566-7', 6);

-- 18. Insertar Más Compras y Detalles en Diferentes Años
INSERT INTO Compra (Fecha, Hora, Tipo_pago, Descuentos, Codigo, Rut) VALUES
('2022-06-25', '12:00:00', 'Tarjeta', 5.00, 4, '22334455-6'),
('2023-07-30', '13:30:00', 'Efectivo', 0.00, 5, '66778899-0'),
('2025-08-15', '14:45:00', 'Transferencia', 10.00, 1, '11223344-5');

INSERT INTO Boleta_Factura (N_operacion, Descripcion_compra, ID_compra) VALUES
(2004, 'Compra de vinos y souvenirs', 7),
(2005, 'Compra de Pinot Noir', 8),
(2006, 'Compra de Chardonnay', 9);

INSERT INTO Detalle (ID_compra, ID_vino, Cantidad) VALUES
(7, 4, 1),  -- Compra 7: 1 Syrah
(7, 3, 2),  -- Compra 7: 2 Chardonnay
(8, 5, 3),  -- Compra 8: 3 Pinot Noir
(9, 3, 4);  -- Compra 9: 4 Chardonnay

-- 19. Insertar Más Reservas y Tours Programados
-- Nuevos Tours Programados
INSERT INTO Tour_Programado (ID_tour, Fecha, Hora) VALUES
(2, '2025-09-10', '14:00:00'),  -- ID_tour_programado=7
(3, '2026-02-20', '11:00:00');  -- ID_tour_programado=8

-- Nuevas Reservas
INSERT INTO Reserva (Codigo_descuento, Tipo_pago, Fecha, Numero_acompanantes, Lista_de_acompanantes, Rut) VALUES
('AUTUMN25', 'Tarjeta', '2025-09-05', 2, 'Daniel Rojas, Fernanda Silva', '11223344-5'),
('WINTER26', 'Efectivo', '2026-02-15', 1, 'Isabel Núñez', '22334455-6');

-- Relacionar Reservas con Tours Programados
INSERT INTO Reserva_Tour_Programado (N_operacion, ID_tour_programado) VALUES
(7, 7),  -- Reserva 7: Tour Programado 7
(8, 8);  -- Reserva 8: Tour Programado 8

-- Insertar Reseñas para las Nuevas Reservas
INSERT INTO Resena (Valoracion, Descripcion, Rut, ID_tour_programado) VALUES
(4, 'Muy buen tour, disfrutamos mucho.', '11223344-5', 7),
(5, 'Excelente experiencia en Viña Montes.', '22334455-6', 8);

-- 20. Actualizar Stock de Vinos
-- Restar las cantidades vendidas del stock general
UPDATE Vino SET Stock = Stock - 2 WHERE ID_vino = 4;  -- Syrah vendido en Compra 4
UPDATE Vino SET Stock = Stock - 1 WHERE ID_vino = 5;  -- Pinot Noir vendido en Compra 4

-- Continuar actualizando el stock para los demás vinos vendidos según sea necesario

-- 21. Insertar Datos en Años Futuros y Pasados para Pruebas Adicionales
-- Compras en 2020 y 2027
INSERT INTO Compra (Fecha, Hora, Tipo_pago, Descuentos, Codigo, Rut) VALUES
('2020-03-10', '10:20:00', 'Efectivo', 0.00, 3, '98765432-1'),
('2027-04-12', '15:30:00', 'Tarjeta', 0.00, 1, '12345678-9');

INSERT INTO Boleta_Factura (N_operacion, Descripcion_compra, ID_compra) VALUES
(2007, 'Compra de Chardonnay', 10),
(2008, 'Compra de Cabernet Sauvignon', 11);

INSERT INTO Detalle (ID_compra, ID_vino, Cantidad) VALUES
(10, 3, 2),  -- Compra 10: 2 Chardonnay
(11, 1, 3);  -- Compra 11: 3 Cabernet Sauvignon

-- Reservas y Tours Programados en 2020 y 2027
INSERT INTO Tour_Programado (ID_tour, Fecha, Hora) VALUES
(3, '2020-03-15', '11:00:00'),  -- ID_tour_programado=9
(1, '2027-04-15', '09:00:00');  -- ID_tour_programado=10

INSERT INTO Reserva (Codigo_descuento, Tipo_pago, Fecha, Numero_acompanantes, Lista_de_acompanantes, Rut) VALUES
(NULL, 'Efectivo', '2020-03-12', 1, 'José Pérez', '98765432-1'),
('FUTURE27', 'Tarjeta', '2027-04-10', 2, 'Mariana López, Andrés Fuentes', '12345678-9');

INSERT INTO Reserva_Tour_Programado (N_operacion, ID_tour_programado) VALUES
(9, 9),   -- Reserva 9: Tour Programado 9
(10, 10); -- Reserva 10: Tour Programado 10

INSERT INTO Resena (Valoracion, Descripcion, Rut, ID_tour_programado) VALUES
(4, 'Un tour agradable en Viña Montes.', '98765432-1', 9),
(5, 'La mejor experiencia en viñas hasta ahora.', '12345678-9', 10);
