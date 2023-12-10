"""
Отвечает за валидацию входных данных, в частности изображений. 
Может включать проверку формата, размера, целостности данных и т.д.
"""

from app.processing.base_processor import BaseProcessor

class ImageValidator(BaseProcessor):
    def process(self, context):
        # Логика валидации изображения
        return context
