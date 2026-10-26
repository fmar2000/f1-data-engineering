SELECT 
    d.full_name,
    d.team_name,
    r.position,
    r.duration,
    r.gap_to_leader,
    r.number_of_laps
FROM f1_clean_session_result r
JOIN f1_clean_drivers d 
  ON r.driver_number = d.driver_number 
  AND r.session_key = d.session_key
ORDER BY r.position ASC;