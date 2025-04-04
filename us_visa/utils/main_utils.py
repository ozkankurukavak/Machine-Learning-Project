import os
import sys
import yaml
import dill
import numpy as np
import pandas as pd
from pandas import DataFrame
import logging

# Özel hata sınıfı
class USvisaException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)

# 1️ YAML dosyasını okuyup Python sözlüğü olarak döndüren fonksiyon

def read_yaml_file(file_path: str) -> dict:
    """
    Verilen YAML dosyasını okuyarak bir Python sözlüğü (dictionary) olarak döndürür.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise USvisaException(e, sys)

# 2️ Python nesnesini YAML formatında kaydeden fonksiyon

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Python nesnesini (dictionary, liste vb.) YAML formatında dosyaya kaydeder.
    Eğer replace=True ise, mevcut dosyayı silip yeniden oluşturur.
    """
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise USvisaException(e, sys)

# 3️ Pickle dosyasını yükleyip Python nesnesine çeviren fonksiyon

def load_object(file_path: str) -> object:
    """
    Pickle (dill) formatındaki bir dosyayı yükleyerek Python nesnesine çevirir.
    """
    try:
        logging.info("Entered the load_object method of utils")
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        logging.info("Exited the load_object method of utils")
        return obj
    except Exception as e:
        raise USvisaException(e, sys)

# 4️ NumPy dizisini dosyaya kaydeden fonksiyon

def save_numpy_array_data(file_path: str, array: np.array) -> None:
    """
    NumPy dizisini belirtilen dosyaya kaydeder.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise USvisaException(e, sys)

# 5️ Kaydedilmiş NumPy dizisini dosyadan yükleyen fonksiyon

def load_numpy_array_data(file_path: str) -> np.array:
    """
    Dosyadan bir NumPy dizisini yükler ve döndürür.
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise USvisaException(e, sys)

# 6️ Python nesnesini pickle formatında kaydeden fonksiyon

def save_object(file_path: str, obj: object) -> None:
    """
    Python nesnesini pickle formatında belirtilen dosyaya kaydeder.
    """
    try:
        logging.info("Entered the save_object method of utils")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exited the save_object method of utils")
    except Exception as e:
        raise USvisaException(e, sys)

# 7️ DataFrame içinden belirli sütunları silen fonksiyon

def drop_columns(df: DataFrame, cols: list) -> DataFrame:
    """
    Pandas DataFrame içindeki belirtilen sütunları siler.
    """
    try:
        logging.info("Entered drop_columns method of utils")
        df = df.drop(columns=cols, axis=1)
        logging.info("Exited the drop_columns method of utils")
        return df
    except Exception as e:
        raise USvisaException(e, sys)
