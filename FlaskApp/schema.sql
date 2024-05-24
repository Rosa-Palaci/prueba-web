DROP TABLE IF EXISTS estudiante;
DROP TABLE IF EXISTS maestros;
DROP TABLE IF EXISTS partida;
DROP TABLE IF EXISTS nivel;
DROP TABLE IF EXISTS escenario;
DROP TABLE IF EXISTS admin;

CREATE TABLE estudiante (
    idEstudiante INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_lista INTEGER NOT NULL,
    grupo VARCHAR(50) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    ciclo_escolar VARCHAR(50) NOT NULL
);

CREATE TABLE maestros (
    idMaestro INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE nivel (
    idNivel INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255),
    escenario VARCHAR(255)
);

CREATE TABLE escenario (
    idEscenario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombreEscenario VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255)
);

CREATE TABLE partida (
    idPartida INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(255) NOT NULL,
    idEstudiante INTEGER NOT NULL,
    idNivel INTEGER NOT NULL,
    puntaje INTEGER,
    fecha_jugada VARCHAR(255),
    minutos_jugados INTEGER,
    FOREIGN KEY (idEstudiante) REFERENCES estudiante (idEstudiante),
    FOREIGN KEY (idNivel) REFERENCES nivel (idNivel)
);

CREATE TABLE admin (
    idAdmin INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
