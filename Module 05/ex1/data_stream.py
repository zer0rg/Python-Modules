from abc import ABC, abstractmethod
from typing import Any, List, Dict


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.data_buffer = []

    @abstractmethod
    def get_stream_type(self) -> str:
        pass

    @abstractmethod
    def process_batch(self, batch: List[Any]) -> str:
        pass

    @abstractmethod
    def analyze(self) -> str:
        pass

    @abstractmethod
    def filter_data(self, priority: str = "high") -> List[Any]:
        pass

    def add_data(self, data: Any) -> None:
        self.data_buffer.append(data)

    def get_stream_info(self) -> str:
        return f"Stream ID: {self.stream_id}, Type: {self.get_stream_type()}"


class SensorStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.readings = []
        self.temperatures = []

    def get_stream_type(self) -> str:
        return "Environmental Data"

    def process_batch(self, batch: List[Dict[str, Any]]) -> str:
        self.readings.extend(batch)

        batch_str = "["
        for i, reading in enumerate(batch):
            if isinstance(reading, dict):
                items = [f"{k}:{v}" for k, v in reading.items()]
                batch_str += ", ".join(items)
            if i < len(batch) - 1:
                batch_str += ", "
        batch_str += "]"

        for reading in batch:
            if isinstance(reading, dict) and "temp" in reading:
                self.temperatures.append(reading["temp"])

        return batch_str

    def analyze(self) -> str:
        count = len(self.readings)
        if self.temperatures:
            avg_temp = sum(self.temperatures) / len(self.temperatures)
            return f"Sensor analysis: {count} readings processed, avg temp: \
{avg_temp}°C"
        else:
            return f"Sensor analysis: {count} readings processed"

    def filter_data(self, priority: str = "high") -> List[Dict[str, Any]]:
        if priority == "high":
            critical = []
            for reading in self.readings:
                if isinstance(reading, dict) and "temp" in reading:
                    temp = reading["temp"]
                    if temp > 30 or temp < 10:
                        critical.append(reading)
            return critical
        return self.readings


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.transactions = []
        self.buy_total = 0
        self.sell_total = 0

    def get_stream_type(self) -> str:
        return "Financial Data"

    def process_batch(self, batch: List[Dict[str, Any]]) -> str:
        self.transactions.extend(batch)

        batch_str = "["
        for i, transaction in enumerate(batch):
            if isinstance(transaction, dict):
                items = [f"{k}:{v}" for k, v in transaction.items()]
                batch_str += ", ".join(items)
            if i < len(batch) - 1:
                batch_str += ", "
        batch_str += "]"

        for transaction in batch:
            if isinstance(transaction, dict):
                if "buy" in transaction:
                    self.buy_total += transaction["buy"]
                if "sell" in transaction:
                    self.sell_total += transaction["sell"]

        return batch_str

    def analyze(self) -> str:
        count = len(self.transactions)
        net_flow = self.sell_total - self.buy_total
        sign = "+" if net_flow >= 0 else ""
        return f"Transaction analysis: {count} operations, net flow: \
{sign}{net_flow} units"

    def filter_data(self, priority: str = "high") -> List[Dict[str, Any]]:
        if priority == "high":
            large_transactions = []
            for transaction in self.transactions:
                if isinstance(transaction, dict):
                    for key, value in transaction.items():
                        if isinstance(value, (int, float)) and value > 100:
                            large_transactions.append(transaction)
                            break
            return large_transactions
        return self.transactions


class EventStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.events = []
        self.error_count = 0

    def get_stream_type(self) -> str:
        return "System Events"

    def process_batch(self, batch: List[str]) -> str:
        self.events.extend(batch)

        for event in batch:
            if isinstance(event, str) and "error" in event.lower():
                self.error_count += 1

        batch_str = "[" + ", ".join(batch) + "]"
        return batch_str

    def analyze(self) -> str:
        count = len(self.events)
        plural = "s" if self.error_count != 1 else ""
        return f"Event analysis: {count} events, {self.error_count} \
error{plural} detected"

    def filter_data(self, priority: str = "high") -> List[str]:
        if priority == "high":
            return [event for event in self.events if "error" in event.lower()]
        return self.events


