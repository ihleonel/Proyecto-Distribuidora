CREATE PROCEDURE agregarMovimiento(in anio int(4), in num int(4), in cnum int(4), in mnum int(4), in monto decimal(10, 2), in tipo int(1), in coment varchar(50))
BEGIN
	INSERT INTO movimientos(mcam_anio, mcam_num, mcaj_numero, mov_numero, mov_monto, mov_tipo, mov_comentario)
	VALUES (anio, num, cnum, mnum, monto, tipo, coment);
END$


CREATE FUNCTION cantidadMovimientos(anio int(4), num int(4), cnum int(4)) RETURNS bigint(3)
BEGIN
	declare cont bigint(3);
	SELECT COUNT(*) INTO cont FROM movimientos WHERE mcam_anio = anio AND mcam_num = num AND mcaj_numero = cnum;
	RETURN cont;
END$

DROP FUNCTION IF EXISTS totalIngresos$
CREATE FUNCTION totalIngresos(anio int(4), num int(4), cnum int(4)) RETURNS decimal(10, 2)
BEGIN
	declare cont bigint(3);
	declare inicial decimal(10, 2);
	declare acum decimal(10, 2);
	SET inicial = 0;
	SELECT COUNT(*) INTO cont FROM cajas WHERE ccam_anio = anio AND ccam_num = num AND caj_numero = cnum AND caj_estado = 1;
	IF cont > 0 THEN
		SELECT caj_inicial INTO inicial FROM cajas WHERE ccam_anio = anio AND ccam_num = num AND caj_numero = cnum;
	END IF;

	SELECT SUM(mov_monto) INTO acum FROM movimientos
	WHERE mcam_anio = anio AND mcam_num = num AND mcaj_numero = cnum AND mov_tipo = 1;
	IF acum IS null THEN
		SET acum = 0;
	END IF;
	SET acum = inicial + acum;
	RETURN acum;
END$

DROP FUNCTION IF EXISTS totalEgresos$
CREATE FUNCTION totalEgresos(anio int(4), num int(4), cnum int(4)) RETURNS decimal(10, 2)
BEGIN
	declare acum decimal(10, 2);
	SELECT SUM(mov_monto) INTO acum FROM movimientos
	WHERE mcam_anio = anio AND mcam_num = num AND mcaj_numero = cnum AND mov_tipo = 2;
	IF acum IS null THEN
		SET acum = 0;
	END IF;
	RETURN acum;
END$

