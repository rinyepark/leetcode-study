/* Write your PL/SQL query statement below */
select a.name Customers
from customers a
where 1=1
and not exists (select 1
                from orders b
                where a.id = b.customerId)