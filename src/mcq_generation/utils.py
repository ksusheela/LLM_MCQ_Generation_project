import os
import PyPDF2
import json
import traceback
from src.mcq_generation.log import logger
import pandas as pd

def read_file(file):
    try:
        if file.name.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        elif file.name.endswith(".txt"):
            return file.read().decode("utf-8")
        else:
            raise BaseException("Unexpected file format. only PDF and text files are supported")
    except Exception as e:
        logger.error(f"Error reading file: {e}")
        raise  
    
def get_table_data(quiz):
    try:
        logger.info(f"parsing quiz data:  {quiz }") 
        quiz_data = json.load(quiz)
        
        
        table_data = []
        for q_num, q in quiz_data.items():
            mcq = q["mcq"]
            choices = " || ".join  
    