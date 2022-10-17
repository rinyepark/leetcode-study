/* Write your PL/SQL query statement below */

SELECT *
FROM CINEMA
WHERE 1=1
AND MOD(ID, 2) <> 0
AND DESCRIPTION <> 'boring'
ORDER BY RATING DESC;