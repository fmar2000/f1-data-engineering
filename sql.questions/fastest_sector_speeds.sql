SELECT d.full_name, d.team_name, l.lap_number, l.i1_speed
FROM f1_clean_laps l
JOIN f1_clean_drivers d
  ON l.driver_number = d.driver_number
  AND l.session_key = d.session_key
  WHERE L.i1_speed IS NOT NULL
  ORDER BY l.i1_speed DESC
  LIMIT 10;