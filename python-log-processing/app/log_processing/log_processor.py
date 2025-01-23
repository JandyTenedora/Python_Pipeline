import json

import pandas as pd

def not_null(key, value):
    if key in ['user_id', 'timestamp', 'event_type']:
        if value is None:
            return f"{key} has value None"
    return None

def validate_log_entries(log_entries):
    validations = {}
    for i, log in enumerate(log_entries):
        for key, value in log.items():
            validation = not_null(key, value)
            if validation is not None:
                validations[i] = validation
    if not validations:
        pass
    else:
        raise ValueError(f"Validations failed: {validations}")

def flatten_fields(log_entries):
    return [pd.json_normalize(log).to_dict(orient="records")[0] for log in log_entries]

def calculate_events_per_event_type(log_entries) -> pd.DataFrame:
    flattened_df = pd.DataFrame(flatten_fields(log_entries))
    grouped_df = flattened_df.groupby('event_type').size().reset_index(name="count")
    return grouped_df

def calculate_most_active_user(log_entries) -> pd.DataFrame:
    df = pd.DataFrame(log_entries)
    event_count_by_users_df = df.groupby('user_id').size().reset_index(name="event_count")
    sorted_event_count_by_users_df = event_count_by_users_df.sort_values(by=['event_count'], ascending=False)
    most_active_user = sorted_event_count_by_users_df.head(1)
    return most_active_user

if __name__ == "__main__":
    with open('input/logs.json', 'r') as file:
        data = json.load(file)
    final_logs = []
    for i in range(len(data['user_id'])):
        entry = {key: data[key][str(i)] for key in data}
        final_logs.append(entry)

    # Print the result
    [print(log) for log in final_logs]
    events_per_type = calculate_events_per_event_type(final_logs)
    most_active_user = calculate_most_active_user(final_logs)
    events_per_type.to_csv('output/events_per_type.csv', index=False)
    most_active_user.to_csv('output/most_active_user.csv', index=False, header=True)