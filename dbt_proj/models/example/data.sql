WITH filtered AS (
    SELECT *
    FROM stocks
    WHERE (high / open <= 1.07) AND (low / open >= 0.93)
),
monthly_trades AS (
    SELECT
        symbol,
        DATE_TRUNC('month', time) AS month
    FROM filtered
    WHERE time BETWEEN '2018-01-01' AND '2023-12-31'
    GROUP BY symbol, month
),
months_range AS (
    SELECT
        symbol,
        COUNT(DISTINCT month) AS months_count
    FROM monthly_trades
    GROUP BY symbol
),
valid_symbols AS (
    SELECT
        symbol
    FROM months_range
    WHERE months_count = 72 -- Số tháng từ 01/2018 đến 12/2023
) SELECT *
FROM filtered
WHERE symbol IN (SELECT symbol FROM valid_symbols)