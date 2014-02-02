from tree_sim import *

clear_area(200)

c = 10
for i in range(-10, 10):
  for j in range(-10, 10):
    make_tree(c*j, c*i,2,3,sphere)

teleport_home()

