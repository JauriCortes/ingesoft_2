# Ejemplos de patrones

Este directorio contiene un ejemplo simple en Python que cubre los cuatro puntos pedidos:

1. `Singleton`: `AppConfig` asegura una sola instancia compartida.
2. `Patron creacional aparte`: `ReportFactory` implementa `Factory Method`.
3. `Creacional + estructural`: `StorageFactory` crea servicios y `LegacyDiskAdapter` adapta un sistema legado.
4. `Creacional + estructural + comportamiento`: `NotifierFactory` crea notificadores, `AuditDecorator` agrega funcionalidad y `DeliveryStrategy` cambia la forma de envio.

## Ejecutar

```bash
python3 patrones/patrones_demo.py
```
