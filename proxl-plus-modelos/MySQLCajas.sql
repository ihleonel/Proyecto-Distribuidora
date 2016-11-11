CREATE PROCEDURE agregarCaja(in anio int(4), in num int(4), in numero int(4),in fecha date, in inicial decimal(10, 2))
BEGIN
	INSERT INTO cajas(ccam_anio, ccam_num, caj_numero, caj_fecha, caj_inicial) 
	VALUES (anio, num, numero, fecha, inicial);
END$

CREATE FUNCTION cantidadCajas(anio int(4), num int(4)) RETURNS bigint(3)
BEGIN
	declare cont bigint(3);
	SELECT COUNT(*) INTO cont FROM cajas
	WHERE ccam_anio = anio AND ccam_num = num;
	RETURN cont;
END$

CREATE PROCEDURE cerrarCaja(in anio int(4), in num int(4), in numero int(4))
BEGIN
	UPDATE cajas SET caj_estado = 2 WHERE ccam_anio = anio AND ccam_num = num AND caj_numero = numero;
END$