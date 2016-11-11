DROP PROCEDURE IF EXISTS agregarArticulo$
CREATE PROCEDURE agregarArticulo (in cam_anio int(4),
								in cam_num int(4), 
								in lis_numero int (4), 
								in codigo varchar(20), 
								in deuda decimal(10, 2), 
								in camp varchar(3) )
BEGIN
	INSERT INTO articulos (acam_anio, 
						acam_num, 
						alis_numero, 
						acli_codigo, 
						art_camp, 
						art_deuda)
	VALUES (cam_anio, 
			cam_num, 
			lis_numero, 
			codigo, 
			camp, 
			deuda);
END$

DROP PROCEDURE IF EXISTS actualizarArticulo$
CREATE PROCEDURE actualizarArticulo (in cam_anio int(4),
								in cam_num int(4), 
								in lis_numero int (4), 
								in cli_codigo varchar(20), 
								in deuda decimal(10, 2), 
								in camp varchar(3),
								in entregado date,
								in forma_pago tinyint(1),
								in medio_entr tinyint(1),
								in rebote varchar(120))
BEGIN
	UPDATE articulos SET art_deuda = deuda,
						art_camp = camp, 
						art_entregado = entregado,
						art_forma_pago = forma_pago,
						art_medio_entr = medio_entr,
						art_rebote = rebote
	WHERE acam_anio = cam_anio 
	AND   acam_num = cam_num
	AND   alis_numero = lis_numero
	AND   acli_codigo = cli_codigo;
END$

DROP PROCEDURE IF EXISTS actualizarStock $
CREATE PROCEDURE actualizarStock(in anio int(4), in num int(4), in cod varchar(20), in cant tinyint(2))
BEGIN
	UPDATE articulos SET art_cant = cant
	WHERE acam_anio = anio 
	AND   acam_num = num
	AND   acli_codigo = cod;
END$


CREATE FUNCTION ocurrenciaCodigoEnCampania(anio int(4), num int(4), cod varchar(20)) RETURNS bigint(3)
BEGIN
	declare cont bigint(3);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND acli_codigo = cod;
	RETURN cont;
END$

# EN Articulos

SELECT COUNT(*) FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado <> '0000/00/00';

SELECT COUNT(*) FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado = '0000/00/00';

