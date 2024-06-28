from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    OPENAI_KEY = os.getenv('OPENAI_KEY')
    POSTGRE_URL = os.getenv('POSTGRE_URL')
    NEO4J_URL = os.getenv('NEO4J_URL')
    NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
    CLF_CONFIG_PATH = os.getenv('CLF_CONFIG_PATH')
    CLF_TOKENIZER_PATH = os.getenv('CLF_TOKENIZER_PATH')
    CLF_TRAINER_PATH = os.getenv('CLF_TRAINER_PATH')
    SUMM_MODEL_NAME = os.getenv('SUMM_MODEL_NAME')
