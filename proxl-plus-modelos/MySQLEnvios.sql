CREATE PROCEDURE agregarEnvio(in anio int(4), in num int(4), in numero int(4), in fecha varchar(11), in monto decimal(10, 2))
BEGIN
	INSERT INTO envios VALUES (anio, num, numero, fecha, monto);
END$

CREATE PROCEDURE modificarEnvio(in anio int(4), in num int(4), in numero int(4), in fecha varchar(11), in monto decimal(10, 2))
BEGIN
	UPDATE envios SET env_monto = monto, env_fecha = fecha WHERE ecam_anio = anio AND ecam_num = num AND env_numero = numero;
END$

CREATE PROCEDURE eliminarEnvio(in anio int(4), in num int(4), in numero int(4))
BEGIN
	DELETE FROM envios WHERE ecam_anio = anio AND ecam_num = num AND env_numero = numero;
END$

DROP FUNCTION IF EXISTS ultimoDeposito$
CREATE FUNCTION ultimoDeposito(anio int(4), num int(4)) RETURNS int(4)
BEGIN
	declare max int(4);
	SELECT MAX(env_numero) INTO max FROM envios WHERE ecam_anio = anio AND ecam_num = num;
	IF max IS Null THEN
		SET max = 0;
	END IF;
	RETURN max;
END$