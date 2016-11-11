CREATE TABLE `imprevistos` (
 `icam_anio` int(4) NOT NULL,
 `icam_num` int(4) NOT NULL,
 `i_numero` int(4) NOT NULL,
 `i_fecha` varchar(11) NULL default "-",
 `i_monto` decimal(10, 2) NOT NULL default 0,
 `i_concepto` varchar(30) NULL default "-",
 PRIMARY KEY  (`icam_anio`,`icam_num`,`i_numero`),
 KEY `icam_num` (`icam_num`),
 KEY `i_numero` (`i_numero`),
 CONSTRAINT `imprevisto_ibfk_1` FOREIGN KEY (`icam_anio`) REFERENCES `campanias` (`cam_anio`) ON UPDATE CASCADE,
 CONSTRAINT `imprevisto_ibfk_2` FOREIGN KEY (`icam_num`) REFERENCES `campanias` (`cam_num`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8

------------------------------------------------------------------
DROP FUNCTION IF EXISTS existeImprevisto$
CREATE FUNCTION existeImprevisto(anio int(4), num int(4), numero int(4)) RETURNS bigint(3)
BEGIN
	declare cont bigint(3);
	SELECT COUNT(*) INTO cont FROM imprevistos WHERE icam_anio = anio AND icam_num = num AND i_numero = numero;
	RETURN cont;
END$

DROP FUNCTION IF EXISTS cantidadImprevistos$
CREATE FUNCTION cantidadImprevistos(anio int(4), num int(4)) RETURNS bigint(3)
BEGIN
	declare cont bigint(3);
	SELECT COUNT(*) INTO cont FROM imprevistos WHERE icam_anio = anio AND icam_num = num;
	RETURN cont;
END$

DROP FUNCTION IF EXISTS ultimoImprevisto$
CREATE FUNCTION ultimoImprevisto(anio int(4), num int(4)) RETURNS int(4)
BEGIN
	declare max int(4);
	SELECT MAX(i_numero) INTO max FROM imprevistos WHERE icam_anio = anio AND icam_num = num;
	IF max IS Null THEN
		SET max = 0;
	END IF;
	RETURN max;
END$


DROP PROCEDURE IF EXISTS agregarImprevisto$
CREATE PROCEDURE agregarImprevisto(in anio int(4), 
									in num int(4), 
									in numero int(4), 
									in fecha varchar(11), 
									in monto decimal(10, 2), 
									in concepto varchar(30))
BEGIN
	INSERT INTO imprevistos VALUES (anio, num, numero, fecha, monto, concepto);
END$

DROP PROCEDURE IF EXISTS modificarImprevisto$
CREATE PROCEDURE modificarImprevisto(in anio int(4), 
									in num int(4), 
									in numero int(4),
									in fecha varchar(11), 
									in monto decimal(10, 2), 
									in concepto varchar(30))
BEGIN
	UPDATE imprevistos SET i_fecha = fecha, 
							i_monto = monto,
							i_concepto = concepto
	WHERE icam_anio = anio AND icam_num = num AND i_numero = numero;
END$

DROP PROCEDURE IF EXISTS eliminarImprevisto$
CREATE PROCEDURE eliminarImprevisto(in anio int(4), in num int(4), in numero int(4)) 
BEGIN
	DELETE FROM imprevistos WHERE icam_anio = anio AND icam_num = num AND i_numero = numero;
END$