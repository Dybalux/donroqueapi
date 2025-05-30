# Forrajeria Don Roque Api

El objetivo es llevar el registro de las ventas del negocio.



## Authors

https://github.com/Dybalux [Luciano Emanuel Lagoria Villagran]

## Documentation


Primero abre la terminal, luego crear un entorno virtual para instalar las dependencias con virtual env

pip install virtualenv
virtualenv mi_entorno

Activar entorno virtual

.\mi_entorno\Scripts\activate

Luego hay que instalar los requerimientos:

pip install -r requirements.txt

Siguiente paso tener instalado docker. Levantamos el container:
docker compose up -d

Para iniciar el api se ejecuta el siguiente comando

fastapi dev main.py

Los endpoints pueden verse en el siguiente link:

http://127.0.0.1:8000/documentacion 

![image](https://github.com/user-attachments/assets/65f48b48-50d0-438b-9552-1523f0641ff4)
