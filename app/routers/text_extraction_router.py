# text_extraction_router.py
from fastapi import UploadFile, File
from typing import List
from ..processing.context import Context
from ..processing.pipeline import Pipeline
from .base_router import BaseRouter

router = BaseRouter()

@router.post("/v1/extract_text/")
async def extract_text_from_image(files: List[UploadFile] = File(...)):
    file_names = [file.filename for file in files]
    # Логика обработки изображения и извлечения текста
    context = Context(file_names, {}, {})

    # Запуск пайплайна
    pipeline = Pipeline()
    result = pipeline.run(context)

    return { "results": result.predicted_text() }
