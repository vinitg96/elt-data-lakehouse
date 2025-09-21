SELECT
CASE
    WHEN cid LIKE 'NAS%' THEN SUBSTRING(cid, 4, LEN(cid)) -- Remove 'NAS' prefix if present
    ELSE cid
END AS cid, 
CASE
    WHEN CAST(bdate AS DATE) > NOW() THEN NULL
    ELSE CAST(bdate AS DATE)
END AS bdate, -- Set future birthdates to NULL
CASE
    WHEN UPPER(TRIM(gen)) IN ('F', 'FEMALE') THEN 'Female'
    WHEN UPPER(TRIM(gen)) IN ('M', 'MALE') THEN 'Male'
    ELSE 'n/a'
END AS gen -- Normalize gender values and handle unknown cases
FROM {{ref('bronze_erp_cust_az12')}}