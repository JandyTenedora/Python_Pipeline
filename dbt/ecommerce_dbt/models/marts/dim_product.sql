SELECT
    product_id,
    category,
    device
FROM {{ source('ecommerce_data_raw', 'product_catalog') }}