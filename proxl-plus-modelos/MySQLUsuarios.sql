CREATE FUNCTION existeUsuario(usu varchar(50)) RETURNS tinyint(1)
BEGIN
	declare cont bigint(20);
	declare resp tinyint(1);
	SELECT COUNT(*) INTO cont FROM usuarios WHERE usu_usuario = usu;
	IF cont > 0 THEN
		SET resp = 1;
	ELSE
		SET resp = 0;
	END IF;
	RETURN resp;
END$

CREATE FUNCTION existeUsuarioClave(usu varchar(50), cla varchar(20)) RETURNS tinyint(1)
BEGIN
	declare cont bigint(20);
	declare resp tinyint(1);
	SELECT COUNT(*) INTO cont FROM usuarios WHERE usu_usuario = usu AND usu_clave = cla AND usu_estado = 1;
	IF cont > 0 THEN
		SET resp = 1;
	ELSE
		SET resp = 0;
	END IF;
	RETURN resp;
END$

CREATE FUNCTION tipoUsuario(usu varchar(50), cla varchar(20)) RETURNS varchar(20)
BEGIN
	declare cont bigint(20);
	declare resp varchar(20);
	SELECT COUNT(*) INTO cont FROM usuarios WHERE usu_usuario = usu AND usu_clave = cla;
	IF cont > 0 THEN
		SELECT usu_tipo INTO resp FROM usuarios WHERE usu_usuario = usu AND usu_clave = cla;
	ELSE
		SET resp = 'error user-key';
	END IF;
	RETURN resp;
END$

CREATE PROCEDURE agregarUsuario(usu varchar(50), cla varchar(20), tip varchar(20))
BEGIN
	INSERT INTO usuarios(usu_usuario, usu_clave, usu_tipo) VALUES (usu, cla, tip); 
END$

CREATE PROCEDURE deshabilitarUsuario(usu varchar(20))
BEGIN
	UPDATE usuarios SET usu_estado = 0 WHERE usu_usuario = usu;
END$

CREATE PROCEDURE modificarUsuario(usu varchar(50), cla varchar(20), tip varchar(20))
BEGIN
	UPDATE usuarios SET usu_clave = cla, usu_tipo = tip WHERE usu_usuario = usu;
END$



