SELECT
    ROW_NUMBER() OVER (ORDER BY cst_id) AS customer_key, 
    ci.cst_id                          AS customer_id,
    ci.cst_key                         AS customer_number,
    ci.cst_firstname                   AS first_name,
    ci.cst_lastname                    AS last_name,
    la.cntry                           AS country,
    ci.cst_marital_status              AS marital_status,
    CASE 
        WHEN ci.cst_gndr != 'n/a' THEN ci.cst_gndr 
        ELSE COALESCE(ca.gen, 'n/a')  			   
    ca.bdate                           AS birthdate,
    ci.cst_create_date                 AS create_date
FROM {{ref('silver_crm_cust_info')}} ci
LEFT JOIN {{ref('silver_erp_cust_az12')}} ca
    ON ci.cst_key = ca.cid
LEFT JOIN {{ref('silver_erp_loc_a101')}}  la
    ON ci.cst_key = la.cid