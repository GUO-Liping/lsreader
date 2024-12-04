import numpy as np
import re

# Function to parse the data from the file
def parse_data(filename):
    # Dictionary to store forces data for each time step
    time_forces = {}

    # Open the data file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Initialize variables
    current_time = None
    forces_data = {}

    # Regular expression to capture forces for each node
    force_pattern = re.compile(r"node=\s*(\d+)\s+local\s+x,y,z\s+forces\s*=\s*([\d\.\-E\+]+)\s+([\d\.\-E\+]+)\s+([\d\.\-E\+]+)")

    # Loop over lines in the file
    for line in lines:
        # Capture the time step information
        if "output at time" in line:
            # Extract time step
            time_match = re.search(r"output at time =\s*([\d\.E\+\-]+)", line)
            if time_match:
                current_time = float(time_match.group(1))
                forces_data = {}  # Reset forces for the new time step

        # Capture the forces for each node
        match = force_pattern.search(line)
        if match:
            node_id = int(match.group(1))
            forces = np.array([float(match.group(2)), float(match.group(3)), float(match.group(4))])
            forces_data[node_id] = forces

        # If we have parsed forces for all nodes in a time step, save it
        if current_time is not None and forces_data:
            time_forces[current_time] = forces_data

    return time_forces

# Function to extract forces for a specific node across all time steps
def extract_forces(time_forces, node_id):
    # Lists to store forces (x, y, z) along the time steps
    x_forces = []
    y_forces = []
    z_forces = []
    
    # Extract forces for the specified node across all time steps
    for time_step in sorted(time_forces.keys()):
        if node_id in time_forces[time_step]:
            forces = time_forces[time_step][node_id]
            x_forces.append(forces[0])
            y_forces.append(forces[1])
            z_forces.append(forces[2])

    # Convert lists to np.array for the specified node
    x_forces = np.array(x_forces)
    y_forces = np.array(y_forces)
    z_forces = np.array(z_forces)

    return x_forces, y_forces, z_forces

# Example usage
filename = 'data.txt'  # Replace with your actual file path
time_forces = parse_data(filename)

# Extract forces for node 58307 along the time steps
node_id = 58307
x_forces, y_forces, z_forces = extract_forces(time_forces, node_id)

# Output the forces as numpy arrays
print(f'Node {node_id} x forces: {x_forces}')
print(f'Node {node_id} y forces: {y_forces}')
print(f'Node {node_id} z forces: {z_forces}')
