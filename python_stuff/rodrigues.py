# Rodrigues formula:  v_rot = v * cos(theta) + (k x v) * sin(theta) + k * (k . v) * (1 - cos(theta))
import math
import numpy as np
import matplotlib.pyplot as plt


def rodrigues_rotation(v, k, theta):

    v = np.array(v)
    k = np.array(k) / np.linalg.norm(k)

    v_rot = (v*math.cos(theta) + np.cross(k, v) * math.sin(theta) +
             k * (k @ v) * (1 - math.cos(theta)))

    return v_rot


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


wow = rodrigues_rotation([6, 8, 3], [0, 0, 1], math.pi/2)
print(np.round(wow, 3))

ax.quiver(0, 0, 0, wow[0], wow[1], wow[2], color='r',
          label='Rotated Vector', arrow_length_ratio=0.1)

ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Rodrigues Rotation')

plt.show()
