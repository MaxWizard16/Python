import numpy as np

import pandas as pd

########### Part 1: Sensor Data Analysis ###########

# Load sensor data

sensor_df = pd.read_csv("sensor_data.csv")

# Calculate average, min, max for each sensor (exclude timestamp)

stats = {}

for sensor in ['temperature', 'distance', 'battery', 'humidity']:

 values = sensor_df[sensor].values

 stats[sensor] = {

 'mean': np.mean(values),

 'min': np.min(values),

 'max': np.max(values)

 }

# Find time when temperature was highest

max_temp_idx = sensor_df['temperature'].idxmax()

max_temp_time = sensor_df.loc[max_temp_idx, 'timestamp']

max_temp_value = sensor_df.loc[max_temp_idx, 'temperature']

# Count battery % below 30

battery_below_30_count = np.sum(sensor_df['battery'].values < 30)

# Save results to output file

sensor_results = {

 'Sensor Mean': {s: stats[s]['mean'] for s in stats},

 'Sensor Min': {s: stats[s]['min'] for s in stats},

 'Sensor Max': {s: stats[s]['max'] for s in stats},

 'Max Temp Time': max_temp_time,

 'Max Temp Value': max_temp_value,

 'Battery < 30 Count': battery_below_30_count

}

sensor_out_df = pd.DataFrame(sensor_results)

sensor_out_df.to_csv("sensor_analysis_output.csv", index=False)

########### Part 2: Robot Path Analysis ###########

# Load robot's positions

robot_positions = pd.read_csv("robot_path.csv")

# Compute total distance travelled (Euclidean distance between points)

coords = robot_positions[['x', 'y']].to_numpy()

diffs = np.diff(coords, axis=0)

distances = np.sqrt(np.sum(diffs**2, axis=1))

total_distance = np.sum(distances)

# The farthest point from origin (0, 0)

dists_from_origin = np.sqrt(np.sum(coords**2, axis=1))

farthest_idx = np.argmax(dists_from_origin)

farthest_point = tuple(coords[farthest_idx])

max_distance_from_origin = dists_from_origin[farthest_idx]

# Detect if robot revisited the same position

# Use tuples for hashing positions

visited = set()

revisited = False

for pos in map(tuple, coords):

 if pos in visited:

 revisited = True

 break

 visited.add(pos)

# Save results to output file

robot_results = {

 'Total Distance': [total_distance],

 'Max Distance from Origin': [max_distance_from_origin],

 'Farthest Point': [farthest_point],

 'Revisited Any Point': [revisited]

}

robot_out_df = pd.DataFrame(robot_results)

robot_out_df.to_csv("robot_path_analysis_output.csv", index=False)

print("Analysis complete. See sensor_analysis_output.csv and robot_path_analysis_output.csv fo