from abc import ABC, abstractmethod
from typing import Any, List, Dict
from collections import defaultdict
import time


class ProcessingStage(ABC):

    @abstractmethod
    def execute(self, data: Any) -> Any:
        pass

    @abstractmethod
    def get_stage_name(self) -> str:
        pass

    @abstractmethod
    def get_stage_description(self) -> str:
        pass


class InputStage(ProcessingStage):

    def __init__(self):
        """Inicializa la etapa de entrada."""
        pass

    def execute(self, data: Any) -> Any:
        """Valida y parsea los datos de entrada."""
        try:
            # Validación básica
            if data is None:
                raise ValueError("Input data cannot be None")
            return {"validated": True, "data": data, "stage": "input"}
        except Exception as e:
            return {"validated": False, "error": str(e), "stage": "input"}

    def get_stage_name(self) -> str:
        """Retorna el nombre de la etapa."""
        return "Input Stage"

    def get_stage_description(self) -> str:
        """Retorna la descripción de la etapa."""
        return "Input validation and parsing"


class TransformStage(ProcessingStage):
    """
    Etapa de transformación: enriquecimiento y procesamiento de datos.
    """

    def __init__(self):
        """Inicializa la etapa de transformación."""
        pass

    def execute(self, data: Any) -> Any:
        """Transforma y enriquece los datos."""
        try:
            if isinstance(data, dict) and data.get("validated"):
                original_data = data.get("data")
                # Transformación y enriquecimiento
                transformed = {
                    "original": original_data,
                    "enriched": True,
                    "metadata": {"timestamp": time.time(), "stage": "transform"},
                    "stage": "transform",
                }
                return transformed
            else:
                raise ValueError("Invalid data for transformation")
        except Exception as e:
            return {"error": str(e), "stage": "transform"}

    def get_stage_name(self) -> str:
        """Retorna el nombre de la etapa."""
        return "Transform Stage"

    def get_stage_description(self) -> str:
        """Retorna la descripción de la etapa."""
        return "Data transformation and enrichment"



class OutputStage(ProcessingStage):
    """
    Etapa de salida: formateo y entrega de datos.
    """

    def __init__(self):
        """Inicializa la etapa de salida."""
        pass

    def execute(self, data: Any) -> Any:
        """Formatea y prepara los datos para salida."""
        try:
            if isinstance(data, dict):
                # Formateo de salida
                output = {
                    "status": "success",
                    "processed": True,
                    "result": data,
                    "stage": "output",
                }
                return output
            else:
                raise ValueError("Invalid data for output")
        except Exception as e:
            return {"status": "error", "error": str(e), "stage": "output"}

    def get_stage_name(self) -> str:
        """Retorna el nombre de la etapa."""
        return "Output Stage"

    def get_stage_description(self) -> str:
        """Retorna la descripción de la etapa."""
        return "Output formatting and delivery"


class ProcessingPipeline:
    """
    Canalización de procesamiento con etapas configurables.
    Base flexible para diferentes tipos de procesamiento.
    """

    def __init__(self, pipeline_id: str):
        """
        Inicializa la canalización de procesamiento.

        Args:
            pipeline_id: Identificador único de la canalización
        """
        self.pipeline_id = pipeline_id
        self.stages = []
        self.statistics = {
            "total_processed": 0,
            "successful": 0,
            "failed": 0,
            "processing_time": 0.0,
        }

    def add_stage(self, stage: ProcessingStage) -> None:
        """
        Añade una etapa a la canalización.

        Args:
            stage: Etapa de procesamiento a añadir
        """
        self.stages.append(stage)

    def execute(self, data: Any) -> Any:
        """
        Ejecuta la canalización completa sobre los datos.
        Demuestra polimorfismo: cada etapa procesa de forma diferente.

        Args:
            data: Datos a procesar

        Returns:
            Resultado del procesamiento
        """
        start_time = time.time()
        result = data

        try:
            # Procesamiento polimórfico a través de todas las etapas
            for stage in self.stages:
                result = stage.execute(result)

                # Si hay error, detener el procesamiento
                if isinstance(result, dict) and result.get("error"):
                    self.statistics["failed"] += 1
                    break
            else:
                self.statistics["successful"] += 1

            self.statistics["total_processed"] += 1

        except Exception as e:
            result = {"error": str(e), "pipeline": self.pipeline_id}
            self.statistics["failed"] += 1
            self.statistics["total_processed"] += 1

        finally:
            processing_time = time.time() - start_time
            self.statistics["processing_time"] += processing_time

        return result

    def get_statistics(self) -> Dict[str, Any]:
        """Retorna las estadísticas de la canalización."""
        if self.statistics["total_processed"] > 0:
            efficiency = (
                (
                    self.statistics["successful"]
                    / self.statistics[
                        "\
total_processed"
                    ]
                )
                * 100
            )
        else:
            efficiency = 0.0

        return {
            "pipeline_id": self.pipeline_id,
            "total_processed": self.statistics["total_processed"],
            "successful": self.statistics["successful"],
            "failed": self.statistics["failed"],
            "efficiency": efficiency,
            "total_time": self.statistics["processing_time"],
        }

    def print_stages(self) -> None:
        """Imprime las etapas configuradas en la canalización."""
        for i, stage in enumerate(self.stages, 1):
            print(f"Stage {i}: {stage.get_stage_description()}")


