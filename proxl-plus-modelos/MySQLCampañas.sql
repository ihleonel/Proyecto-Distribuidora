DROP PROCEDURE IF EXISTS agregarCampania$
CREATE PROCEDURE agregarCampania(in anio int(4), 
                                in numero int(11),
                                in inicio date,
                                in ini_reparto varchar(11),
                                in diferencia decimal(10, 2),
                                in parametro decimal(10,2),
                                in base decimal(10, 2),
                                in comentario varchar(150), 
                                in usuario varchar(50))
BEGIN
    INSERT INTO campanias(cam_anio, 
                            cam_num,
                            cam_inicio,
                            cam_ini_reparto,
                            cam_diferencia,
                            cam_parametro,
                            cam_base, 
                            cam_comentario, 
                            cam_usuario) 
    VALUES 
                        (   anio,
                            numero, 
                            inicio,
                            ini_reparto, 
                            diferencia,
                            parametro,
                            base, 
                            comentario, 
                            usuario);
END$

DROP PROCEDURE IF EXISTS actualizarCampania$
CREATE PROCEDURE actualizarCampania(in anio int(4), 
                                    in num int(11),
                                    in ini_reparto varchar(11),
                                    in fin_reparto varchar(11),
                                    in diferencia decimal(10, 2),
                                    in parametro decimal(10, 2),
                                    in base decimal(10, 2), 
                                    in comentario varchar(150))
BEGIN
    UPDATE campanias 
    SET cam_ini_reparto = ini_reparto,
        cam_fin_reparto = fin_reparto,
        cam_diferencia = diferencia,
        cam_parametro = parametro,
        cam_base = base,
        cam_comentario = comentario
    WHERE cam_anio = anio AND cam_num = num;
END$


#retorna el siguiente numero de campaña dado un año(6 => 7)
CREATE FUNCTION siguienteNumeroCampania(anio int(4)) RETURNS int(4)
BEGIN
    declare cont bigint(3);
    declare max int(4);

    SELECT COUNT(*) INTO cont FROM campanias 
    WHERE cam_anio = anio;

    IF cont = 0 THEN
        SET max = 1;
    ELSE
        SELECT MAX(cam_num) INTO max FROM campanias
        WHERE cam_anio = anio;

        SET max = max + 1;
    END IF;
    RETURN max;
END$

CREATE FUNCTION existeCampania(anio int(4), num int(4)) RETURNS bigint(3)
BEGIN
    declare cont bigint(3);
    SELECT COUNT(*) INTO cont FROM campanias WHERE cam_anio = anio AND cam_num = num;
    RETURN cont;
END$

