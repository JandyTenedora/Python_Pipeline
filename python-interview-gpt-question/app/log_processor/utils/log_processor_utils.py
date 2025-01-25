import pandas as pd

def register_process_log_functions(*callbacks):
    def wrapper(file_path, target_path):
        for callback in callbacks:
            callback(file_path, target_path)

    return wrapper

def calculate_count_per_event(file_path, target_path):
    df = pd.read_json(file_path)
    event_logs_by_type = df.groupby('event_type').size().reset_index(name="count")
    event_logs_by_type.to_csv(target_path + "/count_per_event.csv", index=False)

def find_most_common_event(file_path, target_path):
    df = pd.read_json(file_path)
    event_logs_by_type = df.groupby('event_type').size().reset_index(name="count")
    event_logs_by_type.sort_values('count', ascending=False).iloc[0][['event_type', 'count']].to_csv(target_path + "/most_common_event.csv", index=False)