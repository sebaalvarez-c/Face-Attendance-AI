# Face Attendance AI — DÍA 1 corregido

Este proyecto quedó preparado para cumplir el primer bloque crítico:

- Backend FastAPI funcional.
- Conexión PostgreSQL centralizada.
- Modelos reales: `users` y `attendance`.
- Endpoints principales:
  - `POST /register-user`
  - `POST /mark-attendance`
  - `GET /get-attendance`
  - `GET /users`
- Registro de asistencia guardado en BD.
- Validación GPS con radio configurable.
- Control de duplicado por usuario y día.
- Frontend base para registro, asistencia y dashboard.

## 1. Crear base de datos en PostgreSQL

En pgAdmin o psql crea:

```sql
CREATE DATABASE face_ai;
CREATE USER face_ai WITH PASSWORD 'faceai123';
GRANT ALL PRIVILEGES ON DATABASE face_ai TO face_ai;
```

Luego puedes ejecutar `database/init.sql`, aunque FastAPI también crea las tablas al iniciar.

## 2. Instalar dependencias

Desde la carpeta `backend`:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Ejecutar backend

Desde la carpeta `backend`:

```bash
uvicorn app.main:app --reload
```

Prueba en el navegador:

```text
http://127.0.0.1:8000/docs
```

## 4. Ejecutar frontend

Abre con Live Server o desde la carpeta `frontend`:

```bash
python -m http.server 5500
```

Luego entra a:

```text
http://127.0.0.1:5500/index.html
```

## Nota importante

El reconocimiento facial todavía está en modo base usando Haar Cascade y un encoding temporal `rostro_detectado`.
Eso es intencional para cerrar DÍA 1. En DÍA 3 se reemplaza por comparación facial real.
