/* Write your PL/SQL query statement below */
SELECT name, population, area
FROM WORLD
WHERE 1=1
AND (POPULATION >= 25000000 OR AREA >= 3000000)
;