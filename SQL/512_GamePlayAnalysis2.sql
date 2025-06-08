#512. Game Play Analysis II
#Easy
#Topics
#Companies
#SQL Schema
#Pandas Schema
#Table: Activity
#
#+--------------+---------+
#| Column Name  | Type    |
#+--------------+---------+
#| player_id    | int     |
#| device_id    | int     |
#| event_date   | date    |
#| games_played | int     |
#+--------------+---------+
#(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
#This table shows the activity of players of some games.
#Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
# 
#
#Write a solution to report the device that is first logged in for each player.
#
#Return the result table in any order.
#
#The result format is in the following example.
#
# 
#
#Example 1:
#
#Input: 
#Activity table:
#+-----------+-----------+------------+--------------+
#| player_id | device_id | event_date | games_played |
#+-----------+-----------+------------+--------------+
#| 1         | 2         | 2016-03-01 | 5            |
#| 1         | 2         | 2016-05-02 | 6            |
#| 2         | 3         | 2017-06-25 | 1            |
#| 3         | 1         | 2016-03-02 | 0            |
#| 3         | 4         | 2018-07-03 | 5            |
#+-----------+-----------+------------+--------------+
#Output: 
#+-----------+-----------+
#| player_id | device_id |
#+-----------+-----------+
#| 1         | 2         |
#| 2         | 3         |
#| 3         | 1         |
#+-----------+-----------+


with playerlogindate as (
    select player_id,device_id,rank() over (partition by player_id order by event_date) as 'row_num' from Activity
)

select t.player_id,t.device_id as 'device_id' from playerlogindate as t where t.row_num=1


-- 2nd query
SELECT
  A1.player_id,
  A1.device_id
FROM
  Activity A1
JOIN (
  SELECT
    player_id,
    MIN(event_date) AS first_login
  FROM
    Activity
  GROUP BY
    player_id
) A2 ON A1.player_id = A2.player_id
     AND A1.event_date = A2.first_login;
