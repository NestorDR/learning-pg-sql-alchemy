CREATE OR REPLACE FUNCTION udf_item_save(
    name varchar(50),
    "position" integer,
    price money,
    amount real,
    username varchar(100)
)
    RETURNS int AS
$$
DECLARE
    identity int;
BEGIN
    SELECT id INTO identity FROM item WHERE item.name = udf_item_save.name;

    IF identity IS NULL
    THEN
           INSERT INTO item
               (
                   name,
                   position,
                   price,
                   amount,
                   created_by,
                   created_at
               )
           VALUES
               (
                   udf_item_save.name,
                   udf_item_save.position,
                   udf_item_save.price,
                   udf_item_save.amount,
                   udf_item_save.username,
                   NOW()
               )
        RETURNING id INTO identity;
    ELSE
        UPDATE item
           SET name       = udf_item_save.name,
               position   = udf_item_save.position,
               price      = udf_item_save.price,
               amount     = udf_item_save.amount,
               updated_by = udf_item_save.username,
               updated_at = NOW()
         WHERE id = identity;
    END IF;
    --SELECT identity AS id;

    RETURN identity;
END;
$$
    LANGUAGE plpgsql;

SELECT udf_item_save('Computer', 1, '1000.50', 5, username=>'Nestor') AS identity
 UNION
SELECT udf_item_save('Alcohol', 2, '10', 1.5, 'Nestor');

--CALL udf_item_save('Alcohol', 2, '10', 1.5, 'Nestor');