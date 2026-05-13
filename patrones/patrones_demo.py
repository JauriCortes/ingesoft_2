from __future__ import annotations

from abc import ABC, abstractmethod


class AppConfig:
    _instance: "AppConfig | None" = None

    def __new__(cls) -> "AppConfig":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.environment = "desarrollo"
        return cls._instance


class Report(ABC):
    @abstractmethod
    def render(self) -> str:
        raise NotImplementedError


class PdfReport(Report):
    def render(self) -> str:
        return "Reporte en PDF"


class ExcelReport(Report):
    def render(self) -> str:
        return "Reporte en Excel"


class ReportFactory:
    @staticmethod
    def create(report_type: str) -> Report:
        if report_type == "pdf":
            return PdfReport()
        if report_type == "excel":
            return ExcelReport()
        raise ValueError(f"Tipo de reporte no soportado: {report_type}")


class StorageService(ABC):
    @abstractmethod
    def save(self, file_name: str) -> str:
        raise NotImplementedError


class CloudStorage(StorageService):
    def save(self, file_name: str) -> str:
        return f"Archivo {file_name} guardado en la nube"


class LegacyDiskSystem:
    def write_file(self, path: str) -> str:
        return f"Archivo {path} guardado en disco local"


class LegacyDiskAdapter(StorageService):
    def __init__(self, legacy_disk: LegacyDiskSystem) -> None:
        self.legacy_disk = legacy_disk

    def save(self, file_name: str) -> str:
        return self.legacy_disk.write_file(file_name)


class StorageFactory:
    @staticmethod
    def create(storage_type: str) -> StorageService:
        if storage_type == "cloud":
            return CloudStorage()
        if storage_type == "legacy":
            return LegacyDiskAdapter(LegacyDiskSystem())
        raise ValueError(f"Tipo de almacenamiento no soportado: {storage_type}")


class DeliveryStrategy(ABC):
    @abstractmethod
    def deliver(self, message: str) -> str:
        raise NotImplementedError


class EmailStrategy(DeliveryStrategy):
    def deliver(self, message: str) -> str:
        return f"Enviado por email: {message}"


class SmsStrategy(DeliveryStrategy):
    def deliver(self, message: str) -> str:
        return f"Enviado por SMS: {message}"


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        raise NotImplementedError


class BasicNotifier(Notifier):
    def __init__(self, strategy: DeliveryStrategy) -> None:
        self.strategy = strategy

    def send(self, message: str) -> str:
        return self.strategy.deliver(message)


class NotifierDecorator(Notifier):
    def __init__(self, wrapped: Notifier) -> None:
        self.wrapped = wrapped


class AuditDecorator(NotifierDecorator):
    def send(self, message: str) -> str:
        audited_message = f"[audit] {message}"
        return self.wrapped.send(audited_message)


class NotifierFactory:
    @staticmethod
    def create(channel: str, audited: bool = False) -> Notifier:
        if channel == "email":
            notifier: Notifier = BasicNotifier(EmailStrategy())
        elif channel == "sms":
            notifier = BasicNotifier(SmsStrategy())
        else:
            raise ValueError(f"Canal no soportado: {channel}")

        if audited:
            notifier = AuditDecorator(notifier)

        return notifier


def singleton_example() -> None:
    first_config = AppConfig()
    second_config = AppConfig()
    second_config.environment = "produccion"

    print("1. Singleton")
    print(f"IDs iguales: {id(first_config) == id(second_config)}")
    print(f"Ambos apuntan a environment = {first_config.environment}")
    print()


def creational_example() -> None:
    report = ReportFactory.create("pdf")

    print("2. Patron creacional aparte: Factory Method")
    print(report.render())
    print()


def creational_structural_example() -> None:
    cloud_storage = StorageFactory.create("cloud")
    legacy_storage = StorageFactory.create("legacy")

    print("3. Combinacion creacional + estructural")
    print(cloud_storage.save("arquitectura.png"))
    print(legacy_storage.save("respaldo.zip"))
    print("Factory Method crea el servicio y Adapter unifica la API del sistema legado.")
    print()


def all_categories_example() -> None:
    email_notifier = NotifierFactory.create("email", audited=True)
    sms_notifier = NotifierFactory.create("sms")

    print("4. Combinacion de los tres tipos")
    print(email_notifier.send("Servidor estable"))
    print(sms_notifier.send("Incidente critico"))
    print("Factory Method crea el notificador, Decorator agrega auditoria y Strategy define el canal.")
    print()


def main() -> None:
    singleton_example()
    creational_example()
    creational_structural_example()
    all_categories_example()


if __name__ == "__main__":
    main()
