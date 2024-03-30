import time
from naoqi import ALProxy

ROBOT_IP = "10.101.0.183"


motion = ALProxy("ALMotion", "nao.local", 9559)

motion.moveInit()

correction_lr = 0
correction_fb = 0

while True :

    motion.post.moveTo(correction_fb, 0 + correction_lr , 0)
    correction_lr= 0
    correction_fb = 0
    # Connect to ALSonar module.
    sonarProxy = ALProxy("ALSonar", ROBOT_IP, 9559)

    # Subscribe to sonars, this will launch sonars (at hardware level) and start data acquisition.
    sonarProxy.subscribe("myApplication")

    #Now you can retrieve sonar data from ALMemory.
    memoryProxy = ALProxy("ALMemory", ROBOT_IP, 9559)

    # Get sonar left first echo (distance in meters to the first obstacle).
    left_sensor = memoryProxy.getData("Device/SubDeviceList/US/Left/Sensor/Value")

    # Same thing for right.
    right_sensor = memoryProxy.getData("Device/SubDeviceList/US/Right/Sensor/Value")
    print("Left" ,left_sensor)
    print("Right", right_sensor)

    if left_sensor <= 0.4 and right_sensor <= 0.4:
        correction_fb = - 0.2

    if left_sensor < right_sensor and left_sensor <= 0.5:
        correction_lr = -0.2
        print("je vais a droitw au prochain")
    if right_sensor < left_sensor and right_sensor <= 0.5:
        correction_lr = +0.2
        print("je vais a gauche au prochain")


motion.post.moveTo(+0.0, 0, 0)