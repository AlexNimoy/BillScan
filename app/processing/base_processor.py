"""
Базовый класс для всех обработчиков в конвейере. 
Каждый обработчик должен наследоваться 
от этого класса и реализовывать метод process.
"""

class BaseProcessor:
    def process(self, context):
        raise NotImplementedError("Each processor must implement the 'process' method.")
