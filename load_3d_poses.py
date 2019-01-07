import numpy as np
import cPickle as pk

path = "/content/MVA-DL/hmr.pkl"
f = open(path, 'r')
data = pk.load(f)

print(data.keys()) # ['thetas', 'poses', 'cams', 'shapes', 'joint_2d_positions', 'trans']

print(data['poses']) # (210, 72) 210 frames, each row contains a 72d SMPL pose vector
# 24 spherical joints, each represented by a 3d axis-angle vector, results the 72d pose vector

print(data['shapes'].shape) # (210, 10) each row contains a 10d SMPL shape vector

print(data['cams'].shape) # (210, 3) each row contains the camera translation
# we assume that the camera is fixed in front of the scene, with identity rotation

# please refer to SMPL project page on how to get 3D joint positions from SMPL pose and shape vectors:
# http://smpl.is.tue.mpg.de/
