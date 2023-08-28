from stl import mesh
import numpy as np
import math

# Load the STL files
your_mesh = mesh.Mesh.from_file('input.stl')

# Define rotation matrix (rotation around X-axis)
angle = 45 # or whatever angle you wish
angle = math.radians(angle) # converting to radians

rotation_matrix = np.array([
    [1, 0, 0],
    [0, math.cos(angle), -math.sin(angle)],
    [0, math.sin(angle), math.cos(angle)]
])

# Apply the rotation to the mesh
your_mesh.rotate([1, 0, 0], angle)

# Save as a new STL file
your_mesh.save('new_file.stl')
