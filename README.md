# Ejecución de Tests Funcionales de la Clasificación de tableros

### Paso 0: Ingrese al Escritorio remoto

### Paso 1: Fork del Repositorio Original

En el navegador, inicie sesión en Github. Luego, vaya al enlace del proyecto original (https://github.com/JohRiCh10/Clasificacion_tableros) y dé click al botón "Fork". Esto copiará todo el proyecto en su usuario de Github.


### Paso 2: Levantar el contenedor de Python

```
docker run -it --rm -p 8888:8888 jupyter/pyspark-notebook
```


### Paso 3: Configurar git

Abra una Terminal en JupyterLab e ingrese los siguientes comandos

```
git config --global user.name "<USER>"
git config --global user.email <CORREO>
```


### Paso 4: Clonar el Proyecto desde su propio Github

```
git clone https://github.com/<USER>/Clasificacion_tableros.git
```


### Paso 5: Instalar los pre-requisitos

```
cd Clasificacion_tableros/

pip install -r requirements.txt
```


### Paso 6: Ejecutar las pruebas en el entorno

```
cd src

python 1.Generar_data.py

python 2.CreacionModeloyEntrenamiento.py

python 3.Clasificacion.py

cd ..
```


### Paso 7: Guardar los cambios en el Repo

```
git add .

git commit -m "Pruebas Finalizadas"

git push

```

Ingrese su usuario y Personal Access Token de Github. Puede revisar que los cambios se hayan guardado en el repositorio. Luego, puede finalizar JupyterLab ("File" => "Shut Down").
