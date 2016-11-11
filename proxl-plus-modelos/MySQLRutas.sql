CREATE TABLE  `Rutas` (
 `rut_id` INT( 4 ) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
 `rut_nombre` VARCHAR( 20 ) NOT NULL DEFAULT  'NINGUNO',
 `rut_orden` INT( 4 ) NOT NULL DEFAULT  '0'
) ENGINE = INNODB;

DROP PROCEDURE IF EXISTS crearRuta$
CREATE PROCEDURE crearRuta(in nombre varchar(20), in orden int(4))
BEGIN
	INSERT INTO Rutas(rut_nombre, rut_orden) VALUES (nombre, orden);
END$

DROP PROCEDURE IF EXISTS modificarRuta$
CREATE PROCEDURE modificarRuta(in id int(4), in nombre varchar(20), in orden int(4))
BEGIN
	UPDATE Rutas SET rut_nombre = nombre, rut_orden = orden WHERE rut_id = id;
END$

DROP PROCEDURE IF EXISTS eliminarRuta$
CREATE PROCEDURE eliminarRuta(in id int(4))
BEGIN
	DELETE FROM Rutas WHERE rut_id = id;
END$

DROP TRIGGER integridadRefRuta;
CREATE TRIGGER integridadRefRuta BEFORE DELETE
ON rutas
FOR EACH ROW 
UPDATE clientes cli_ruta = 0, cli_orden = 0 
WHERE cli_ruta = OLD.rut_id;

DROP FUNCTION IF EXISTS existeRuta$
CREATE FUNCTION existeRuta(nombre varchar(20)) RETURNS bigint(8)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM rutas WHERE rut_nombre = nombre;
	RETURN cont;
END$