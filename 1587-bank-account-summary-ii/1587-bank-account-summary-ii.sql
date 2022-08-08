# Write your MySQL query statement below
select a.name,sum(b.amount) as balance from Users a left join Transactions b on a.account=b.account group by a.account having balance>10000;