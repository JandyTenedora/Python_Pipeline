SELECT
    user_id,
    DATE(timestamp) AS activity_date,
    COUNT(CASE WHEN event_type = 'view' THEN 1 END) AS views,
    COUNT(CASE WHEN event_type = 'clicks' THEN 1 END) AS clicks,
    COUNT(CASE WHEN event_type = 'purchases' THEN 1 END) AS purchases,
FROM {{ref('stg_customer_logs')}}
GROUP BY user_id, product_id, activity_date