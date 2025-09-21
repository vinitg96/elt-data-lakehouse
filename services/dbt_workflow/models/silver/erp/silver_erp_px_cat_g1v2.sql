SELECT
			id,
			cat,
			subcat,
			maintenance
		FROM {{ref('bronze_erp_px_cat_g1v2')}}