CREATE FUNCTION cantArticulosCampania(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num;
	RETURN cont;
END$

CREATE FUNCTION cantArticulosNoEntregados(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado = '0000/00/00';
	RETURN cont;
END$

CREATE FUNCTION cantArticulosBoletas(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_forma_pago = 2;
	RETURN cont;
END$

CREATE FUNCTION cantArticulosEntregadosNoCobrados(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado <> '0000/00/00' AND art_forma_pago = 0;
	RETURN cont;
END$

CREATE FUNCTION cantArticulosNoEntregadosNoCobrados(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado = '0000/00/00' AND art_forma_pago = 0;
	RETURN cont;
END$

CREATE FUNCTION cantArticulosNoCobrados(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_forma_pago = 0;
	RETURN cont;
END$


CREATE FUNCTION cantArticulosEntregadosEfectivo(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado <> '0000/00/00' AND art_forma_pago = 1;
	RETURN cont;
END$

CREATE FUNCTION cantArticulosNoEntregadosEfectivo(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado = '0000/00/00' AND art_forma_pago = 1;
	RETURN cont;
END$

CREATE FUNCTION cantArticulosCobradosEfectivo(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_forma_pago = 1;
	RETURN cont;
END$

CREATE FUNCTION cantArticulosEntregadosBoleta(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado <> '0000/00/00' AND art_forma_pago = 2;
	RETURN cont;
END$

CREATE FUNCTION cantArticulosNoEntregadosBoleta(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado = '0000/00/00' AND art_forma_pago = 2;
	RETURN cont;
END$

CREATE FUNCTION cantArticulosCobradosBoleta(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_forma_pago = 2;
	RETURN cont;
END$

CREATE FUNCTION cantArticulosEntregadosOficina(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado <> '0000/00/00' AND art_forma_pago = 3;
	RETURN cont;
END$

CREATE FUNCTION cantArticulosNoEntregadosOficina(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado = '0000/00/00' AND art_forma_pago = 3;
	RETURN cont;
END$

CREATE FUNCTION cantArticulosCobradosOficina(anio int(4), num int(4)) RETURNS bigint(6)
BEGIN
	declare cont bigint(8);
	SELECT COUNT(*) INTO cont FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_forma_pago = 3;
	RETURN cont;
END$

# EN $

CREATE FUNCTION valArticulosEntregados(anio int(4), num int(4)) RETURNS decimal(10,2)
BEGIN
	declare sum decimal(10,2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado <> '0000/00/00';
	RETURN sum;
END$

CREATE FUNCTION valArticulosNoEntregados(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado = '0000/00/00';
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

CREATE FUNCTION valArticulosBoletas(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_forma_pago  = 2;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

CREATE FUNCTION valArticulosCampania(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$


CREATE FUNCTION valArticulosEntregadosNoCobrados(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado <> '0000/00/00' AND art_forma_pago = 0;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

CREATE FUNCTION valArticulosNoEntregadosNoCobrados(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado = '0000/00/00' AND art_forma_pago = 0;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

CREATE FUNCTION valArticulosNoCobrados(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_forma_pago = 0;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

CREATE FUNCTION valArticulosEntregadosEfectivo(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado <> '0000/00/00' AND art_forma_pago = 1;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

CREATE FUNCTION valArticulosNoEntregadosEfectivo(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado = '0000/00/00' AND art_forma_pago = 1;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

CREATE FUNCTION valArticulosEfectivo(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_forma_pago = 1;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

CREATE FUNCTION valArticulosEntregadosBoleta(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado <> '0000/00/00' AND art_forma_pago = 2;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

CREATE FUNCTION valArticulosNoEntregadosBoleta(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado = '0000/00/00' AND art_forma_pago = 2;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

CREATE FUNCTION valArticulosBoleta(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_forma_pago = 2;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

CREATE FUNCTION valArticulosEntregadosOficina(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado <> '0000/00/00' AND art_forma_pago = 3;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

CREATE FUNCTION valArticulosNoEntregadosOficina(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_entregado = '0000/00/00' AND art_forma_pago = 3;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

CREATE FUNCTION valArticulosOficina(anio int(4), num int(4)) RETURNS decimal(10, 2)
BEGIN
	declare sum decimal(10, 2);
	SELECT SUM(art_deuda) INTO sum FROM articulos WHERE acam_anio = anio AND acam_num = num AND art_forma_pago = 3;
	IF sum is null THEN
		SET sum = 0;
	END IF;
	RETURN sum;
END$

DROP FUNCTION IF EXISTS articuloPagado$
CREATE FUNCTION articuloPagado(anio int(4), num int(4), cod varchar(20)) RETURNS decimal(10, 2)
BEGIN
	declare pago tinyint(1);
	SELECT art_forma_pago INTO pago FROM articulos WHERE acam_anio = anio AND acam_num = num AND acli_codigo = cod;
	IF pago is null THEN
		SET pago = -1; 
	END IF;
	RETURN pago;
END$

DROP FUNCTION IF EXISTS articuloEntregado$
CREATE FUNCTION articuloEntregado(anio int(4), num int(4), cod varchar(20)) RETURNS date
BEGIN
	declare fecha date;
	SELECT art_entregado INTO fecha FROM articulos WHERE acam_anio = anio AND acam_num = num AND acli_codigo = cod;
	RETURN fecha;
END$

DROP FUNCTION IF EXISTS historial$
CREATE FUNCTION historial(rango int(4), anio int(4), num int(4), cod varchar(20)) RETURNS varchar(255)
BEGIN
    declare i int(4) default 1;
    declare a int(4);
    declare n int(4);
    declare reb varchar(120);
    declare hist varchar(255) default '';
    declare cont bigint(8);
    SET a = anio;
    SET n = num;
    WHILE i <= rango DO
        SELECT COUNT(*) INTO cont
        FROM articulos WHERE acam_anio = a AND acam_num = n AND acli_codigo = cod;
        IF cont > 0 THEN
            SELECT art_rebote INTO reb
            FROM articulos WHERE acam_anio = a AND acam_num = n AND acli_codigo = cod; 
            SET hist = CONCAT(hist, ',', reb);
        ELSE
            SET hist = CONCAT(hist, ',', 'x');
        END IF;

        IF n = 1 THEN
            SET n = 18;
            SET a = a - 1;
        ELSE
            SET n = n - 1;
        END IF;
        SET i = i + 1;
    END WHILE;

    RETURN hist;
END$

