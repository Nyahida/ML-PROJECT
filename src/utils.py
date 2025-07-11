import os
import sys
import dill

import pandas as pd
import numpy as np
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        # Create the directory if it doesn't exist
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Open the file in write-binary mode and save the object
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
