# Procedimiento para ejecutar la limpieza de datos

Para ejecutar la limpieza de datos se debe de colocar los archivos de 
de ejecución en el mismo lugar en donde se encuentran los registros.
Los pasos que sigue son:

1. Realizar la relación entre los métodos para la limpieza de datos y 
estaciones de monitoreo por mes.
2. Se aplica el método correspondiente a las estaciones selccionadas.
3. Se intercambian los datos modificados con los datos originales teniendo 
como clave el *id*.
4. Se genera un archivo final con los datos modificados.

El procedimiento se realiza por año.

__nota:__ En la versión 1.0 solo se pueden leer archivos csv, en versiones 
posteriores se implentara codigo para que genere consultas de bases de datos.
