SELECT 
    sls_ord_num,
    sls_prd_key,
    sls_cust_id,
    CASE 
        WHEN sls_order_dt = '0' OR LEN(sls_order_dt) != 8 THEN NULL
        ELSE STRPTIME(sls_order_dt, '%Y%m%d')::DATE
    END AS sls_order_dt,
    CASE 
        WHEN sls_ship_dt = '0' OR LEN(sls_ship_dt) != 8 THEN NULL
        ELSE STRPTIME(sls_ship_dt, '%Y%m%d')::DATE
    END AS sls_ship_dt,
    CASE 
        WHEN sls_due_dt = '0' OR LEN(sls_due_dt) != 8 THEN NULL
        ELSE STRPTIME(sls_due_dt, '%Y%m%d')::DATE
    END AS sls_due_dt,
    CASE 
        WHEN sls_sales IS NULL 
            OR CAST(sls_sales AS FLOAT) <= 0 
            OR CAST(sls_sales AS FLOAT) != CAST(sls_quantity AS INT) * ABS(CAST(sls_price AS FLOAT)) 
        THEN CAST(sls_quantity AS INT) * ABS(CAST(sls_price AS FLOAT))
        ELSE CAST(sls_sales AS FLOAT)
    END AS sls_sales, -- Recalculate sales if original value is missing or incorrect
    CAST(sls_quantity AS INT) AS sls_quantity,
    CASE 
        WHEN sls_price IS NULL OR CAST(sls_price AS FLOAT) <= 0 
        THEN 
            CASE 
                WHEN CAST(sls_quantity AS INT) = 0 THEN NULL
                ELSE CAST(sls_sales AS FLOAT) / CAST(sls_quantity AS INT)
            END
        ELSE CAST(sls_price AS FLOAT)
    END AS sls_price
FROM {{ref('bronze_crm_sales_details')}}