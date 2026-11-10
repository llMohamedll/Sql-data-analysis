# Project 05: SQL for Data Analysis

## Overview
Comprehensive SQL tutorial using Python's sqlite3 and pandas, covering database design, complex queries, joins, aggregations, and CRUD operations.

## Original Notebooks (4)
- `DB0201EN-Week3-1-3-SQLmagic-SQlite-v2.ipynb`
- `DB0201EN-Week3-1-4-Analyzing-SQLite-v2.ipynb`
- `DB0201EN-Week4-1-1-RealDataPractice-v5-sqlite-Learner-v2(Edited).ipynb`
- `Week4-Insert-Update-SQLite-v2.ipynb`

## Key Skills Demonstrated
- Database creation and schema design
- Basic queries: SELECT, WHERE, ORDER BY, LIMIT
- Aggregations: COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING
- JOINs: INNER, LEFT, multiple table joins
- CRUD: INSERT, UPDATE, DELETE
- pandas SQL integration (`read_sql_query`)

## How to Run
```bash
pip install pandas numpy matplotlib seaborn
python main.py
```

## Outputs
- `chicago_sql_analysis.png` - Chicago socioeconomic SQL analysis

## Databases Created
1. `SQLiteMagic.db` - International student test scores
2. `chicago.db` - Chicago community socioeconomic data
3. `company.db` - Employee/Department HR data

## Key Findings
- SQL + pandas = powerful analytical combination
- JOINs enable relational analysis across tables
- Aggregations reveal patterns invisible in raw data
- Chicago hardship index correlates with income & unemployment
