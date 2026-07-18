# Face Attendance AI 🤖

Sistema inteligente de control de asistencia desarrollado con Inteligencia Artificial, utilizando reconocimiento facial, análisis de emociones, reconocimiento de voz y validación mediante ubicación GPS.

El objetivo del proyecto es automatizar el registro de asistencia mediante una cámara web, permitiendo identificar usuarios registrados y almacenar la información en una base de datos PostgreSQL.

---

#  Descripción del proyecto

Face Attendance AI es una aplicación web que permite controlar la asistencia de usuarios mediante diferentes tecnologías de inteligencia artificial.

El sistema realiza:

- Captura de rostro mediante cámara web.
- Reconocimiento facial mediante comparación de características biométricas.
- Identificación automática del usuario registrado.
- Análisis de emociones mediante modelos de IA.
- Validación de voz como método adicional.
- Validación de ubicación mediante GPS.
- Registro de asistencia en PostgreSQL.
- Visualización de datos mediante un dashboard.


---

#  Características principales

##  Registro de usuarios

El sistema permite registrar nuevos usuarios mediante:

- Nombre completo.
- Rol del usuario.
- Captura facial mediante cámara.
- Generación de características faciales.

La información del usuario queda almacenada en la base de datos.


---

##  Reconocimiento facial

El sistema utiliza Inteligencia Artificial para identificar usuarios.

Proceso:

1. La cámara captura una imagen.
2. Se detecta el rostro.
3. Se genera un embedding facial.
4. Se compara con los usuarios registrados.
5. Si existe coincidencia, se identifica al usuario.


---

##  Reconocimiento de emociones

El sistema analiza la expresión facial del usuario mediante un modelo de inteligencia artificial.

Permite detectar estados emocionales como:

- Happy
- Sad
- Angry
- Fear
- Neutral
- Surprise


---

##  Reconocimiento de voz

Como validación adicional, el sistema incorpora reconocimiento de voz.

El usuario puede utilizar una frase de confirmación para complementar el proceso de asistencia.


---

##  Validación GPS

El sistema verifica que el usuario se encuentre dentro del área permitida.

Características:

- Obtención de coordenadas.
- Cálculo de distancia.
- Validación mediante radio permitido.


---

## Dashboard

Cuenta con un panel donde se puede visualizar:

- Usuarios registrados.
- Asistencias realizadas.
- Fecha de registro.
- Estado de asistencia.
- Historial.


---

# Arquitectura del sistema
              Usuario
                |
                |
          Cámara Web
                |
                |
          Frontend Web
      HTML + JavaScript
                |
                |
          API REST FastAPI
                |
             | | | |
Reconocimiento Emociones Voz GPS
Facial IA IA Validación
                |
                |
          PostgreSQL
                |
                |
    Usuarios y registros asistencia

---

# Tecnologías utilizadas


## Backend

- Python 3
- FastAPI
- SQLAlchemy
- PostgreSQL
- OpenCV
- TensorFlow
- Deep Learning
- Librerías de reconocimiento facial
- Librerías de reconocimiento de voz


## Frontend

- HTML5
- JavaScript
- Tailwind CSS


## Base de datos

- PostgreSQL


---

# Estructura del proyecto
Face-Attendance-AI
│
├── backend
│ │
│ ├── app
│ │ ├── ia
│ │ │ └── face_engine.py
│ │ │
│ │ ├── routes
│ │ │ ├── attendance.py
│ │ │ ├── auth_routes.py
│ │ │ └── user.py
│ │ │
│ │ ├── database.py
│ │ ├── models.py
│ │ ├── schemas.py
│ │ ├── face_recognition_module.py
│ │ ├── emotion_recognition.py
│ │ ├── voice_recognition.py
│ │ ├── geo_validation.py
│ │ └── main.py
│ │
│ ├── requirements.txt
│
├── database
│ └── init.sql
│
├── frontend
│ │
│ ├── index.html
│ ├── register.html
│ ├── login.html
│ ├── dashboard.html
│ │
│ └── assets
│ └── js
│ ├── api.js
│ ├── camera.js
│ └── auth.js
│
└── README.md


---

# ⚙️ Instalación


## 1. Clonar repositorio


```bash
git clone https://github.com/sebaalvarez-c/Face-Attendance-AI.git
cd Face-Attendance-AI

## Configuración Backend

Ingresar a backend:

cd backend

Crear entorno virtual:

python -m venv venv

Activar entorno virtual:

Windows:

venv\Scripts\activate

Instalar dependencias:

pip install -r requirements.txt

## Configuración PostgreSQL

Crear base de datos:

CREATE DATABASE face_ai;

Ejecutar el script:

database/init.sql

Configurar las credenciales en:

backend/config.py
## Ejecutar Backend

Desde la carpeta backend:

uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

Servidor disponible:

http://127.0.0.1:8000

Documentación automática:

http://127.0.0.1:8000/docs
## Ejecutar Frontend

Abrir la carpeta:

frontend

Ejecutar mediante Live Server de Visual Studio Code.

Página principal:

index.html
## Endpoints principales
Usuarios

Registrar usuario:

POST /register-user

Obtener usuarios:

GET /users
Asistencia

Registrar asistencia:

POST /mark-attendance

Consultar asistencias:

GET /get-attendance
## Funcionamiento de seguridad

El sistema no utiliza fotografías almacenadas como método principal de identificación.

Las imágenes capturadas son procesadas mediante Inteligencia Artificial para obtener características matemáticas del rostro llamadas embeddings.

Estos datos permiten comparar usuarios sin necesidad de guardar fotografías completas.

## Objetivo del proyecto

Desarrollar un sistema inteligente capaz de automatizar el control de asistencia utilizando tecnologías modernas de Inteligencia Artificial, reduciendo errores humanos y mejorando la seguridad del proceso.

## Autor

Sebastian Alvarez

Proyecto académico:

Face Attendance AI

Año: 2026