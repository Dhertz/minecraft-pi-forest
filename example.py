from tree_sim import *

clear_area()

c = 10
for i in range(-4, 4):
  for j in range(-4, 4):
    make_tree(c*j, c*i,2,3,sphere)

teleport_home()
