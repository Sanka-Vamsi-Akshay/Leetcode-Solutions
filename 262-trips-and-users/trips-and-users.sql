# Write your MySQL query statement below
WITH ban AS (
    SELECT users_id FROM Users WHERE banned = 'Yes'
),
tmp AS (
    SELECT request_at, status FROM Trips WHERE (request_at BETWEEN '2013-10-01' AND '2013-10-03') AND (client_id NOT IN (SELECT * FROM ban)) AND (driver_id NOT IN (SELECT * FROM ban))
)
SELECT request_at AS Day, ROUND(SUM(CASE WHEN status != "completed" THEN 1 ELSE 0 END) / COUNT(status), 2) AS 'Cancellation Rate' FROM tmp GROUP BY request_at;