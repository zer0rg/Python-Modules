from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def format_output(self, processed_result: str) -> str:
        pass

    def execute(self, data: Any) -> str:
        try:
            if isinstance(data, str):
                print(f'Processing data: "{data}"')
            else:
                print(f"Processing data: {data}")
            if self.validate(data):
                print(f"Validation: {self._get_validation_message()}")

                result = self.process(data)
                output = self.format_output(result)

                print(f"Output: {output}")
                return output
            else:
                error_msg = f"Validation failed: Invalid data for \
{self.__class__.__name__}"
                print(f"Output: {error_msg}")
                return error_msg
        except Exception as e:
            error_msg = f"Error processing data: {str(e)}"
            print(f"Output: {error_msg}")
            return error_msg

    @abstractmethod
    def _get_validation_message(self) -> str:
        pass


class NumericProcessor(DataProcessor):
    def __init__(self):
        pass

    def validate(self, data: Any) -> bool:
        if not isinstance(data, (list, tuple)):
            return False
        if not data:
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: List[Union[int, float]]) -> str:
        count = len(data)
        total = sum(data)
        average = total / count
        return f"{count},{total},{average}"

    def format_output(self, processed_result: str) -> str:
        count, total, avg = processed_result.split(",")
        return f"Processed {count} numeric values, sum={total}, avg={avg}"

    def _get_validation_message(self) -> str:
        return "Numeric data verified"


class TextProcessor(DataProcessor):
    def __init__(self):
        pass

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data) > 0

    def process(self, data: str) -> str:
        char_count = len(data)
        word_count = len(data.split())
        return f"{char_count},{word_count}"

    def format_output(self, processed_result: str) -> str:
        char_count, word_count = processed_result.split(",")
        return f"Processed text: {char_count} characters, {word_count} words"

    def _get_validation_message(self) -> str:
        return "Text data verified"


class LogProcessor(DataProcessor):
    def __init__(self):
        pass

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        log_levels = ["ERROR", "WARNING", "INFO", "DEBUG"]
        return any(level in data.upper() for level in log_levels)

    def process(self, data: str) -> str:
        data_upper = data.upper()

        level = None
        for log_level in ["ERROR", "WARNING", "INFO", "DEBUG"]:
            if log_level in data_upper:
                level = log_level
                break

        if ":" in data:
            message = data.split(":", 1)[1].strip()
        else:
            message = data

        return f"{level},{message}"

    def format_output(self, processed_result: str) -> str:
        level, message = processed_result.split(",", 1)

        if level == "ERROR":
            return f"[ALERT] {level} level detected: {message}"
        else:
            return f"[{level}] {level} level detected: {message}"

    def _get_validation_message(self) -> str:
        return "Log entry verified"


def demonstrate_polymorphism():
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors_data = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello Nexus!"),
        (LogProcessor(), "INFO: System ready"),
    ]

    for i, (processor, data) in enumerate(processors_data, 1):
        result = processor.process(data)
        output = processor.format_output(result)
        print(f"Result {i}: {output}")


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()

    # Demonstracion NumericProcessor
    print("Initializing Numeric Processor...")
    numeric_processor = NumericProcessor()
    numeric_processor.execute([1, 2, 3, 4, 5])
    print()

    # Demonstracion TextProcessor
    print("Initializing Text Processor...")
    text_processor = TextProcessor()
    text_processor.execute("Hello Nexus World")
    print()

    # Demostración LogProcessor
    print("Initializing Log Processor...")
    log_processor = LogProcessor()
    log_processor.execute("ERROR: Connection timeout")
    print()

    # Demostracion polimorfismo
    demonstrate_polymorphism()
    print()

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
