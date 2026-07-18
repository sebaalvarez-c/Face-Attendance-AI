CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    code VARCHAR(50) UNIQUE NOT NULL,
    role VARCHAR(50) NOT NULL DEFAULT 'student',
    face_encoding TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS attendance (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    attendance_date DATE NOT NULL DEFAULT CURRENT_DATE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(30) NOT NULL DEFAULT 'present',
    lat FLOAT NOT NULL,
    lng FLOAT NOT NULL,
    distance_meters FLOAT,
    CONSTRAINT uq_attendance_user_day UNIQUE (user_id, attendance_date)
);

CREATE INDEX IF NOT EXISTS ix_users_code ON users(code);
CREATE INDEX IF NOT EXISTS ix_attendance_user_id ON attendance(user_id);
CREATE INDEX IF NOT EXISTS ix_attendance_date ON attendance(attendance_date);
