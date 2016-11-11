 
CREATE PROCEDURE insertarCliente(in cod varchar(20), in nom varchar(100), in dom varchar(50), in tel varchar(100),
							in bar varchar(50),in loc varchar(50), in sec varchar(50), in zon varchar(11), in des varchar(700))
BEGIN
	INSERT INTO clientes (cli_codigo, cli_apenom, cli_domicilio, cli_telefono,
                          cli_barrio, cli_localidad, cli_seccion, cli_zona, 
                          cli_descripcion, cli_alta)
    VALUES (cod, nom, dom, tel, bar, loc, sec, zon, des, CURDATE());
END$

CREATE PROCEDURE insertarCliente2(in cod varchar(20))
BEGIN
    INSERT INTO clientes (cli_codigo, cli_alta)
    VALUES (cod, CURDATE());
END$

CREATE PROCEDURE eliminarCliente(in cod varchar(20))
BEGIN
    UPDATE clientes SET cli_estado = 0, cli_baja = CURDATE() WHERE cli_codigo = cod;
END$

DROP PROCEDURE IF EXISTS actualizarCliente$
CREATE PROCEDURE actualizarCliente(in cod varchar(20), in nom varchar(100), in dom varchar(50), in tel varchar(100),
                            in bar varchar(50),in loc varchar(50), in sec varchar(50), in zona varchar(11), 
                            in des varchar(700), in ref tinyint(1), in rut_id int(4), in ord int(4) )
BEGIN
    UPDATE clientes SET 
    cli_apenom = nom,
    cli_domicilio = dom,
    cli_telefono = tel,
    cli_barrio = bar,
    cli_localidad = loc,
    cli_seccion = sec,
    cli_zona = zona,
    cli_descripcion = des,
    cli_referencia = ref, 
    cli_orden = ord,
    crut_id = rut_id WHERE cli_codigo = cod;
END$

CREATE FUNCTION existeCliente(cod varchar(20)) RETURNS tinyint(1)
BEGIN
    declare contador bigint(20);
    declare resultado tinyint(1);
    SELECT COUNT(*) INTO contador FROM clientes WHERE cli_codigo = cod;
    IF contador > 0 THEN
        SET resultado = 1;
    ELSE
        SET resultado = 0;
    END IF;
    RETURN resultado;
END$


CREATE PROCEDURE actualizandoTablaClientes(in cod varchar(20), in nom varchar(100), in dom varchar(50), in tel varchar(100),
                            in bar varchar(50),in loc varchar(50), in sec varchar(50), in zon varchar(11), in des varchar(700))
BEGIN
    declare cont bigint(3);
    SELECT COUNT(*) INTO cont FROM clientes WHERE cli_codigo = cod;
    IF cont > 0 THEN
        UPDATE clientes SET 
        cli_apenom = nom,
        cli_domicilio = dom,
        cli_telefono = tel,
        cli_barrio = bar,
        cli_localidad = loc,
        cli_seccion = sec,
        cli_zona = zon,
        cli_descripcion = des WHERE cli_codigo = cod;
        
    ELSE
        INSERT INTO clientes (cli_codigo, cli_apenom, cli_domicilio, cli_telefono,
                          cli_barrio, cli_localidad, cli_seccion, cli_zona, 
                          cli_descripcion, cli_alta)
        VALUES (cod, nom, dom, tel, bar, loc, sec, zon, des, CURDATE());
    END IF;
END$


