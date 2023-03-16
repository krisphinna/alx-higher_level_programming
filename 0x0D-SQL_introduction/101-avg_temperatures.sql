-- Import temperatures into hbtn_0c_0
-- DML query to display average temperature by city
SELECT city,
AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
