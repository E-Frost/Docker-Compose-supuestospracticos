# odoo16_docker-compose

Una vez se tenga un proyecto nuevo utilizaremos el archivo docker-compose.yaml y lo copiamos en el propio. Este contiene dos contenedores, el de odoo y postsgress.

Para crear los contenedores utilizaremos el comando 

```bash  
docker-compose up -d 
```

Cuando ya ha acabado de crear los contenedores, veremos que ha creado las carpetas de adons y config. 

Ya podremos ejecutar odoo en localhost

```bash  
http://localhost:8069 
```

Para poder cambiar a modo desarrollador tenemos que cambiar en la url despues del web escribir "?debug=1"

```bash  
web?debug=1
```

Cunado hemos comprobado que podemos entrar, sino se ha creado en la carpeta de conf un archivo llamado <strong>odoo.conf</strong>, lo creamos nosotros he insertamos este codigo. Si se ha creado solo copiamos el codigo dentro

```bash  
[options]
addons_path = /mnt/extra-addons
```

Para poder crear modulos en odoo tenemos que acceder al contenedor para ejecutar comandos

```bash  
docker exec -u root -t -i [nombre contenedor odoo] /bin/bash
```

Una vez estemos dentro del contenedor crearemos un modulo

```bash  
odoo scaffold [nombre_modulo] /mnt/extra-addons
```

Y reseteamos el contenedor donde esta de odoo y de la dase de datos

```bash
docker restart [nombre contenedor]
```



## Comandos útiles docker

Ver las imagenes de docker instaladas 
```bash
docker images
```

Borrar imagen 
```bash
docker rmi [id]
```

Ver todos los contenedores 
```bash
docker container ls
```

Borrar contenedor 
```bash
docker rm [id]
```

Run contenedor 
```bash
docker start [id]
```

Parar contenedor 
```bash
docker stop [id]
```


Restart contenedor 
```bash
docker restart [id]
```

Parar todos contenedor 
```bash
docker stop $(docker ps -a -q)
```

Borrar todos contenedor 
```bash
docker stop $(docker ps -a -q)
```
