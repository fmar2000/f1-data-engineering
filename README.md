# 🏎️ Formula 1 Data Engineering Pipeline & Analytics

An end-to-end data engineering portfolio project implementing a containerized medallion-architecture data pipeline. This repository ingests, cleans, models, and analyzes 2023 Singapore Grand Prix telemetry data (Practice 1, Session ID: 9158) using Python, Docker, PostgreSQL, and advanced SQL.

---

## 🏗️ Architecture & Tech Stack

* **Orchestration & Containerization:** Docker, Docker Compose, WSL 2
* **Warehouse:** PostgreSQL
* **Data Processing Language:** Python (Pandas/SQLAlchemy)
* **Storage Pattern:** Medallion Architecture (`data/processed/` landing to relational warehouse tables)

---

## 📂 Repository Structure

```text
f1-race-pipeline/
├── data/
│   └── processed/          # Cleaned CSV artifacts (drivers, laps, weather, etc.)
├── src/
│   ├── ingest.py           # Raw data ingestion scripts
│   ├── transform.py        # Data hygiene & cleaning pipelines
│   └── load.py             # Warehouse loading logic
├── sql.questions/
│   ├── advanced_driver_rankings.sql   # RIGHT JOIN & window partitioning
│   ├── fastest_sector_speeds.sql      # Aggregations (MAX, AVG) & null handling
│   ├── practice_performance_leaderboard.sql # Multi-table joins and positional sorting
│   ├── speed_categorization.sql       # CASE WHEN feature engineering
│   └── track_temperature_trend.sql    # Temporal filtering (BETWEEN)
└── docker-compose.yaml     # Containerized PostgreSQL instance

## Analytical SQL Suite

This repository features 5 analytical queries designed to extract deep insights while demonstrating advanced SQL proficiencies:

1. **Practice Performance Leaderboard (`practice_performance_leaderboard.sql`)**
   *  *Technique:* multi-table joins (`JOIN`) using foreign key matching (`driver_number` and `session_key`) combined with positional ordering (`ORDER BY`).
   *Purpose:* Combines pre-aggregated results with driver meta data to produce a structured leaderboard showing every drivers gap to the leader.

2. **Fastest Sector Speeds (`fastest_sector_speeds.sql`)**
   *  *Tehnique:* Aggregate functions (`MAX()` and `ROUND(AVG(...), 2)`). relational `JOIN` and null filtering (`IS NOT NULL`).
   *Purpose:* Identifies top maximum speeds achieved down straightaways while calculating average speeds per driver.

3. **Track Temperature Trend (`track_temperature_trend.sql`)**
   *  *Technique:* Time-series extraction and range filtering (`BETWEEN '09:30:00' AND '10:30:00'`).
   *Purpose:* Analyzes micro-environmental track changes between two times within the track session.

4. **Speed Categorization (`speed_categorization.sql`)**
   *  *Technique:*  On-the-fly conditional feature using `CASE WHEN`.
   *Purpose:* Groups raw velocity metrics into categorized groups ('Vmax', 'Medium', 'Standard').

5. **Advanced Driver Rankings (`advanced_driver_rankings.sql`)**
   *Technique:* `RIGHT-OUTER JOIN` combined with window partitioning (`ROW_NUMBER() OVER (PARTITION BY ...)`).
   *Purpose:* Ranks individual lap speeds per team by fastest speeds recorded in the speed trap while preserving complete driver record sets via RIGHT JOIN.
