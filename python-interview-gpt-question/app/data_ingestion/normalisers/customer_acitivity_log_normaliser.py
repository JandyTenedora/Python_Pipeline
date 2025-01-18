import json

from app.utils.find_project_root import find_project_root

project_root = find_project_root()

def normalise_customer_activity() -> (list[dict], list[dict]):
    with open(f"{project_root}/target/raw/large_customer_activity_logs.json", "r") as file:
        print("Loading json data...\n")
        data = json.load(file)
        normalized_customer_logs = []
        product_json = []
        for d in data:
            normalized_customer_log = {
                "timestamp": d["timestamp"],
                "user_id": d["user_id"],
                "event_type": d["event_type"],
                "product_id": d["metadata"]["product_id"]
            }
            product = {
                "product_id": d["metadata"]["product_id"],
                "category": d["metadata"]["category"],
                "device": d["metadata"]["device"]
            }
            normalized_customer_logs.append(normalized_customer_log)
            product_json.append(product)

        return normalized_customer_logs, product_json

def normalise_customer_activity_write():
    normalized_customer_logs, product_json = normalise_customer_activity()

    with open(f"{project_root}/target/normalized/normalized_customer_logs.json", "w") as main_file:
        print("Writing normalized_customer_logs.json...\n")
        json.dump(normalized_customer_logs, main_file, indent=4)

    with open(f"{project_root}/target/normalized/product_lookup.json", "w") as lookup_file:
        print("Writing product_lookup.json...\n")
        json.dump(product_json, lookup_file, indent=4)

if __name__ == "__main__":
    normalise_customer_activity_write()