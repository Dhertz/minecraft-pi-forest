from minecraft import minecraft, block
from math import sqrt

class Minecraft(object):

  mc = minecraft.Minecraft.create()
  bounds = 100

def clear_area():
  size = Minecraft.bounds
  Minecraft.mc.setBlocks(-size/2, -6, -size/2, size/2, -2, size/2, block.DIRT)
  Minecraft.mc.setBlocks(-size/2, -1, -size/2, size/2, -1, size/2, block.GRASS)
  Minecraft.mc.setBlocks(-size/2, 0, -size/2, size/2, 60, size/2, block.AIR)

def teleport_home():
  Minecraft.mc = minecraft.Minecraft.create()
  Minecraft.mc.player.setTilePos(1,0,0)

### Non-funcitonal ###
def make_fire(x,z):
  #mc.setBlock(x, 1, z, block.FIRE) 
  block = Minecraft.mc.getBlockWithData(x, 1, z);
  block.data = (block.data + 1) & 0xf;

### xt  - x coord
### zt  - z coord (no height coord, everything is on 0)
### r   - 'radius' of shape - from trunk to edge in most cases
### t   - trunk height
### alg - generator to create shape, see below for options
def make_tree(xt, zt, r, t, alg):
  assert xt < Minecraft.bounds/2 and xt > -Minecraft.bounds/2, "x coord is not in bounds: %i" % xt
  assert zt < Minecraft.bounds/2 and zt > -Minecraft.bounds/2, "z coord is not in bounds: %i" % zt
  assert r < 5, "radius is too large"
  assert t < 20, "trunk is too large"
  for x, y, z in alg(xt, t+r, zt, r):
    Minecraft.mc.setBlock(x, y, z, block.LEAVES)
  Minecraft.mc.setBlocks(xt, 0 ,zt, xt, t+r, zt, block.WOOD)


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

def put_block(x,z,blocktype):
  assert x < Minecraft.bounds/2 and x > -Minecraft.bounds/2, "x coord is not in bounds: %i" % x
  assert z < Minecraft.bounds/2 and z > -Minecraft.bounds/2, "z coord is not in bounds: %i" % z
  Minecraft.mc.setBlock(x, 0, z, blocktype)
