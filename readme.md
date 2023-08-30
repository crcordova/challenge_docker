# Challenge docker
Documentación para configurar app de marcaje propuesta en el challenge  

## Ejecutar contenedores
__Primero__ configuramos el archivo docker-compose.yml en la seccion environment definimos nombre de la base de datos (MYSQL_DATABASE) y el password (MYSQL_PASSROD).  
también definos el container_name  
__Segundo__ configurar el archivo .env (ver .env.sample) donde:  
    - pass: será el password que definimos en el docker-compose.yml  
    - host: será el container_name que definimos en el docker-compose.yml  
    - bd: será el nomnre de la base de datos que definimos en el docker-compose.yml  
__Tercero__ el archivo .env debe ser copiado en tres carpetas '/api', '/DB' y '/backend'

```sh

docker compose build  

```

```sh

docker compose -f docker-compose.yml up

```
### Usar aplicación
Ya cargada la BD y a app se puede acceder a la API que esta en el puerto 8000, aqui podremos creaer Usuarios (post user) y ver, crear, eliminar marcas.  
Para crear una marca se debe enviar como parámetro el id del usuario y el tipo de marca, esta puede ser 'In' o 'Out'

### Generando Reporte
Para generar un reporte primero se debe solicitar, a traves del endpoint get /report, el cual enviara la BD la solicitud, el Backend que esta constantemente buscando solicitudes, generará la información para el reporte que puede ser desacargado a traves del endpoint get /download