import json

import pandas as pd

def not_null(key, value):
    pass

def validate_log_entries(log_entries):
    pass

def flatten_fields(log_entries):
    pass

def calculate_events_per_event_type(log_entries) -> pd.DataFrame:
    pass

def calculate_most_active_user(log_entries) -> pd.DataFrame:
    pass

if __name__ == "__main__":
    final_logs = []
    # Print the result
    [print(log) for log in final_logs]
    events_per_type = calculate_events_per_event_type(final_logs)
    most_active_user = calculate_most_active_user(final_logs)
    events_per_type.to_csv('output/events_per_type.csv', index=False)
    most_active_user.to_csv('output/most_active_user.csv', index=False, header=True)