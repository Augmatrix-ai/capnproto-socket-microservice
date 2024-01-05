from typing import Dict, Union
from operations import digitized_pdf_ocr
import json

class OCRTask:
    # self.properties (Dict): A dictionary containing properties from block configrations.
    # self.credentials (Dict): A dictionary containing authentication credentials from block configurations.
    
    def __init__(self, properties: Dict, credentails: Dict, logger: object) -> None:
        """
        Initialize OCR Task object.

        Parameters:
        
        logger (oject): A logger object to log messages and errors.
        """
        self.properties = properties
        self.credentails = credentails
        self.logger = logger
        super().__init__()

    def run(self, pdf: bytes) -> Dict:
        """
        Perform OCR on an pdf.

        Parameters:
        pdf (bytes): A bytes object containing the input pdf data.

        Returns:
        Dict: A dictionary containing the OCR results.
            The keys are "ocr_json" and "raw_text", and the values are the OCR data (Dict) and raw text (str),
            respectively.
        """

        ocr_engine = digitized_pdf_ocr.DigitizedPDFOCR()
        ocr_engine.perform(pdf)
        ocr_json = ocr_engine.ocrinfo
        raw_text = ocr_engine.raw_text

        return {"ocrJson": json.dumps(ocr_json), "rawText": raw_text}