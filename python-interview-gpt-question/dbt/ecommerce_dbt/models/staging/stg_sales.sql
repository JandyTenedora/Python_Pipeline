WITH cleaned_sales AS (
    SELECT
        transaction_id,
        product_id,
        sale_date,
        quantity,
        price_per_unit
    FROM {{ source('raw_data', 'sales')}}
    WHERE sale_date IS NOT NULL
)
SELECT * FROM cleaned_sales