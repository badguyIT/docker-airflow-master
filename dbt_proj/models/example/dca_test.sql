SELECT *
FROM {{ref('data')}}
WHERE (high / open <= 1.07 AND low / open >= 0.93);