# Reglas de negocio del sistema de gestión de peluquería.

- Un cliente debe estar registrado antes de asignarle un turno.
- Un turno debe estar asociado a un cliente y un servicio.
- No se permite crear turnos sin datos completos.
- Los servicios deben existir antes de ser asignados a un turno.
- Los registros pueden ser modificados o eliminados según necesidad del sistema.

El sistema garantiza integridad de datos mediante el uso de claves y relaciones en SQLite.
