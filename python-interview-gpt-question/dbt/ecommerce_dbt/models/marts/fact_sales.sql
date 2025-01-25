SELECT
    sale_date,
    product_id,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price_per_unit) AS total_revenue
FROM {{ ref('stg_sales')}}
GROUP BY
sale_date, product_id