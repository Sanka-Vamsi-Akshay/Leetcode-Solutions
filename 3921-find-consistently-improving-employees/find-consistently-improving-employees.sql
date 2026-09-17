# Write your MySQL query statement below
SELECT
    T.employee_id AS employee_id, 
    E.name AS name, 
    T.rating - T.prev2 AS improvement_score 
FROM (
    SELECT 
        *, 
        LAG(rating) OVER (PARTITION BY employee_id ORDER BY review_date) AS prev1, 
        LAG(rating, 2) OVER (PARTITION BY employee_id ORDER BY review_date) AS prev2, 
        LEAD(rating) OVER (PARTITION BY employee_id ORDER BY review_date) AS next 
    FROM performance_reviews
) T 
LEFT JOIN employees E 
    ON T.employee_id = E.employee_id 
WHERE T.next IS NULL
    AND T.prev2 IS NOT NULL 
    AND T.rating > T.prev1 
    AND T.prev1 > T.prev2 
ORDER BY 
    improvement_score DESC, 
    name;