"DJANGO - VUE - SMODF1" 


para poder levantar el proyecto se deve de lavantar el servidor tanto en django como en el de Vue 
estos son los pasos para poder de realizar el correspondiente funcionamiento del proyecto. 

1: SMOD-f1 

Abre una consola de powershell 

en windows -> boton de inicio -> pwsh o powershell 
tambien puedes de usar directamente abriendo desde la ubicacion de esta carpeta de este archivo readme.md
una terminal o cmd 

ejecuta el directorio virtual: 

en CMD 

 C:\Users\<directorio-smodvue> denv\Scripts\activate 
 
 
luego de ejecutar el entorno virtual se puede de levantar el servidor de django: 


(denv) C:\Users\<directorio-smodvue> python smodf1-backend\manage.py runserver

de esta manera ya estaria el servicio de python en escucha para poder recibir la informacion del frontend


en otra terminal : 

C:\Users\<directorio-smodvue>cd smodf1-frontend
C:\Users\<directorio-smodvue> npm run serve

con este comando ya se tendria en funcionamiento el servidor del frontend 

por lo general tarda la primera vez cuando se ejecuta esto es por que el servicio tiene
la funcion de analizar tadas sus librerias 

cuando termine : se tendra la direccion 127.0.0.1:8080 
ya con la plataforma web SMODF1




