"""
Постобработка результатов, 
форматирование выходных данных 
и отправка результатов клиенту.
"""

from app.processing.base_processor import BaseProcessor

class PostProcessor(BaseProcessor):
    def process(self, context):
        # Логика постобработки результатов
        return context
