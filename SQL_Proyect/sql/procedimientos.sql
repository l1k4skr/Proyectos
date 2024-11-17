CREATE OR REPLACE PROCEDURE InsertAndGetNewRecord(_name VARCHAR, _contact VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Insertar un nuevo registro
    INSERT INTO Vinedo (Nombre, Contacto) VALUES (_name, _contact);
    
    -- Seleccionar el último registro insertado
    SELECT * FROM Vinedo ORDER BY ID_vinedo DESC LIMIT 1;
END;
$$;

-- 
CREATE OR REPLACE PROCEDURE AddVinedoAndDireccion(
    _nombre VARCHAR,
    _contacto VARCHAR,
    _codigo_postal VARCHAR,
    _region VARCHAR,
    _calle VARCHAR,
    _ciudad VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    new_id_vinedo INT;
BEGIN
    -- Insertar en Vinedo y obtener el ID
    INSERT INTO Vinedo (Nombre, Contacto) VALUES (_nombre, _contacto) RETURNING ID_vinedo INTO new_id_vinedo;
    
    -- Insertar en Direccion utilizando el nuevo ID_vinedo
    INSERT INTO Direccion (Codigo_postal, Region, Calle, Ciudad, ID_vinedo) VALUES (_codigo_postal, _region, _calle, _ciudad, new_id_vinedo);
END;
$$;

