from app.log_processor.utils.log_processor_utils import register_process_log_functions, calculate_count_per_event, \
    find_most_common_event
from app.utils.find_project_root import find_project_root

PROJECT_ROOT = find_project_root()


class LogProcessor:
    def __init__(self, file_path, target_path, *log_functions):
        self.file_path = file_path
        self.target_path = target_path
        self.process_functions = register_process_log_functions(*log_functions)

    def execute_process_log_functions(self, callbacks):
        callbacks(self.file_path, self.target_path)

    def process_event_logs(self):
        self.execute_process_log_functions(self.process_functions)

def main():
    input_path = f"{PROJECT_ROOT}/target/raw"
    log_processor_path = f"{PROJECT_ROOT}/target"
    log_processor = LogProcessor(f"{input_path}/large_event_logs.json",
                                 f"{log_processor_path}/log_processing",
                                 calculate_count_per_event, find_most_common_event
                                 )
    log_processor.process_event_logs()

if __name__ == "__main__":
    main()