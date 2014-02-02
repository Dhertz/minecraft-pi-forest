from minecraft import minecraft, block
from math import sqrt

def clear_area(size):
  mc = minecraft.Minecraft.create()
  mc.setBlocks(-size/2, -6, -size/2, size/2, -2, size/2, block.DIRT)
  mc.setBlocks(-size/2, -1, -size/2, size/2, -1, size/2, block.GRASS)
  mc.setBlocks(-size/2, 0, -size/2, size/2, 60, size/2, block.AIR)

def teleport_home():
  mc = minecraft.Minecraft.create()
  mc.player.setTilePos(1,0,0)

### Non-funcitonal ###
def make_fire(x,z):
  mc = minecraft.Minecraft.create()
  #mc.setBlock(x, 1, z, block.FIRE) 
  block = mc.getBlockWithData(x, 1, z);
  block.data = (block.data + 1) & 0xf;

### xt  - x coord
### zt  - z coord (no height coord, everything is on 0)
### r   - 'radius' of shape - from trunk to edge in most cases
### t   - trunk height
### alg - generator to create shape, see below for options
def make_tree(xt, zt, r, t, alg):
  mc = minecraft.Minecraft.create()
  for x, y, z in alg(xt, t+r, zt, r):
    mc.setBlock(x, y, z, block.LEAVES)
  mc.setBlocks(xt, 0 ,zt, xt, t+r, zt, block.WOOD)


### Generators for the make_tree function - pass in as last argument ###
def sphere(x,y,z,r):
  for i in range(x-r**2,x+r**2):
    for j in range(y-r**2,y+r**2):
        for k in range(z-r**2,z+r**2):
            if(sqrt((i - x)**2 + (j - y)**2 + (k - z)**2) <= r):
              yield i, j, k

def stripey(x,y,z,r):
  for j in range(1, (y+r)/3):
    for i in range(x-r,x+r+1):
      for k in range(z-r, z+r+1):
         yield i, j*3, k


def cube(x,y,z,r):
 for i in range(x-r,x+r+1):
    for j in range(y-r,y+r+1):
      for k in range(z-r,z+r+1):
        yield i, j, k

def cone(x,y,z,r):
  for i in range(x-r**2,x+r**2+1):
    for j in range(y-r**2,y+r**2+1):
      for k in range(z-r**2,z+1):
        if((i - x)**2 + (j - y)**2 <= (k - z)**2):
          yield i, y-z+k+1, j-(y-z) 

def xmas(x,y,z,r):
  for i in range(1, 4):
    for j in cone(x, i*3+r, z, 2):
      yield j

if __name__ == '__main__':
  clear_area(60)
#   teleport_home()
  make_tree(-15,0,3,2, make_sphere)
  make_tree(-10,5,1,2,make_cube)
  make_tree(-5,0,3,10,make_stripey)
  make_tree(0,5,2,4,make_cone)
  make_tree(5,0,2,4,make_xmas)
