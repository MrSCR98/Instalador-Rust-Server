# Instalador Rust Server Python ![Python](https://img.shields.io/badge/Lenguaje-Python-yellow.svg) ![RUST](https://img.shields.io/badge/Juego-RUST-orange.svg) ![SCR98](https://img.shields.io/badge/Creador-SCR98-ff69b4.svg)

 <img src="https://github.com/MrSCR98/Instalador-Rust-Server/blob/main/README%20RECURSOS/ejemploinstalador.jpg?raw=true" alt="Logo" width="800" />

## Como iniciarlo ?

### - Primera forma:

Solo tendremos que descargar el ejecutable y iniciarlo: [Descargar Instalador Rust Server Python](https://github.com/MrSCR98/Instalador-Rust-Server/releases/download/Ejecutable/rustserverinstall.exe)

La primera vez lo más posible es que salte el antivirus.

Si queréis crear el ejecutable vosotros mismos sera muy facil primero instalaremos pyinstaller, yo usé la version:

```bash
pip install pyinstaller==5.9.0
```

A continuación haremos la build:

```bash
pyinstaller --onefile --windowed rustserverinstall.py
```

### - Segunda forma:

Tendremos que tener instalado Python y las dependencias que se utilizaron.

Ejecutamos rustserverinstall.py con la terminal, pero primero iremos a la carpeta del archivo:

```bash
cd tu ruta de carpeta 📂
```

también podemos escribir cd espacio y arrastramos la carpeta al cmd o terminal y se pondrá de manera más sencilla.

Después:

```bash
py rustserverinstall.py
```

o usando vscode para ejecutarlo (manera más fácil)

## Como se usa ?

### 1 INSTALAR Y ACTUALIZAR STEAMCMD

Para ello lo único que tendremos que hacer es hacer click en el **boton de Steam** y esperar a que la terminal se cierre automáticamente.

Esto se suele hacer solo una vez.

### 2 INSTALAR Y ACTUALIZAR SERVIDOR DE RUST

Para ello lo único que tendremos que hacer es hacer click en el **boton de Rust** y esperar a que la terminal se cierre automáticamente.

Se actualiza cada vez que sale un parche, normalmente el primer jueves de cada mes.

### (OPCIONAL) INSTALAR Y ACTUALIZAR OXIDE

Para ello lo único que tendremos que hacer es hacer click en el **boton de Oxide** y esperar a que la terminal se cierre automáticamente.

Se tiene que actualizar cada vez que se actualiza el servidor de rust.

Está última parte no es necesaria, pero sirve para poder poner plugins a nuestro servidor gracias a umod.

### COMO BORRAR TODO

Para ello hice un botón con una papelera que nos ayudará a borrar todos los archivos que se crearon.

### COMO INICIAR EL SERVIDOR ?

Si quieres poder iniciar el servidor, tendrás que crear un .bat que se crea a partir de un bloc de notas, pero dentro le tendrás que poner unos parámetros de lanzamiento. Para facilitar la tarea, ya hice un .bat **INICIADOR SERVER.bat** que contiene lo siguiente:

```bash
@echo off
RustDedicated.exe -batchmode -nographics ^
+server.hostname "Nombre de servidor" ^
+server.description "Instalador-Rust-Server" ^
+server.headerimage "" ^
+server.url "" ^
+server.ip 0.0.0.0 ^
+server.port 28015 ^
+server.maxplayers 100 ^
+rcon.ip 0.0.0.0 ^
+rcon.port 28016 ^
+rcon.password "cambia#estañc0ntraseña" ^
+server.identity "default" ^
+server.level "Procedural Map" ^
+server.seed 5658512 +server.worldsize 4000 ^
+server.radiation "True" ^
+bradley.enabled "True" ^
+bradley.respawndelayminutes "60" ^
+bradley.respawndelayvariance "1" ^
+heli.lifetimeminutes "15" ^
+server.stability "True" ^
+decay.upkeep "True" ^
+decay.upkeep_heal_scale "1" ^
+decay.upkeep_inside_decay_scale "0.1" ^
+decay.upkeep_period_minutes "1440" ^
+rcon.web "True" ^
-logfile "logfilename.log" ^
```

¿Dónde se pone? El archivo se tendrá que poner en la carpeta SERVER.
Intenta cambiar la contraseña de rcon.password por otra privada:

```bash
+rcon.password "cambia#estañc0ntraseña"
```

## Requerimientos

Este proyecto se hizo usando Python 3.11 y las siguientes versiones de librerías (Probado en Windows 10):

- flet: 0.7.4
- requests: 2.28.2

## Instalación

Para instalar las dependencias necesarias, puedes utilizar pip:

```bash
pip install flet==0.7.4 requests==2.28.2
```

Puede que también funcione en las últimas versiones de Python y de las librerías utilizadas:


```bash
pip install flet requests
```

## COSAS PARA MEJORAR

Poner foto al ejecutable .exe para Windows y hacer que no salte el antivirus?.

Controlar los errores.

Crear botón que haga un .bat editable desde la interfaz.

Quitar el icono de flet por otro...

Mejorar el código, ahora es código espagueti, pero funciona.

## Planes de futuro

Escribir la aplicación entera en Rust.
