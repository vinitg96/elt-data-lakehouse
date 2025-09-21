
SELECT * FROM read_csv({{source('bronze', 'cust_info')}}, all_varchar='true')