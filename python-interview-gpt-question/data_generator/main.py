import pandas as pd
import random
import json
from datetime import datetime, timedelta

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

def main():
    # Configure the number of entries
    n = 5000  # Number of sales data rows
    m = 5000  # Number of customer activity log entries

    # Generate the data
    sales_data = generate_sales_data(n)
    customer_logs = generate_customer_logs(m)

    # Save to files
    sales_file = "large_sales_data.csv"
    logs_file = "large_customer_activity_logs.json"

    # Save sales data as CSV
    sales_data.to_csv(f"target/{sales_file}", index=False)
    print(f"Sales data saved to {sales_file}")

    # Save customer logs as JSON
    with open(f"target/{logs_file}", "w") as json_file:
        json.dump(customer_logs, json_file, indent=4)
    print(f"Customer activity logs saved to {logs_file}")

if __name__ == "__main__":
    main()