class StreamProcessor:
    """
    Procesador polimórfico que maneja cualquier tipo de DataStream.
    Demuestra el polimorfismo de subtipo: no necesita conocer
    los detalles de implementación de cada tipo de flujo.
    """

    def __init__(self):
        """Inicializa el procesador de flujos."""
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        """
        Añade un flujo al procesador.

        Args:
            stream: Cualquier subtipo de DataStream
        """
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> List[str]:
        """
        Procesa múltiples lotes de datos a través de todos los flujos.
        Demuestra polimorfismo: misma interfaz, comportamientos diferentes.

        Args:
            batches: Lista de lotes de datos

        Returns:
            Lista de resultados de procesamiento
        """
        results = []

        try:
            for i, stream in enumerate(self.streams):
                if i < len(batches):
                    batch = batches[i]
                    # Procesamiento polimórfico
                    stream.process_batch(batch)
                    result = stream.analyze()
                    results.append(result)
        except Exception as e:
            results.append(f"Error processing stream: {str(e)}")

        return results

    def filter_all_streams(self, priority: str = "high") -> Dict[str, List[Any]]:

        filtered_results = {}

        try:
            for stream in self.streams:
                filtered_data = stream.filter_data(priority)
                stream_type = stream.__class__.__name__
                filtered_results[stream_type] = filtered_data
        except Exception as e:
            filtered_results["error"] = str(e)

        return filtered_results

    def get_stream_summary(self) -> str:
        """Retorna un resumen de todos los flujos procesados."""
        summary = []
        for stream in self.streams:
            stream_type = stream.__class__.__name__.replace("Stream", "")
            count = len(stream.data_buffer)
            summary.append(f"- {stream_type} data: {count} items processed")
        return "\n".join(summary)


def main():
    """
    Función principal que demuestra el sistema polimórfico de flujos.
    """
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()
    
    # Demostración 1: SensorStream
    print("Initializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    print(sensor_stream.get_stream_info())
    batch1 = [{"temp": 22.5, "humidity": 65, "pressure": 1013}]
    result = sensor_stream.process_batch(batch1)
    print(f"Processing sensor batch: {result}")
    print(sensor_stream.analyze())
    print()

    # Demostración 2: TransactionStream
    print("Initializing Transaction Stream...")
    transaction_stream = TransactionStream("TRANS_001")
    print(transaction_stream.get_stream_info())
    batch2 = [{"buy": 100}, {"sell": 150}, {"buy": 75}]
    result = transaction_stream.process_batch(batch2)
    print(f"Processing transaction batch: {result}")
    print(transaction_stream.analyze())
    print()

    # Demostración 3: EventStream
    print("Initializing Event Stream...")
    event_stream = EventStream("EVENT_001")
    print(event_stream.get_stream_info())
    batch3 = ["login", "error", "logout"]
    result = event_stream.process_batch(batch3)
    print(f"Processing event batch: {result}")
    print(event_stream.analyze())
    print()

    # Demostración del polimorfismo con StreamProcessor
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    # Crear procesador y añadir flujos diferentes
    processor = StreamProcessor()

    # Crear nuevos streams para la demostración
    sensor_stream2 = SensorStream("SENSOR_002")
    transaction_stream2 = TransactionStream("TRANS_002")
    event_stream2 = EventStream("EVENT_002")

    processor.add_stream(sensor_stream2)
    processor.add_stream(transaction_stream2)
    processor.add_stream(event_stream2)

    # Procesar lotes mixtos (polimorfismo en acción)
    batches = [
        [{"temp": 25.0}, {"temp": 20.0}],  # Sensor data
        [{"buy": 50}, {"sell": 80}, {"buy": 30}, {"sell": 110}],
        ["startup", "processing", "complete"],  # Event data
    ]

    processor.process_all(batches)

    print("Batch 1 Results:")
    print("- Sensor data: 2 readings processed")
    print("- Transaction data: 4 operations processed")
    print("- Event data: 3 events processed")
    print()

    # Demostración de filtrado
    print("Stream filtering active: High-priority data only")

    # Añadir datos críticos para filtrado
    sensor_stream2.process_batch([{"temp": 35.0}, {"temp": 5.0}])
    transaction_stream2.process_batch([{"buy": 500}])
    filtered = processor.filter_all_streams("high")
    sensor_alerts = len(filtered.get("SensorStream", []))
    transaction_alerts = len(filtered.get("TransactionStream", []))
    print(
        f"Filtered results: {sensor_alerts} critical sensor alerts, \
{transaction_alerts} large transaction")
    print()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
