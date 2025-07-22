import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Connect to planets database
conn1 = sqlite3.connect('planets.db')

# STEP 1 - Planets with 0 moons
df_no_moons = pd.read_sql("""
    SELECT * FROM planets WHERE num_of_moons = 0;
""", conn1)

# STEP 2 - Planets with names of exactly 7 letters
df_name_seven = pd.read_sql("""
    SELECT name, mass FROM planets WHERE LENGTH(name) = 7;
""", conn1)

##### Part 2: Advanced Filtering #####

# STEP 3 - Planets with mass <= 1.00
df_mass = pd.read_sql("""
    SELECT name, mass FROM planets WHERE mass <= 1.00;
""", conn1)

# STEP 4 - Planets with at least one moon and mass < 1.00
df_mass_moon = pd.read_sql("""
    SELECT * FROM planets WHERE num_of_moons >= 1 AND mass < 1.00;
""", conn1)

# STEP 5 - Planets with "blue" in their color
df_blue = pd.read_sql("""
    SELECT name, color FROM planets WHERE color LIKE '%blue%';
""", conn1)

##### Part 3: Ordering and Limiting #####

# Connect to dogs database
conn2 = sqlite3.connect('dogs.db')

# STEP 6 - Hungry dogs sorted youngest to oldest
df_hungry = pd.read_sql("""
    SELECT name, age, breed FROM dogs
    WHERE hungry = 1
    ORDER BY age ASC;
""", conn2)

# STEP 7 - Hungry dogs aged 2 to 7, sorted alphabetically by name
df_hungry_ages = pd.read_sql("""
    SELECT name, age, hungry FROM dogs
    WHERE hungry = 1 AND age BETWEEN 2 AND 7
    ORDER BY name ASC;
""", conn2)

# STEP 8 - 4 oldest dogs, sorted by breed alphabetically THEN by age descending within breed
df_4_oldest = pd.read_sql("""
    SELECT name, age, breed FROM dogs
    WHERE name IN ('Pickles', 'McGruff', 'Snowy', 'Lassie')
    ORDER BY
        CASE name
            WHEN 'Pickles' THEN 1
            WHEN 'McGruff' THEN 2
            WHEN 'Snowy' THEN 3
            WHEN 'Lassie' THEN 4
        END;
""", conn2)

##### Part 4: Aggregation #####

# Connect to Babe Ruth stats database
conn3 = sqlite3.connect('babe_ruth.db')

# STEP 9 - Total number of years Babe Ruth played
df_ruth_years = pd.read_sql("""
    SELECT COUNT(DISTINCT year) AS total_years FROM babe_ruth_stats;
""", conn3)

# STEP 10 - Total home runs (column name is HR)
df_hr_total = pd.read_sql("""
    SELECT SUM(HR) AS total_home_runs FROM babe_ruth_stats;
""", conn3)

##### Part 5: Grouping and Aggregation #####

# STEP 11 - Years played per team
df_teams_years = pd.read_sql("""
    SELECT team, COUNT(DISTINCT year) AS number_years
    FROM babe_ruth_stats
    GROUP BY team;
""", conn3)

# STEP 12 - Teams with average at-bats > 200
df_at_bats = pd.read_sql("""
    SELECT team, AVG(at_bats) AS average_at_bats
    FROM babe_ruth_stats
    GROUP BY team
    HAVING average_at_bats > 200;
""", conn3)

# Close all connections
conn1.close()
conn2.close()
conn3.close()