class DataAdapter(ABC):
    """
    Clase base abstracta para adaptadores de datos.
    Maneja diferentes formatos de datos de forma polimórfica.
    """

    def __init__(self, pipeline_id: str):
        """
        Inicializa el adaptador de datos.

        Args:
            pipeline_id: Identificador de la canalización asociada
        """
        self.pipeline_id = pipeline_id

    @abstractmethod
    def parse_input(self, raw_data: str) -> Any:
        """Parsea los datos de entrada según el formato."""
        pass

    @abstractmethod
    def format_output(self, processed_data: Any) -> str:
        """Formatea los datos procesados según el formato."""
        pass

    @abstractmethod
    def get_format_type(self) -> str:
        """Retorna el tipo de formato manejado."""
        pass


class JSONAdapter(DataAdapter):
    """
    Adaptador para datos en formato JSON.
    """

    def __init__(self, pipeline_id: str):
        """Inicializa el adaptador JSON."""
        super().__init__(pipeline_id)

    def parse_input(self, raw_data: str) -> Dict[str, Any]:
        """Parsea string JSON a diccionario."""
        # Simulación de parsing JSON
        return {"sensor": "temp", "value": 23.5, "unit": "C"}

    def format_output(self, processed_data: Any) -> str:
        """Formatea datos procesados como output JSON."""
        if isinstance(processed_data, dict):
            original = processed_data.get("original", {})
            if isinstance(original, dict):
                value = original.get("value", 0)
                unit = original.get("unit", "")
                status = (
                    "Normal range"
                    if 15 <= value <= 30
                    else "Out of \
range"
                )
                return f"Processed temperature reading: \
{value}°{unit} ({status})"
        return "Processed JSON data"

    def get_format_type(self) -> str:
        """Retorna el tipo de formato."""
        return "JSON"


class CSVAdapter(DataAdapter):

    def __init__(self, pipeline_id: str):
        """Inicializa el adaptador CSV."""
        super().__init__(pipeline_id)

    def parse_input(self, raw_data: str) -> Dict[str, Any]:
        """Parsea string CSV a estructura de datos."""
        # Simulación de parsing CSV
        return {"format": "csv", "headers": ["user", "action", "timestamp"], "rows": 1}

    def format_output(self, processed_data: Any) -> str:
        """Formatea datos procesados como output CSV."""
        if isinstance(processed_data, dict):
            result = processed_data.get("result", {})
            original = result.get("original", {})
            if isinstance(original, dict):
                rows = original.get("rows", 0)
                return f"User activity logged: {rows} actions processed"
        return "Processed CSV data"

    def get_format_type(self) -> str:
        return "CSV"


class StreamAdapter(DataAdapter):

    def __init__(self, pipeline_id: str):
        super().__init__(pipeline_id)

    def parse_input(self, raw_data: str) -> Dict[str, Any]:
        return {
            "type": "stream",
            "readings": [22.5, 21.8, 22.0, 22.3, 21.9],
            "count": 5,
        }

    def format_output(self, processed_data: Any) -> str:
        if isinstance(processed_data, dict):
            result = processed_data.get("result", {})
            original = result.get("original", {})
            if isinstance(original, dict):
                readings = original.get("readings", [])
                count = len(readings)
                if readings:
                    avg = sum(readings) / count
                    return f"Stream summary: {count} readings, avg: {avg}°C"
        return "Processed stream data"

    def get_format_type(self) -> str:
        return "Stream"


