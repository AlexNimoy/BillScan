"""
Содержит классы для предварительной обработки изображений,
такие как масштабирование, нормализация,
преобразование цветовой палитры и т.д.
"""

from app.processing.base_processor import BaseProcessor

class ImagePreprocessor(BaseProcessor):
    def process(self, context):
        # Логика предобработки изображения
        return context
