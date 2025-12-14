# Imports
import pandas as pd
from datetime import datetime, timedelta
import random

# Functions
def compute_dataframe(measure_name: str, frequency_minuts: int, duration_hours: int, datetime_start: datetime) -> pd.DataFrame:
    # Initialize computing data
    data_list = []
    total_minutes = 60 * duration_hours
    data_amont = int(total_minutes / frequency_minuts)

    # Generatate list
    for data_index in range(data_amont):
        data_dict = {}
        data_dict["Timestamp"] = compute_timestamp(datetime_start, frequency_minuts, data_index)
        data_dict["Measure"] = measure_name
        if data_index == 0:
            data_dict["Value"] = 50.0
        else:
            previous_value = data_list[data_index-1]["Value"]
            data_dict["Value"] = compute_value(previous_value)
        data_list.append(data_dict)

    return pd.DataFrame(data_list)

def compute_timestamp(datetime_start: datetime, frequency_minuts: int, data_index: int) -> datetime:
    return datetime_start + timedelta(minutes=frequency_minuts * data_index)

def compute_value(previous_value: float) -> float:
    return round(previous_value + random.uniform(-1.0, 1.0), 2)