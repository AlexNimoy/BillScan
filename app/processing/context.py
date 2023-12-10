"""
Bключает в себя всю необходимую информацию 
для обработки изображений, такую как ссылки на изображения,
параметры обработки, метаданные и другие данные.
"""

class Context:
    def __init__(self, image_paths, processing_params, metadata):
        self.image_paths = image_paths
        self.processing_params = processing_params
        self.metadata = metadata
        self.results = {}
    
    def predicted_text(self):
        # Пример ответа сервиса
        example = {
                "File Name": "",
                "01 Receipt Number": "",
                "02 Receipt Date": "",
                "04 Counterparty": [
                    {
                    "04-01 Name": "",
                    "04-02 BIN": ""
                    }
                ],
                "05 Contract": "",
                "06 Our Company BIN": "",
                "07 Counterparty Bank": [
                    {
                    "07-01 Bank BIC": "",
                    "07-02 Current Account IIC": ""
                    }
                ],
                "09 Counterparty Payment Purpose Code": "",
                "10 Items Table": [
                    {
                    "10-01 Item": "",
                    "10-02 Unit": "",
                    "10-03 Quantity": "",
                    "10-04 Price": "",
                    "10-05 Amount": ""
                    }
                ]
                }
        return [example]