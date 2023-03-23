import pydobot
import dobot_tools

dobot_port = ""
device = pydobot.Dobot(port=dobot_port)

#device.move_to(100, 0, 0, 0, wait=True)
(x, y, z, r, j1, j2, j3, j4) = device.pose()

device._set_end_effector_suction_cup(enable=True)
 
for i in range(3):
    device.move_to(x + 50, y-200, z-195, r-100, wait=True)
    print(device.pose())
    device.suck(enable=True)
    device.wait(1000)
    device.move_to(x, y, z, r, wait=True)
    print(device.pose())
    device.suck(enable=False)
    device.wait(1000)


device.close()
