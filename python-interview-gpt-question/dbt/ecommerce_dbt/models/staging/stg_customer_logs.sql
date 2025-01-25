WITH cleaned_customer_logs AS (
    SELECT
        timestamp,
        user_id,
        event_type,
        product_id
    FROM {{source('raw_data', 'customer_logs')}}
    WHERE user_id IS NOT NULL
)
SELECT * FROM cleaned_customer_logs