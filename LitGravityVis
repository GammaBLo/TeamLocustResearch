import matplotlib . pyplot as plt
import numpy as np

# Create a three - dimensional coordinate system . fig = 
 plt . figure ()
ax = fig . add_subplot (111, projection = ' 3 d')

# Generate the points in the pentagonal prism . points = 
 np . array ([(0, 0, 0), (0, 0, 1), (0.5, 0.866, 0), (0.5, 0.866, 
    1), (1, 0, 0), (1, 0, 1), (0.5, -0.866, 0), (0.5, -0.866, 1)])

# Create pi logic and pi brane embedded cells . logic = PiLogic ()
cells = PiBraneEmbeddedCells (logic)

# Set the center point to (0, 0, 0) and emit light, gravity, 
and is the modulus of vibrorotation between the other points . 
   center_point = points[0]
cells . set_center _point (center_point)
cells . calculate_light (points)
cells . calculate_gravity (points)
cells . calculate_vibrorotation (points)

# Implement mapping between the points to that the harmony between \
them is consistent with data from particle physics . 
   mapping = {(0, 0, 0) : ' photon', (0, 0, 1) : ' electron', (0.5, 
    0.866, 0) : ' neutron', (0.5, 0.866, 1) : ' quark', (1, 0, 
    0) : ' muon', (1, 0, 1) : ' tau', (0.5, -0.866, 
    0) : ' gluon', (0.5, -0.866, 1) : ' graviton'}

# Plot the points in the coordinate system . for point, 
label in mapping . items () : 
 ax . scatter (point[0], point[1], point[2], label = label)

# Connect the points to create a lattice . ax . 
  plot_wireframe (points[: , 0], points[: , 1], points[: , 2])

# Show the plot . plt . show ()