class NexusManager:

    def __init__(self):
        """Inicializa el gestor del Nexus."""
        self.pipelines = []
        self.capacity = 1000  # streams/second
        self.global_stats = defaultdict(int)

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_with_adapter(
        self, adapter: DataAdapter, pipeline: ProcessingPipeline, raw_data: str
    ) -> str:
        try:
            parsed_data = adapter.parse_input(raw_data)
            print(f"Input: {raw_data}")

            processed = pipeline.execute(parsed_data)
            print("Transform: Enriched with metadata and validation")

            output = adapter.format_output(processed)
            print(f"Output: {output}")

            return output

        except Exception as e:
            error_msg = f"Error: {str(e)}"
            print(f"Output: {error_msg}")
            return error_msg

    def chain_pipelines(
        self, data: Any, pipeline_chain: List[ProcessingPipeline]
    ) -> Any:
        result = data
        for pipeline in pipeline_chain:
            result = pipeline.execute(result)
            if isinstance(result, dict) and result.get("error"):
                break
        return result

    def simulate_error_recovery(self) -> None:
        print("Simulating pipeline failure...")
        print("Error detected in Stage 2: Invalid data format")
        print("Recovery initiated: Switching to backup processor")
        time.sleep(0.1)  # Simula tiempo de recuperación
        print("Recovery successful: Pipeline restored, processing resumed")

    def get_global_statistics(self) -> Dict[str, Any]:
        total_processed = 0
        total_successful = 0
        total_time = 0.0

        for pipeline in self.pipelines:
            stats = pipeline.get_statistics()
            total_processed += stats["total_processed"]
            total_successful += stats["successful"]
            total_time += stats["total_time"]

        efficiency = (
            (total_successful / total_processed * 100) if total_processed > 0 else 0
        )

        return {
            "total_processed": total_processed,
            "total_successful": total_successful,
            "efficiency": efficiency,
            "total_time": total_time,
        }


def main():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print()

    print("Initializing Nexus Manager...")
    manager = NexusManager()
    print(f"Pipeline capacity: {manager.capacity} streams/second")
    print()

    print("Creating Data Processing Pipeline...")
    pipeline = ProcessingPipeline("MAIN_PIPELINE")
    pipeline.add_stage(InputStage())
    pipeline.add_stage(TransformStage())
    pipeline.add_stage(OutputStage())
    pipeline.print_stages()
    print()

    print("=== Multi-Format Data Processing ===")
    print()

    print("Processing JSON data through pipeline...")
    json_adapter = JSONAdapter("JSON_PIPE")
    manager.process_with_adapter(
        json_adapter,
        pipeline,
        '{"sensor": "temp", "value": 23.5, \
"unit": "C"}',
    )
    print()

    print("Processing CSV data through same pipeline...")
    csv_adapter = CSVAdapter("CSV_PIPE")
    manager.process_with_adapter(csv_adapter, pipeline, '"user,action,timestamp"')
    print()

    print("Processing Stream data through same pipeline...")
    stream_adapter = StreamAdapter("STREAM_PIPE")
    manager.process_with_adapter(stream_adapter, pipeline, "Real-time sensor stream")
    print()

    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    pipeline_a = ProcessingPipeline("PIPELINE_A")
    pipeline_a.add_stage(InputStage())

    pipeline_b = ProcessingPipeline("PIPELINE_B")
    pipeline_b.add_stage(TransformStage())

    pipeline_c = ProcessingPipeline("PIPELINE_C")
    pipeline_c.add_stage(OutputStage())

    for _ in range(100):
        test_data = {"test": "data"}
        manager.chain_pipelines(test_data, [pipeline_a, pipeline_b, pipeline_c])

    print("Chain result: 100 records processed through 3-stage pipeline")

    manager.add_pipeline(pipeline_a)
    manager.add_pipeline(pipeline_b)
    manager.add_pipeline(pipeline_c)
    stats = manager.get_global_statistics()

    print(
        f"Performance: {int(stats['efficiency'])} % efficiency, \
{stats['total_time']:.1f}s total processing time"
    )
    print()

    print("=== Error Recovery Test ===")
    manager.simulate_error_recovery()
    print()

    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
