# Inflex backend

## Instalación

Crear el entorno virtual:

```sh
python -m virtualenv venv 
```

Activar el entorno virtual:

```sh
source venv/bin/activate
```

Instalar los requisitos:

```sh
pip install -r requirements.txt
```

## Ejecución

Activar el entorno virtual antes de ejecutar la aplicación:

```sh
source venv/bin/activate
```

Para ejecutar la aplicación con Uvicorn:

```sh
uvicorn main:app --reload
```
