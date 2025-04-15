# Robot Kinematics 6 - Differential Kinematics

## Differential Kinematics
- Velocities of joints and end effector. 
- Whereas direct kinematics is direct transformation from one point to another.

![alt text](imgs/robot_kinematics6/image-1.png)

Direct Kinematics:
![alt text](imgs/robot_kinematics6/image.png)

Differential Kinematics:
![alt text](imgs/robot_kinematics6/image-2.png)

### Forward Differential Kinematics
From velocities of joints to end effector velocities.

### Inverse Differential Kinematics
From end effector velocities to joint velocities.


### Derivative
- Can't just calculate the exact velocities for a given config (would require infinite solutions!) 
- So of course take time derivative!

![alt text](imgs/robot_kinematics6/image-4.png)

![alt text](imgs/robot_kinematics6/image-3.png)

$$
v = J(\theta_1, \theta_2), = J \dot \theta
$$

Where J is the jacbobian of the angles. So when multiplied by the joint velocities, gives the end effector velocity.

![alt text](imgs/robot_kinematics6/image-5.png)


### Forward Differential Kinematics of Cartesian
- Same thing, using jacobian of all the angles, but the pose of the moving frame contains x, y, z, and the angles.
- Therefore 6x1 vector (with position and orientation)
- ![alt text](imgs/robot_kinematics6/image-6.png)

![alt text](imgs/robot_kinematics6/image-7.png)

$$ 
v = J \dot q
$$


### Differential Motions - Wrt to Fixed Frame
- Differential motion wrt to fixed frame, use jacboian of the fixed frame.
- ![alt text](imgs/robot_kinematics6/image-8.png)

![alt text](imgs/robot_kinematics6/image-9.png)


### Torques and Forces

![alt text](imgs/robot_kinematics6/image-10.png)

$$
^HF\text{generalised force} = \text{force} / \text{torque}
$$

![alt text](imgs/robot_kinematics6/image-11.png)

Combination of all forces and displacements of each joint. 


### Virtual Works
- Sum of the **virtual works** done by all the forces / torques  (assume know kinetic energy, friction etc) acting on the system in static equilibrium is zero.
$$
T = J^T F
$$

Where T is the generalised force at joint level, jacobian is the bridge between joing and EE (and any frame), and F is the force at teh end effector


### Duality between velocity and force
Very simiular conversion
![alt text](imgs/robot_kinematics6/image-12.png)