CREATE TABLE `movimiento_clientes` (
 `mcam_anio` int(4) NOT NULL,
 `mcam_num` int(4) NOT NULL,
 `mcaj_numero` int(4) NOT NULL,
 `mcli_codigo` varchar(100) NOT NULL,
 `movcli_monto` decimal(10, 2) NOT NULL default 0,
 `movcli_entregado` tinyint(1) NULL default 0,
 `movcli_forma_pago` tinyint(1) NULL default 0, 
 `movcli_diferencia` decimal(10, 2) NULL default 0,
 PRIMARY KEY  (`mcam_anio`,`mcam_num`,`mcaj_numero`, `mcli_codigo`),
 KEY `mcam_num` (`mcam_num`),
 KEY `mcaj_numero` (`mcaj_numero`),
 KEY `mcli_codigo` (`mcli_codigo`),
 CONSTRAINT `movimiento_clientes_ibfk_1` FOREIGN KEY (`mcam_anio`) REFERENCES `cajas` (`ccam_anio`) ON UPDATE CASCADE,
 CONSTRAINT `movimiento_clientes_ibfk_2` FOREIGN KEY (`mcam_num`) REFERENCES `cajas` (`ccam_num`) ON UPDATE CASCADE,
 CONSTRAINT `movimiento_clientes_ibfk_3` FOREIGN KEY (`mcaj_numero`) REFERENCES `cajas` (`caj_numero`) ON UPDATE CASCADE,
 CONSTRAINT `movimiento_clientes_ibfk_4` FOREIGN KEY (`mcli_codigo`) REFERENCES `clientes` (`cli_codigo`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8

DROP FUNCTION IF EXISTS existeMovimientoCliente$
CREATE FUNCTION existeMovimientoCliente(anio int(4), num int(4), cod varchar(100)) RETURNS bigint(3)
BEGIN
	declare cont bigint(3);
	SELECT COUNT(*) INTO cont FROM movimiento_clientes WHERE mcam_anio = anio AND mcam_num = num AND mcli_codigo = cod;
	RETURN cont;
END$

DROP PROCEDURE IF EXISTS agregarMovimientoCliente$
CREATE PROCEDURE agregarMovimientoCliente(in anio int(4), in num int(4), in cnum int(4), in cod varchar(100), in monto decimal(10, 2), in entr tinyint(1), in fpago tinyint(1), in dif decimal(10, 2))
BEGIN
	INSERT INTO movimiento_clientes VALUES (anio, num, cnum, cod, monto, entr, fpago, dif);
END$

DROP FUNCTION IF EXISTS totalIngresosMClientes$
CREATE FUNCTION totalIngresosMClientes(anio int(4), num int(4), cnum int(4)) RETURNS decimal(10, 2)
BEGIN
	declare totalMontos decimal(10, 2);
	declare totalDiferencias decimal(10, 2);
	declare resultado decimal(10, 2);
	SELECT SUM(movcli_monto) INTO totalMontos FROM movimiento_clientes WHERE mcam_anio = anio AND mcam_num = num AND mcaj_numero = cnum;
	SELECT SUM(movcli_diferencia) INTO totalDiferencias FROM movimiento_clientes WHERE mcam_anio = anio AND mcam_num = num AND mcaj_numero = cnum;
	
	SET resultado = totalMontos - totalDiferencias;
	IF resultado IS null THEN
		SET resultado = 0;
	END IF;
	
	RETURN resultado;
END$

DROP PROCEDURE IF EXISTS actualizarEntrega$
CREATE PROCEDURE actualizarEntrega(in anio int(4), in num int(4),in cnum int(4), in cod varchar(11), in entr tinyint(1), in fentr date)
BEGIN
	UPDATE movimiento_clientes SET movcli_entregado = entr
	WHERE mcam_anio = anio AND mcam_num = num AND mcaj_numero = cnum AND mcli_codigo = cod;

	UPDATE articulos SET art_entregado = fentr, art_medio_entr = 1
	WHERE acam_anio = anio AND acam_num = num AND acli_codigo = cod;
END$

DROP PROCEDURE IF EXISTS actualizarMovCli$
CREATE PROCEDURE actualizarMovCli(in anio int(4), in num int(4),in cnum int(4), in cod varchar(11),in mon decimal(10, 2), in entr tinyint(1), in fpago tinyint(1), in dif decimal(10, 2))
BEGIN
	UPDATE movimiento_clientes SET movcli_monto = mon, movcli_entregado = entr, movcli_forma_pago = fpago, movcli_diferencia = dif
	WHERE mcam_anio = anio AND mcam_num = num AND mcaj_numero = cnum AND mcli_codigo = cod;
END$

DROP PROCEDURE IF EXISTS superCargaMovimiento$
CREATE PROCEDURE superCargaMovimiento(
in anio int(4), 
in num int(4), 
in cnum int(4),  
in cod varchar(20),
in reb varchar(120),
in mentr tinyint(1), 
in monto decimal(10, 2), 
in entr tinyint(1), 
in fpago tinyint(1), 
in dif decimal(10, 2),
in fentr date)
BEGIN
	UPDATE articulos 
	SET art_forma_pago = fpago, art_medio_entr = mentr, art_entregado = fentr, art_rebote = reb
	WHERE acam_anio = anio AND acam_num = num AND acli_codigo = cod;

	INSERT INTO movimiento_clientes VALUES (anio, num, cnum, cod, monto, entr, fpago, dif); 

END$