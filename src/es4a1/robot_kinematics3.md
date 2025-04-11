# Robot Kinematics 3 - Forward & Inverse Kinematics

## Forward Kinematics (FK)
> Given joint variables, and link parameters, find the pose of the end effector EE

### 2R Planar Arm
Simple geometric inspections to calculate.

![alt text](imgs/robot_kinematics3/image.png)


### FK Cartesian Arm
- 3 transformations in following order (order of translations doesnt matter with cartesian, rotation does.)
  - Translation px along x
  - Translation py along y
  - Translation pz along z

![alt text](imgs/robot_kinematics3/image-1.png)  

### FK of Cylindrical Arm Position
- 3 transformations in following order (order of translations matters with cylindrical)
  - Translation r along x
  - Rotation about z
  - Translation l along z
- All transofmrations relate to fixed frame so premultiply

![alt text](imgs/robot_kinematics3/image-2.png)

### FK of Spherical Arm Position
- 3 transofmrations:
  - Translation r along z
  - Rotation beta about y
  - rotation gamma about z
- All transofmrations relate to fixed frame so premultiply

![alt text](imgs/robot_kinematics3/image-3.png)


## Inverse Kinematics (IK)
> Given the link parameters and desired pose of the EE, find the values of the joint variables that takes the EE to the desired pose.

### 2R Planar Arm
![alt text](imgs/robot_kinematics3/image-4.png)

- Many possible soluitions

![alt text](imgs/robot_kinematics3/image-5.png)

![alt text](imgs/robot_kinematics3/image-6.png)

A soltuion to the IK for teh 2R planar arm if:

$$
l_1 - l_2 \leq \sqrt{p_x^2 + p_y^2} \leq l_1 + l_2
$$

That means it falles within the range.

#### Solutions
2 solutions, elbow up and elbow down.
- From FK, square and sum, do some maths, re arrange
- Get sine and cosines, but cant just inverse sine, need to take consideration of both sides, so use arc atan.
  
![alt text](imgs/robot_kinematics3/image-7.png)

- To find the angle, use the equations but need to seperate cos1cos2 as difficult
- Create linear equiations
- Solve
- Find determinant 
  - If l1 = l2, cos2 = -1, det A = 0
  - Then infinite solutions for theta 1.
  - If $detA <0$
  - Then 
- ![alt text](imgs/robot_kinematics3/image-8.png)


Observatins:
    - ![alt text](imgs/robot_kinematics3/image-9.png)

### Cartesian Arm
Easy, just the point is the inverse!
![alt text](imgs/robot_kinematics3/image-10.png)


### Cylindrical Arm
Relatvily straightforward
![alt text](imgs/robot_kinematics3/image-11.png)

#### aTan2:
![alt text](imgs/robot_kinematics3/image-12.png)

### Spherical Arm
Linear equations

![alt text](imgs/robot_kinematics3/image-13.png)

