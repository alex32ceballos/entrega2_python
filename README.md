## Clonar repo y entrar:
    ```bash
    git clone https://github.com/alex32ceballos/entrega2_python.git
    cd entrega2_python
    ```

## Como instalar las dependencias:

    1. Instalar la version 3.13.12 de python mediante pyenv:

    ```bash
    pyenv install 3.13.12
    ```

    En una terminal en el directorio ejecutar el siguiente comando:

    ```bash
    pyenv local 3.13.12
    ```

        - Que es pyenv y como instalarlo: https://realpython.com/intro-to-pyenv/  

    2. Crear el entorno virtual venv mediante la terminal dentro del directorio con el siguiente comando:

    ```bash
    python -m venv .venv
    ```

    Si no funciona se utiliza:

    ```bash
    python3 -m venv .venv
    ```

    Una vez creado, hay que entrar en el entorno mediante la terminal con el   siguiente comando: source .venv/bin/activate  
    Dentro, descargo todas las dependencias con:

    ```bash
    pip install -r requirements.txt
    ```

## Como ejecutar el programa:  
En una terminal dentro del directorio usar:

```bash
jupyter lab
```

Tirara dos links, copiar cualquiera de ellos y pegarlo en un navegador. Cuando carga,   hay que apretar la carpeta notebooks y luego el archivo llamado "prueba_ejercicios". De esta manera podras ejecutar el programa.  

## Autor:  
Apellido y nombre: Ceballos Alex.

Numero de estudiante: 027778/1
        
