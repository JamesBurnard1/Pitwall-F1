import pandas as pd
import fastf1
CACHE_DIR = "/Users/jamesburnard/Desktop/Projects/Pitwall-F1/cache"
fastf1.Cache.enable_cache(CACHE_DIR)



year = 2024
gp = 'Silverstone'
# Define the sessions across the different days
days_sessions = ['FP1', 'FP2', 'FP3', 'Q', 'R'] 

# Dictionary to hold the data frames for each day
all_weekend_laps = {}

# 2. Loop through each session type
for session_type in days_sessions:
    print(f"Loading {gp} - {session_type}...")
    
    # Get and load the specific day's session
    session = fastf1.get_session(year, gp, session_type)
    session.load()
    
    # Store the lap data into our dictionary
    all_weekend_laps[session_type] = session.laps

# Now you can easily look at any day you want!
print(all_weekend_laps['Q'].head())







