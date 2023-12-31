CREATE OR REPLACE FUNCTION udf_sales_get(
    limited_to integer
)
    RETURNS TABLE
            (
                name        varchar,
                total_price money
            )
AS
$$
BEGIN
    RETURN QUERY
        SELECT item.name,
               item.amount * item.price AS total_price
          FROM item
         ORDER BY total_price DESC
         LIMIT limited_to;
END;
$$
    LANGUAGE plpgsql;

SELECT name, total_price
  FROM udf_sales_get(2);

--CALL udf_sales_get(2)