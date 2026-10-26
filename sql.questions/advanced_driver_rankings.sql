SELECT 
    d.team_name,
    d.full_name,
    l.i1_speed,
    ROW_NUMBER() OVER (PARTITION BY d.team_name ORDER BY l.i1_speed DESC) AS team_speed_rank
FROM f1_clean_laps l
RIGHT JOIN f1_clean_drivers d 
  ON l.driver_number = d.driver_number 
  AND l.session_key = d.session_key
WHERE d.session_key = 9158
  AND l.i1_speed IS NOT NULL
ORDER BY d.team_name, team_speed_rank;