"""
Содержит логику, которая определяет порядок 
и способ взаимодействия обработчиков 
в вашем приложении.
"""

from app.processing.postprocessors import PostProcessor
from app.processing.predictors import NeuralNetworkPredictor
from app.processing.preprocessors import ImagePreprocessor
from app.processing.validators import ImageValidator

class Pipeline:
    def __init__(self):
        self.pipeline = [
            ImageValidator(),
            ImagePreprocessor(),
            NeuralNetworkPredictor(),
            PostProcessor()
        ]

    def run(self, context):
        for processor in self.pipeline:
            context = processor.process(context)
        return context
