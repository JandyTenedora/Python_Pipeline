---

### **Exercise 1: Building a Streaming Data Pipeline (Kafka Integration)**

#### **Scenario**:
You are tasked with building a real-time data pipeline to process event data from a Kafka topic. The goal is to consume streaming events, transform the data, and write it to a Snowflake table.

#### **Requirements**:
1. Write a Python script that:
   - Consumes messages from a Kafka topic (`user_activity`) containing JSON events. Each event has fields: 
     - `user_id`
     - `event_type` (e.g., `click`, `view`, `purchase`)
     - `timestamp`
   - Validates the events (e.g., `user_id` and `timestamp` are not null, `event_type` is valid).
   - Aggregates the number of events per `event_type` every 10 seconds.
   - Writes the aggregated data into a Snowflake table.

2. Use a Python Kafka library (e.g., `confluent-kafka`) and the Snowflake Python connector.

#### **Focus Areas**:
- Real-time processing logic.
- Efficient aggregation in small windows.
- Integration with external systems (Kafka and Snowflake).

---

### **Exercise 2: Data Modeling and Transformation with dbt**

#### **Scenario**:
You have been given raw e-commerce sales data in a BigQuery dataset (`raw_data`). You need to use dbt to create a normalized and aggregated schema for reporting purposes.

#### **Requirements**:
1. Create the following dbt models:
   - **Staging Model**:
     - Clean the raw sales data (e.g., validate `sale_date`, remove duplicate records).
   - **Fact Table**:
     - Aggregate daily revenue by `product_id` and `category`.
   - **Dimension Table**:
     - Extract a distinct list of `products` with their details (e.g., `product_id`, `category`).
2. Write a schema test to ensure `product_id` in the fact table is not null and unique.

3. Run the dbt pipeline to output the transformed tables into a `reporting` dataset.

#### **Focus Areas**:
- Data modeling best practices (fact and dimension tables).
- Using dbt for transformations and schema tests.
- Writing clean and modular SQL.

---

### **Exercise 3: Log Processing and JSON Parsing**

#### **Scenario**:
Your team receives user activity logs in JSON format. Each log contains:
```json
{
    "user_id": "U123",
    "timestamp": "2025-01-10T10:00:00Z",
    "event_type": "view",
    "metadata": {
        "product_id": "P456",
        "device": "mobile",
        "category": "electronics"
    }
}
```

You need to parse these logs, extract key insights, and store the results in a structured format.

#### **Requirements**:
1. Write a Python script that:
   - Reads logs from a JSON file (`user_logs.json`).
   - Validates each log entry (e.g., `user_id`, `timestamp`, and `event_type` must not be null).
   - Extracts and flattens fields like `user_id`, `timestamp`, `event_type`, `product_id`, `device`, and `category`.
   - Aggregates the data to calculate:
     - Total events per `event_type`.
     - Most active `user_id` (by event count).
   - Outputs the results to a CSV file (`aggregated_logs.csv`).

2. Use Python libraries like `pandas` or `json` for processing.

#### **Focus Areas**:
- JSON parsing and validation.
- Data aggregation and insights extraction.
- Writing efficient and clean Python code.

---

### **Key Considerations for All Exercises**
1. **Clarity and Modularity**:
   - Write clean, modular code with reusable functions/classes.
   - Use comments to explain your approach where necessary.

2. **Error Handling**:
   - Demonstrate graceful handling of common issues (e.g., invalid input, connection errors).

3. **Testability**:
   - Where possible, write small tests or include assertions to validate your code.

4. **Communication**:
   - Explain your thought process and trade-offs during the interview.
