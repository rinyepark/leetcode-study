/* Write your PL/SQL query statement below */

select name
from (select name, nvl(referee_id, -1) referee_id
      from Customer)
where 1=1
and referee_id <> 2