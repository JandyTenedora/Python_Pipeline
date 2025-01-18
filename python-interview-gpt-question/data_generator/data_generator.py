import pandas as pd
import random
import json
from datetime import datetime, timedelta
import os

def generate_sales_data(rows):
    """Generate sales data with the specified number of rows."""
    data = {
        "transaction_id": list(range(1, rows + 1)),
        "product_id": [random.randint(100, 110) for _ in range(rows)],
        "sale_date": [
            (datetime(2025, 1, 1) + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
            for _ in range(rows)
        ],
        "quantity": [random.randint(1, 5) for _ in range(rows)],
        "price_per_unit": [round(random.uniform(10, 50), 2) for _ in range(rows)],
    }
    return pd.DataFrame(data)

def generate_customer_logs(entries):
    """Generate customer activity logs with the specified number of entries."""
    event_types = ["view", "click", "purchase"]
    devices = ["mobile", "desktop", "tablet"]
    logs = []
    for i in range(entries):
        timestamp = (
            datetime(2025, 1, 1) + timedelta(seconds=random.randint(0, 30 * 24 * 3600))
        ).strftime("%Y-%m-%dT%H:%M:%SZ")
        logs.append({
            "timestamp": timestamp,
            "user_id": f"U{random.randint(100, 200)}",
            "event_type": random.choice(event_types),
            "metadata": {
                "product_id": random.randint(100, 110),
                "category": random.choice(["electronics", "home", "furniture", "clothing"]),
                "device": random.choice(devices),
            },
        })
    return logs

def generate_logs(entries):
    """
    Generate customer activity logs with a specified number of entries.

    Parameters:
        entries (int): Number of log entries to generate.

    Returns:
        list: A list of log entries in dictionary format.
    """
    event_types = ["view", "click", "purchase"]
    devices = ["mobile", "desktop", "tablet"]
    categories = ["electronics", "home", "furniture", "clothing"]

    logs = []
    for _ in range(entries):
        timestamp = (
                datetime(2025, 1, 1) + timedelta(seconds=random.randint(0, 30 * 24 * 3600))
        ).strftime("%Y-%m-%dT%H:%M:%SZ")
        logs.append({
            "timestamp": timestamp,
            "user_id": f"U{random.randint(100, 200)}",
            "event_type": random.choice(event_types),
            "metadata": {
                "product_id": random.randint(100, 110),
                "category": random.choice(categories),
                "device": random.choice(devices),
            },
        })
    return logs

def main():
    # Configure the number of entries
    n = 5000  # Number of sales data rows
    m = 5000  # Number of customer activity log entries
    o = 10000 # Number of logs

    # Generate the data
    sales_data = generate_sales_data(n)
    customer_logs = generate_customer_logs(m)
    event_logs = generate_logs(o)

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    target_dir = f"{dir_path}/target/raw"
    # Save to files
    sales_file = "large_sales_data.csv"
    logs_file = "large_customer_activity_logs.json"
    event_logs_file = "large_event_logs.json"

    # Save sales data as CSV
    sales_data.to_csv(f"{target_dir}/{sales_file}", index=False)
    print(f"Sales data saved to {sales_file}")

    # Save customer logs as JSON
    with open(f"{target_dir}/{logs_file}", "w") as json_file:
        json.dump(customer_logs, json_file, indent=4)
    print(f"Customer activity logs saved to {logs_file}")

    with open(f"{target_dir}/{event_logs_file}", "w") as json_file:
        json.dump(event_logs, json_file, indent=4)
    print(f"Event logs saved to {event_logs_file}")

if __name__ == "__main__":
    main()
