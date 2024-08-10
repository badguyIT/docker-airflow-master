WITH monthly_prices AS (
    SELECT
        symbol,
        DATE_TRUNC('month', time) AS month,
        FIRST_VALUE(open) OVER (PARTITION BY symbol ORDER BY time) AS open_price
    FROM stocks
    WHERE time BETWEEN '2018-01-01' AND '2023-12-31'
),
monthly_totals AS (
    SELECT
        symbol,
        COUNT(*) AS num_months,
        SUM(open_price * 100) AS total_spent
    FROM monthly_prices
    GROUP BY symbol
) ,
end_prices AS (
    SELECT
        symbol,
        FIRST_VALUE(close) OVER (PARTITION BY symbol ORDER BY time DESC) AS end_price
    FROM stocks
    -- WHERE time = '2023-12-29'
)
SELECT
    m.symbol,
    m.total_spent,
    e.end_price * m.num_months AS total_value,
    ((e.end_price * m.num_months - m.total_spent) / m.total_spent) * 100 AS profit_percent
FROM monthly_totals m
JOIN end_prices e ON m.symbol = e.symbol