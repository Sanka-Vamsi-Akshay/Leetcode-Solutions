# Write your MySQL query statement below
WITH filter1 AS (
    SELECT store_id, COUNT(store_id) AS cnt FROM inventory GROUP BY store_id HAVING COUNT(store_id) >= 3
), filter2 AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY price) AS num FROM inventory WHERE store_id IN (SELECT store_id FROM filter1)
), T AS (
    SELECT T1.store_id AS store_id, T2.product_name AS most_exp_product, T1.product_name AS cheapest_product, ROUND(T1.quantity / T2.quantity, 2) AS imbalance_ratio FROM (SELECT store_id, product_name, quantity, price FROM filter2 WHERE num = 1) T1 LEFT JOIN (SELECT store_id, product_name, quantity, price FROM filter2 WHERE num = (SELECT cnt FROM filter1 WHERE store_id = filter2.store_id)) T2 ON T1.store_id = T2.store_id WHERE T1.quantity > T2.quantity
)
SELECT T.store_id AS store_id, store_name, location, most_exp_product, cheapest_product, imbalance_ratio FROM T LEFT JOIN stores ON T.store_id = stores.store_id ORDER BY imbalance_ratio DESC, store_name;