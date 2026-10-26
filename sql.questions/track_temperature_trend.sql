SELECT 
    date,
    air_temperature,
    track_temperature
FROM f1_clean_weather
WHERE session_key = 9158
  AND date::time BETWEEN '09:30:00' AND '10:30:00'
ORDER BY date ASC;