from PIL import Image
import numpy as np
from scipy.spatial import Delaunay
from stl import mesh
import math


def spiral(height,radius,radius2):
  no_points = 10
  no_height_points= 20
  no_curve_points = 5
  spiral_= np.zeros((no_points*no_height_points*no_curve_points,3))
  theta = np.linspace(0.,2.*math.pi,no_points*no_curve_points)
  phi = np.linspace(0.,0.2*math.pi,no_height_points)
  radius_a = np.linspace(radius,radius2,no_height_points)
  height_a= np.linspace(0,height,no_height_points)
  curve_a = np.linspace(0,math.pi,no_curve_points)
  for i,t in enumerate(curve_a):
    curve_a[i] = -0.08*math.sin(curve_a[i])+1
  for j,u in enumerate(phi):
    for i,t in enumerate(theta):
      spiral_[j*no_points*no_curve_points+i,0] = curve_a[i%no_curve_points]*radius_a[j]* math.cos(t+u)
      spiral_[j*no_points*no_curve_points+i,1] = curve_a[i%no_curve_points]*radius_a[j]*math.sin(t+u)
      spiral_[j*no_points*no_curve_points+i,2] = height_a[j]
  return(spiral_)

def cone(height,height2,radius,radius2,x,y):
  no_points = 50
  no_height_points= 5
  cone_= np.zeros((no_points*no_height_points,3))
  theta = np.linspace(0.,2.*math.pi,no_points)
  phi = np.linspace(0.,math.pi,no_height_points)
  radius_a = np.linspace(radius,radius2,no_height_points)
  height_a= np.linspace(height2,height,no_height_points)
  for j,u in enumerate(phi):
    for i,t in enumerate(theta):
      cone_[j*no_points+i,0] =x+radius_a[j]* math.cos(t)
      cone_[j*no_points+i,1] =y+ radius_a[j]*math.sin(t)
      cone_[j*no_points+i,2] = height_a[j]
  return(cone_)


def append_to_point_cloud(points3D,points3D_):
  points3D = np.append(points3D,points3D_,axis=0)
  return(points3D)
  
if __name__ == "__main__":
  height = 70.
  radius = 55
  radius2 = 30

  baseheight = 15
  points3D = np.empty((0,3))
  #create screwholes and append 3D points to foot
  spiral_ = spiral(height,radius,radius2)
  points3D= append_to_point_cloud(points3D,spiral_)
  cone_ = cone(height,baseheight,22,23,0,0)
  points3D= append_to_point_cloud(points3D,cone_)
  cone_ = cone(baseheight,0,2,5.1,15,0)
  points3D= append_to_point_cloud(points3D,cone_)
  cone_ = cone(baseheight,0,2,5.1,-15,0)
  points3D= append_to_point_cloud(points3D,cone_)
  cone_ = cone(baseheight,0,2,5.1,0,15)
  points3D= append_to_point_cloud(points3D,cone_)
  cone_ = cone(baseheight,0,2,5.1,0,-15)
  points3D= append_to_point_cloud(points3D,cone_)
  #define 2D points, as input data for the Delaunay triangulation of U
  points2D=points3D[:,0:2]
  tri = Delaunay(points2D)

  # Create the mesh
  foot = mesh.Mesh(np.zeros(len(tri.simplices), dtype=mesh.Mesh.dtype))

  for i, f in enumerate(tri.simplices):
    for j in range(3):
      foot.vectors[i][j] = points3D[f[j],:]

  foot.save('decagon_cone.stl')
  print("done")


