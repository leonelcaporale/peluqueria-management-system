# Modelo de base de datos del sistema de gestión de peluquería.

El sistema utiliza SQLite como base de datos relacional.

🔹 Tablas principales:

- Clientes
  Contiene los datos de los clientes registrados.

- Servicios
  Contiene los servicios disponibles en la peluquería.

- Turnos
  Relaciona clientes y servicios mediante claves foráneas.

🔹 Relaciones:

- Un cliente puede tener muchos turnos.
- Un servicio puede estar asociado a múltiples turnos.
- La tabla turnos conecta clientes y servicios.

🔹 Consultas utilizadas:

- SELECT: consulta de datos
- INSERT: agregar registros
- UPDATE: modificar registros
- DELETE: eliminar registros
- JOIN: unión de tablas clientes y servicios
