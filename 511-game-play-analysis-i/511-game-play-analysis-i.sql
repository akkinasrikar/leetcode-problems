# Write your MySQL query statement below
select a.player_id,min(a.event_date) as first_login from Activity a,Activity b where a.player_id=b.player_id group by a.player_id;