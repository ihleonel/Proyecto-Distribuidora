CREATE PROCEDURE agregarListado(in cam_anio int(4), 
								in cam_num int(4), 
								in numero int(4), 
								in fecha date, 
								in comentario varchar(80))
BEGIN
	INSERT INTO listados (lcam_anio, 
							lcam_num, 
							lis_numero, 
							lis_fecha, 
							lis_comentario)
	VALUES (cam_anio, 
			cam_num, 
			numero, 
			fecha, 
			comentario);
END$

CREATE PROCEDURE actualizarListado(in cam_anio int(4), 
									in cam_num int(4),
									in numero int(4), 
									in comentario varchar(80))
BEGIN
	UPDATE listados SET lis_comentario = comentario
	WHERE lcam_anio = cam_anio AND lcam_num = cam_num AND lis_numero = numero;
END$

CREATE PROCEDURE eliminarListado(in cam_anio int(4), 
								in cam_num int(4), 
								in numero int(4))
BEGIN
	DELETE FROM articulos WHERE acam_anio = cam_anio AND acam_num = cam_num AND alis_numero = numero;
	DELETE FROM listados WHERE lcam_anio = cam_anio AND lcam_num = cam_num AND lis_numero = numero;
END$

CREATE FUNCTION cantidadListados(anio int(4), num int(4)) RETURNS bigint(3)
BEGIN
	declare cont bigint(3);
	SELECT COUNT(*) INTO cont FROM listados
	WHERE lis_numero > 0 AND lcam_anio = anio AND lcam_num = num;
	RETURN cont;
END$