SELECT table_name --seleccionamos solo la columna del nombre de la tabla
FROM information_schema.tables --seleccionamos la información del esquema 
WHERE table_schema='public' --las tablas se encuentran en el esquema publico
AND table_type='BASE TABLE'; --tiene que ser del tipo table ya que aqui se listan tambien las vistas 