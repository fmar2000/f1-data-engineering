SELECT 
    d.full_name,
    d.team_name,
    l.lap_number,
    l.i1_speed,
    CASE 
        WHEN l.i1_speed >= 300 THEN 'Vmax / High Speed'
        WHEN l.i1_speed >= 280 THEN 'Medium Speed'
        ELSE 'Standard Speed'
    END AS speed_category
FROM f1_clean_laps l
JOIN f1_clean_drivers d 
  ON l.driver_number = d.driver_number 
  AND l.session_key = d.session_key
WHERE l.i1_speed IS NOT NULL
ORDER BY l.i1_speed DESC;