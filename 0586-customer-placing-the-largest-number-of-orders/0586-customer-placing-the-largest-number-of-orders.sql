/* Write your PL/SQL query statement below */
select customer_number
from (
select customer_number, count(*) cnt
from orders
group by customer_number
order by cnt desc) a
where rownum = 1