-- lists number of recors with same score and sort them
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC
