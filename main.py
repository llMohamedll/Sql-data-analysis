"""
Project 05: SQL for Data Analysis
==================================
This script demonstrates SQL operations using Python's sqlite3 and pandas,
including database creation, querying, joins, aggregations, and analysis.

Original notebooks: 4 notebooks combined
- DB0201EN-Week3-1-3-SQLmagic-SQlite-v2.ipynb
- DB0201EN-Week3-1-4-Analyzing-SQLite-v2.ipynb
- DB0201EN-Week4-1-1-RealDataPractice-v5-sqlite-Learner-v2(Edited).ipynb
- Week4-Insert-Update-SQLite-v2.ipynb

Author: Data Analysis Portfolio
"""

import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# ================================================================================
# DATABASE SETUP
# ================================================================================

def create_databases():
    """Create sample databases for demonstration."""
    
    # Database 1: International Student Test Scores
    conn1 = sqlite3.connect("SQLiteMagic.db")
    cursor1 = conn1.cursor()
    
    cursor1.execute("""
        CREATE TABLE IF NOT EXISTS INTERNATIONAL_STUDENT_TEST_SCORES (
            country VARCHAR(50),
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            test_score INT
        )
    """)
    
    sample_data = [
        ('United States', 'Marshall', 'Bernadot', 54), ('Ghana', 'Celinda', 'Malkin', 51),
        ('Ukraine', 'Guillermo', 'Furze', 53), ('Greece', 'Aharon', 'Tunnow', 48),
        ('Russia', 'Bail', 'Goodwin', 46), ('Poland', 'Cole', 'Winteringham', 49),
        ('Sweden', 'Emlyn', 'Erricker', 55), ('Russia', 'Cathee', 'Sivewright', 49),
        ('China', 'Barny', 'Ingerson', 57), ('Uganda', 'Sharla', 'Papaccio', 55),
        ('China', 'Stella', 'Youens', 51), ('Poland', 'Julio', 'Buesden', 48),
        ('United States', 'Tiffie', 'Cosely', 58), ('Poland', 'Auroora', 'Stiffell', 45),
        ('China', 'Clarita', 'Huet', 52), ('Poland', 'Shannon', 'Goulden', 45),
        ('Philippines', 'Emylee', 'Privost', 50), ('France', 'Madelina', 'Burk', 49),
        ('China', 'Saunderson', 'Root', 58), ('Indonesia', 'Bo', 'Waring', 55),
        ('China', 'Hollis', 'Domotor', 45), ('Russia', 'Robbie', 'Collip', 46),
        ('Philippines', 'Davon', 'Donisi', 46), ('China', 'Cristabel', 'Radeliffe', 48),
        ('China', 'Wallis', 'Bartleet', 58), ('Moldova', 'Arleen', 'Stailey', 38),
        ('Ireland', 'Mendel', 'Grumble', 58), ('China', 'Sallyann', 'Exley', 51),
        ('Mexico', 'Kain', 'Swaite', 46), ('Indonesia', 'Alonso', 'Bulteel', 45),
        ('Armenia', 'Anatol', 'Tankus', 51), ('Indonesia', 'Coralyn', 'Dawkins', 48),
        ('China', 'Deanne', 'Edwinson', 45), ('China', 'Georgiana', 'Epple', 51),
        ('Portugal', 'Bartlet', 'Breese', 56), ('Azerbaijan', 'Idalina', 'Lukash', 50),
        ('France', 'Livvie', 'Flory', 54), ('Malaysia', 'Nonie', 'Borit', 48),
        ('Indonesia', 'Clio', 'Mugg', 47), ('Brazil', 'Westley', 'Measor', 48),
        ('Philippines', 'Katrinka', 'Sibbert', 51), ('Poland', 'Valentia', 'Mounch', 50),
        ('Norway', 'Sheilah', 'Hedditch', 53), ('Papua New Guinea', 'Itch', 'Jubb', 50),
        ('Latvia', 'Stesha', 'Garnson', 53), ('Canada', 'Cristionna', 'Wadmore', 46),
        ('China', 'Lianna', 'Gatward', 43), ('Guatemala', 'Tanney', 'Vials', 48),
        ('France', 'Alma', 'Zavittieri', 44), ('China', 'Alvira', 'Tamas', 50),
        ('United States', 'Shanon', 'Peres', 45), ('Sweden', 'Maisey', 'Lynas', 53),
        ('Indonesia', 'Kip', 'Hothersall', 46), ('China', 'Cash', 'Landis', 48),
        ('Panama', 'Kennith', 'Digance', 45), ('China', 'Ulberto', 'Riggeard', 48),
        ('Switzerland', 'Judy', 'Gilligan', 49), ('Philippines', 'Tod', 'Trevaskus', 52),
        ('Brazil', 'Herold', 'Heggs', 44), ('Latvia', 'Verney', 'Note', 50),
        ('Poland', 'Temp', 'Ribey', 50), ('China', 'Conroy', 'Egdal', 48),
        ('Japan', 'Gabie', 'Alessandone', 47),
    ]
    
    cursor1.executemany(
        "INSERT OR REPLACE INTO INTERNATIONAL_STUDENT_TEST_SCORES VALUES (?, ?, ?, ?)",
        sample_data
    )
    conn1.commit()
    conn1.close()
    
    # Database 2: Chicago Socioeconomic Data
    conn2 = sqlite3.connect("chicago.db")
    cursor2 = conn2.cursor()
    
    cursor2.execute("""
        CREATE TABLE IF NOT EXISTS CHICAGO_SOCIOECONOMIC (
            community_area_number INT,
            community_area_name TEXT,
            population INT,
            per_capita_income REAL,
            hardship_index INT,
            unemployment_rate REAL,
            below_poverty REAL,
            crowded_housing REAL,
            dependency REAL,
            no_diploma REAL
        )
    """)
    
    # Generate sample Chicago data
    np.random.seed(42)
    chicago_data = []
    for i in range(1, 78):
        chicago_data.append((
            i, f"Community_{i}",
            np.random.randint(10000, 100000),
            np.random.randint(15000, 80000),
            np.random.randint(1, 100),
            np.random.uniform(2, 20),
            np.random.uniform(5, 40),
            np.random.uniform(1, 15),
            np.random.uniform(20, 50),
            np.random.uniform(5, 30)
        ))
    
    cursor2.executemany(
        "INSERT OR REPLACE INTO CHICAGO_SOCIOECONOMIC VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        chicago_data
    )
    conn2.commit()
    conn2.close()
    
    # Database 3: Employee/Department for JOINs
    conn3 = sqlite3.connect("company.db")
    cursor3 = conn3.cursor()
    
    cursor3.execute("""
        CREATE TABLE IF NOT EXISTS DEPARTMENTS (
            dept_id INT PRIMARY KEY,
            dept_name TEXT,
            location TEXT
        )
    """)
    
    cursor3.execute("""
        CREATE TABLE IF NOT EXISTS EMPLOYEES (
            emp_id INT PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            hire_date TEXT,
            salary REAL,
            dept_id INT,
            FOREIGN KEY (dept_id) REFERENCES DEPARTMENTS(dept_id)
        )
    """)
    
    dept_data = [
        (1, 'Engineering', 'San Francisco'),
        (2, 'Marketing', 'New York'),
        (3, 'Sales', 'Chicago'),
        (4, 'HR', 'Boston'),
        (5, 'Finance', 'Seattle'),
    ]
    
    emp_data = [
        (101, 'John', 'Smith', 'john@company.com', '2020-01-15', 95000, 1),
        (102, 'Jane', 'Doe', 'jane@company.com', '2019-03-22', 87000, 1),
        (103, 'Bob', 'Wilson', 'bob@company.com', '2021-06-10', 72000, 2),
        (104, 'Alice', 'Brown', 'alice@company.com', '2018-11-05', 91000, 3),
        (105, 'Charlie', 'Davis', 'charlie@company.com', '2022-02-28', 68000, 2),
        (106, 'Diana', 'Miller', 'diana@company.com', '2020-09-12', 83000, 4),
        (107, 'Eve', 'Garcia', 'eve@company.com', '2019-07-18', 79000, 5),
        (108, 'Frank', 'Martinez', 'frank@company.com', '2021-11-30', 75000, 1),
        (109, 'Grace', 'Lee', 'grace@company.com', '2018-05-25', 88000, 3),
        (110, 'Henry', 'Taylor', 'henry@company.com', '2022-01-10', 71000, 4),
    ]
    
    cursor3.executemany("INSERT OR REPLACE INTO DEPARTMENTS VALUES (?, ?, ?)", dept_data)
    cursor3.executemany("INSERT OR REPLACE INTO EMPLOYEES VALUES (?, ?, ?, ?, ?, ?, ?)", emp_data)
    conn3.commit()
    conn3.close()
    
    print("All databases created successfully!")

# ================================================================================
# SQL OPERATIONS WITH PANDAS
# ================================================================================

def basic_queries():
    """Demonstrate basic SQL queries with pandas."""
    print("\n" + "=" * 50)
    print("BASIC SQL QUERIES")
    print("=" * 50)
    
    conn = sqlite3.connect("SQLiteMagic.db")
    
    # SELECT all
    df = pd.read_sql_query("SELECT * FROM INTERNATIONAL_STUDENT_TEST_SCORES", conn)
    print(f"Total records: {len(df)}")
    print(df.head(10))
    
    # SELECT with WHERE
    df_china = pd.read_sql_query(
        "SELECT * FROM INTERNATIONAL_STUDENT_TEST_SCORES WHERE country = 'China'", conn
    )
    print(f"\nChinese students: {len(df_china)}")
    print(df_china)
    
    # SELECT with ORDER BY
    df_sorted = pd.read_sql_query(
        "SELECT * FROM INTERNATIONAL_STUDENT_TEST_SCORES ORDER BY test_score DESC", conn
    )
    print("\nTop 10 scores:")
    print(df_sorted.head(10))
    
    conn.close()

def aggregation_queries():
    """Demonstrate aggregation queries."""
    print("\n" + "=" * 50)
    print("AGGREGATION QUERIES")
    print("=" * 50)
    
    conn = sqlite3.connect("SQLiteMagic.db")
    
    # COUNT, AVG, GROUP BY
    df_stats = pd.read_sql_query("""
        SELECT country, 
               COUNT(*) as student_count, 
               AVG(test_score) as avg_score,
               MIN(test_score) as min_score,
               MAX(test_score) as max_score
        FROM INTERNATIONAL_STUDENT_TEST_SCORES
        GROUP BY country
        ORDER BY avg_score DESC
    """, conn)
    print("Country statistics:")
    print(df_stats)
    
    # HAVING clause
    df_having = pd.read_sql_query("""
        SELECT country, COUNT(*) as cnt, AVG(test_score) as avg_score
        FROM INTERNATIONAL_STUDENT_TEST_SCORES
        GROUP BY country
        HAVING COUNT(*) > 3
        ORDER BY avg_score DESC
    """, conn)
    print("\nCountries with >3 students:")
    print(df_having)
    
    conn.close()

def join_queries():
    """Demonstrate JOIN operations."""
    print("\n" + "=" * 50)
    print("JOIN OPERATIONS")
    print("=" * 50)
    
    conn = sqlite3.connect("company.db")
    
    # INNER JOIN
    df_inner = pd.read_sql_query("""
        SELECT e.first_name, e.last_name, e.salary, d.dept_name, d.location
        FROM EMPLOYEES e
        INNER JOIN DEPARTMENTS d ON e.dept_id = d.dept_id
    """, conn)
    print("INNER JOIN - Employees with Departments:")
    print(df_inner)
    
    # LEFT JOIN
    df_left = pd.read_sql_query("""
        SELECT d.dept_name, COUNT(e.emp_id) as employee_count
        FROM DEPARTMENTS d
        LEFT JOIN EMPLOYEES e ON d.dept_id = e.dept_id
        GROUP BY d.dept_name
    """, conn)
    print("\nLEFT JOIN - Department employee counts:")
    print(df_left)
    
    # Salary analysis by department
    df_salary = pd.read_sql_query("""
        SELECT d.dept_name, 
               AVG(e.salary) as avg_salary,
               MIN(e.salary) as min_salary,
               MAX(e.salary) as max_salary
        FROM EMPLOYEES e
        INNER JOIN DEPARTMENTS d ON e.dept_id = d.dept_id
        GROUP BY d.dept_name
        ORDER BY avg_salary DESC
    """, conn)
    print("\nSalary by Department:")
    print(df_salary)
    
    conn.close()

def chicago_analysis():
    """Analyze Chicago socioeconomic data."""
    print("\n" + "=" * 50)
    print("CHICAGO SOCIOECONOMIC ANALYSIS")
    print("=" * 50)
    
    conn = sqlite3.connect("chicago.db")
    
    # Basic stats
    df = pd.read_sql_query("SELECT * FROM CHICAGO_SOCIOECONOMIC", conn)
    print(f"Total communities: {len(df)}")
    print(df.describe())
    
    # Top 10 by hardship index
    df_hardship = pd.read_sql_query("""
        SELECT community_area_name, hardship_index, per_capita_income, unemployment_rate
        FROM CHICAGO_SOCIOECONOMIC
        ORDER BY hardship_index DESC
        LIMIT 10
    """, conn)
    print("\nTop 10 Communities by Hardship Index:")
    print(df_hardship)
    
    # Correlation analysis using pandas
    numeric_df = df.select_dtypes(include=[np.number])
    corr = numeric_df.corr()
    print("\nCorrelation with Hardship Index:")
    print(corr['hardship_index'].sort_values(ascending=False))
    
    # Visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    axes[0, 0].hist(df['hardship_index'], bins=20, edgecolor='black', alpha=0.7)
    axes[0, 0].set_title('Hardship Index Distribution')
    
    axes[0, 1].scatter(df['per_capita_income'], df['hardship_index'], alpha=0.6)
    axes[0, 1].set_title('Income vs Hardship')
    axes[0, 1].set_xlabel('Per Capita Income')
    axes[0, 1].set_ylabel('Hardship Index')
    
    axes[1, 0].scatter(df['unemployment_rate'], df['hardship_index'], alpha=0.6, color='orange')
    axes[1, 0].set_title('Unemployment vs Hardship')
    axes[1, 0].set_xlabel('Unemployment Rate')
    axes[1, 0].set_ylabel('Hardship Index')
    
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, 
                ax=axes[1, 1], cbar_kws={'shrink': 0.8})
    axes[1, 1].set_title('Correlation Matrix')
    
    plt.tight_layout()
    plt.savefig('chicago_sql_analysis.png', dpi=150, bbox_inches='tight')
    print("Saved chicago_sql_analysis.png")
    plt.close()
    
    conn.close()

def crud_operations():
    """Demonstrate CREATE, READ, UPDATE, DELETE operations."""
    print("\n" + "=" * 50)
    print("CRUD OPERATIONS")
    print("=" * 50)
    
    conn = sqlite3.connect("SQLiteMagic.db")
    cursor = conn.cursor()
    
    # CREATE (INSERT)
    cursor.execute("""
        INSERT INTO INTERNATIONAL_STUDENT_TEST_SCORES 
        (country, first_name, last_name, test_score)
        VALUES ('Canada', 'Test', 'User', 99)
    """)
    print(f"Inserted 1 row. Total rows: {cursor.rowcount}")
    
    # READ
    df = pd.read_sql_query("SELECT * FROM INTERNATIONAL_STUDENT_TEST_SCORES WHERE country = 'Canada'", conn)
    print("New record:")
    print(df)
    
    # UPDATE
    cursor.execute("""
        UPDATE INTERNATIONAL_STUDENT_TEST_SCORES
        SET test_score = 100
        WHERE country = 'Canada' AND first_name = 'Test'
    """)
    print(f"Updated {cursor.rowcount} rows")
    
    # READ after update
    df = pd.read_sql_query("SELECT * FROM INTERNATIONAL_STUDENT_TEST_SCORES WHERE country = 'Canada'", conn)
    print("After update:")
    print(df)
    
    # DELETE
    cursor.execute("""
        DELETE FROM INTERNATIONAL_STUDENT_TEST_SCORES
        WHERE country = 'Canada' AND first_name = 'Test'
    """)
    print(f"Deleted {cursor.rowcount} rows")
    
    conn.commit()
    conn.close()

# ================================================================================
# MAIN EXECUTION
# ================================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("PROJECT 05: SQL FOR DATA ANALYSIS")
    print("=" * 60)
    
    # Setup databases
    print("\n[1] Creating databases...")
    create_databases()
    
    # Basic queries
    print("\n[2] Basic queries...")
    basic_queries()
    
    # Aggregation
    print("\n[3] Aggregation queries...")
    aggregation_queries()
    
    # Joins
    print("\n[4] Join operations...")
    join_queries()
    
    # Chicago analysis
    print("\n[5] Chicago socioeconomic analysis...")
    chicago_analysis()
    
    # CRUD
    print("\n[6] CRUD operations...")
    crud_operations()
    
    print("\n" + "=" * 60)
    print("ALL SQL OPERATIONS COMPLETE")
    print("=" * 60)
