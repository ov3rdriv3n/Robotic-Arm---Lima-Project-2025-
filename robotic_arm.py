# simple two link robotic arm inverse kinematics sim
import math
import matplotlib.pyplot as plt

# arm lengths
L1, L2 = 100, 75

# target position (x,y)
x, y = 120, 50

# distance calc
d = math.sqrt(x**2 + y**2)

# inverse kinematics
a = math.acos((L1**2 + d**2 - L2**2) / (2*L1*d))
b = math.atan2(y, x)
theta1 = b - a
theta2 = math.acos((L1**2 + L2**2 - d**2) / (2*L1*L2))

# forward kinematics for plottinh
x0, y0 = 0, 0
x1, y1 = L1*math.cos(theta1), L1*math.sin(theta1)
x2, y2 = x1 + L2*math.cos(theta1), L1*math.sin(theta1)

# plot arm and target
plt.plot([x0, x1, x1], [y0, y1, y2], marker = 'o')
plt.scatter([x], [y], color = 'red') # target
plt.axis('equal')
plt.title("Two Link Robotic Arm Reaching Target")
plt.show()
              
