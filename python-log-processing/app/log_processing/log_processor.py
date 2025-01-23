import json

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

"""
Check if given value is not null

Parameters:
key(str): Key associated with value
value(any): Value to check for null
"""
def not_null(key, value):
    if key in ['user_id', 'timestamp', 'event_type']:
        if value is None:
            return f"{key} has None value"
        else:
            return None
    pass

def validate_log_entries(log_entries):
    validations = {}
    for i, log in enumerate(log_entries):
        for k,v in log.items():
            validation = not_null(k,v)
            if validation is not None:
                validations[i] = validation
    return validations

def flatten_fields(log_entries):
    df = pd.json_normalize(log_entries)
    df.info()
    return df.to_dict(orient='records')

def calculate_events_per_event_type(log_entries) -> pd.DataFrame:
    df = pd.DataFrame(log_entries)
    events_per_type_df = df.groupby('event_type').size().reset_index(name='count')
    return events_per_type_df

def calculate_most_active_user(log_entries) -> pd.DataFrame:
    df = pd.DataFrame(log_entries)
    most_active_user_df = df.groupby('user_id').size().reset_index(name='user_count').sort_values('user_count', ascending=False).head(1)
    return most_active_user_df

if __name__ == "__main__":
    with open('input/logs.json', 'r') as file:
        data = json.load(file)
    data_df = pd.DataFrame(data)

    final_logs = flatten_fields(data_df.to_dict(orient='records'))
    # Print the result
    [print(log) for log in final_logs]
    events_per_type = calculate_events_per_event_type(final_logs)
    most_active_user = calculate_most_active_user(final_logs)
    events_per_type.to_csv('output/events_per_type.csv', index=False)
    most_active_user.to_csv('output/most_active_user.csv', index=False, header=True)