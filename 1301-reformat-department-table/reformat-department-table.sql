# Write your MySQL query statement below
WITH all_row AS (
    SELECT DISTINCT id FROM Department ORDER BY id
),
jan AS (
    SELECT id, revenue FROM Department WHERE month = "Jan"
),
feb AS (
    SELECT id, revenue FROM Department WHERE month = "Feb"
),
mar AS (
    SELECT id, revenue FROM Department WHERE month = "Mar"
),
apr AS (
    SELECT id, revenue FROM Department WHERE month = "Apr"
),
may AS (
    SELECT id, revenue FROM Department WHERE month = "May"
),
jun AS (
    SELECT id, revenue FROM Department WHERE month = "Jun"
),
jul AS (
    SELECT id, revenue FROM Department WHERE month = "Jul"
),
aug AS (
    SELECT id, revenue FROM Department WHERE month = "Aug"
),
sep AS (
    SELECT id, revenue FROM Department WHERE month = "Sep"
),
oc AS (
    SELECT id, revenue FROM Department WHERE month = "Oct"
),
nov AS (
    SELECT id, revenue FROM Department WHERE month = "Nov"
),
de AS (
    SELECT id, revenue FROM Department WHERE month = "Dec"
)

SELECT all_row.id AS id, jan.revenue AS Jan_Revenue, feb.revenue AS Feb_Revenue, mar.revenue AS Mar_Revenue, apr.revenue AS Apr_Revenue, may.revenue AS May_Revenue, jun.revenue AS Jun_Revenue, jul.revenue AS Jul_Revenue, aug.revenue AS Aug_Revenue, sep.revenue AS Sep_Revenue, oc.revenue AS Oct_Revenue, nov.revenue AS Nov_Revenue, de.revenue AS Dec_Revenue FROM all_row LEFT JOIN jan ON all_row.id = jan.id LEFT JOIN feb ON all_row.id = feb.id LEFT JOIN mar ON all_row.id = mar.id LEFT JOIN apr ON all_row.id = apr.id LEFT JOIN may ON all_row.id = may.id LEFT JOIN jun ON all_row.id = jun.id LEFT JOIN jul ON all_row.id = jul.id LEFT JOIN aug ON all_row.id = aug.id LEFT JOIN sep ON all_row.id = sep.id LEFT JOIN oc ON all_row.id = oc.id LEFT JOIN nov ON all_row.id = nov.id LEFT JOIN de ON all_row.id = de.id;