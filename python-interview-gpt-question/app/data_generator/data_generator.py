import pandas as pd
import random
import json
from datetime import datetime, timedelta

from app.utils.find_project_root import find_project_root


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

def generate_customer_logs(entries, product_lookup):
    """Generate customer activity logs with the specified number of entries."""
    event_types = ["view", "click", "purchase"]
    logs = []
    for i in range(entries):
        product = random.choice(product_lookup)
        timestamp = (
            datetime(2025, 1, 1) + timedelta(seconds=random.randint(0, 30 * 24 * 3600))
        ).strftime("%Y-%m-%dT%H:%M:%SZ")
        logs.append({
            "timestamp": timestamp,
            "user_id": f"U{random.randint(100, 200)}",
            "event_type": random.choice(event_types),
            "metadata": {
                "product_id": product['product_id'],
                "category": product['category'],
                "device": product['device'],
            },
        })
    return logs

def generate_product_lookup(length):
    categories = {
        "home": {
            "prefix": 1,
            "devices": {
                "smart_speaker": 11,
                "thermostat": 12,
                "vacuum": 13,
                "lightbulb": 14,
                "security_camera": 15,
            },
        },
        "electronics": {
            "prefix": 2,
            "devices": {
                "smartphone": 21,
                "laptop": 22,
                "tablet": 23,
                "tv": 24,
                "smartwatch": 25,
            },
        },
        "furniture": {
            "prefix": 3,
            "devices": {
                "sofa": 31,
                "desk": 32,
                "chair": 33,
                "bed": 34,
                "bookshelf": 35,
            },
        },
        "clothing": {
            "prefix": 4,
            "devices": {
                "t_shirt": 41,
                "jacket": 42,
                "shoes": 43,
                "hat": 44,
                "gloves": 45,
            },
        },
    }

    data = []
    seen_ids = set()  # Ensure unique product IDs globally

    while len(data) < length:
        # Randomly pick a category
        category = random.choice(list(categories.keys()))
        category_data = categories[category]

        # Randomly pick a device within the category
        device = random.choice(list(category_data["devices"].keys()))
        device_suffix = category_data["devices"][device]

        # Construct product_id based on category and device rules
        prefix = category_data["prefix"] * 100
        product_id = prefix + device_suffix

        # Ensure the product_id is globally unique
        while product_id in seen_ids:
            product_id += 1  # Increment product_id to make it unique

        # Add product_id to the seen set and append the entry
        seen_ids.add(product_id)
        data.append({
            "product_id": product_id,
            "category": category,
            "device": device
        })

    return data

def generate_logs(entries, product_lookup):
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
        product = random.choice(product_lookup)
        print(product)
        timestamp = (
                datetime(2025, 1, 1) + timedelta(seconds=random.randint(0, 30 * 24 * 3600))
        ).strftime("%Y-%m-%dT%H:%M:%SZ")
        logs.append({
            "timestamp": timestamp,
            "user_id": f"U{random.randint(100, 200)}",
            "event_type": random.choice(event_types),
            "metadata": {
                "product_id": product['product_id'],
                "category": product['category'],
                "device": product['device'],
            },
        })
    return logs

def main():
    # Configure the number of entries
    n = 5000  # Number of sales data rows
    m = 5000  # Number of customer activity log entries
    o = 10000 # Number of logs

    # Generate the data
    product_lookup = generate_product_lookup(50)
    sales_data = generate_sales_data(n)
    customer_logs = generate_customer_logs(m, product_lookup)
    event_logs = generate_logs(o, product_lookup)

    dir_path = str(find_project_root())
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
