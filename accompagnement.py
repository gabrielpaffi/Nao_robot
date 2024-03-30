from naoqi import ALProxy

# Set the IP address of your NAO robot
#ROBOT_IP = "10.101.0.183"
ROBOT_IP =  "192.168.90.236"
import time
import math

# Create a proxy for the tactile touch module
tactile_touch = ALProxy("ALTouch", ROBOT_IP, 9559)
tts = ALProxy("ALTextToSpeech", ROBOT_IP, 9559)
motion = ALProxy("ALMotion", "nao.local", 9559)

joint_names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]


shoulder_pitch_angle = math.radians(-25)  # Angle du bras par rapport au torse (90 degres)
shoulder_roll_angle = math.radians(70)     # Rotation du bras par rapport au torse (0 degres)
elbow_yaw_angle = math.radians(60)         # Angle du coude par rapport au torse (0 degres)
elbow_roll_angle = math.radians(0)        # Rotation du coude (0 degres)
wrist_yaw_angle = math.radians(40)         # Angle du poignet (0 degres)
finger_angles = 1

speed_fraction = 0.1

# Subscribe to tactile touch events
a = tactile_touch.getStatus()
print(a[7])

if a[8][1] == False:
    print("ok")


counter = 0
tts.say("Debut du programme")

while True :
    
    a = tactile_touch.getStatus()
    if a[7][1] == True:
        

        while  True:
            tts.say("Allez viens avec moi, je te montre le chemin vers ta salle")
            
            turn_angle = 3.14159  # 180 degrees in radians
            turn_angle_right = -turn_angle
            semi_turn_right = turn_angle_right/2
            turn_angle_left = turn_angle*0.80
            semi_turn_left = turn_angle_left/2
            height_turn = semi_turn_right/9

            id = motion.post.moveTo(0, 0, turn_angle_left)
            motion.wait(id, 0)

            id = motion.post.moveTo(0, 0 , semi_turn_right)
            motion.wait(id, 0)

            motion.setAngles(joint_names, [shoulder_pitch_angle, shoulder_roll_angle, elbow_yaw_angle, elbow_roll_angle, wrist_yaw_angle, finger_angles], speed_fraction, stiffness = 1)
            tts.say("A droite se trouve la petite section")
            time.sleep(2)

            id = motion.post.moveTo(0, 0 , semi_turn_left)
            motion.wait(id, 0)


            id = motion.post.moveTo(0.5, -0.08 , 0)
            motion.wait(id, 0)

            id = motion.post.moveTo(0, 0 , height_turn)
            motion.wait(id, 0)

            id = motion.post.moveTo(0.5, -0.08 , 0)
            motion.wait(id, 0)


            id = motion.post.moveTo(0, 0 , height_turn)
            motion.wait(id, 0)

            id = motion.post.moveTo(0.5, -0.08 , 0)
            motion.wait(id, 0)


            id = motion.post.moveTo(0, 0 , height_turn)
            motion.wait(id, 0)

          
            id = motion.post.moveTo(0.5, -0.08, 0)
            motion.wait(id, 0)


            id = motion.post.moveTo(0, 0 , height_turn)
            motion.wait(id, 0)

            id = motion.post.moveTo(0.5, -0.08 , 0)
            motion.wait(id, 0)


            id = motion.post.moveTo(0, 0 , height_turn)
            motion.wait(id, 0)

            id = motion.post.moveTo(0.5, -0.1 , 0)
            motion.wait(id, 0)

            id = motion.post.moveTo(0, 0 , height_turn)
            motion.wait(id, 0)


            id = motion.post.moveTo(0.5, -0.1, 0)
            motion.wait(id, 0)

            id = motion.post.moveTo(0, 0 , height_turn)
            motion.wait(id, 0)

            id = motion.post.moveTo(0.5, -0.1 , 0)
            motion.wait(id, 0)

            id = motion.post.moveTo(0, 0 , height_turn*1.5)
            motion.wait(id, 0)
            
            id = motion.post.moveTo(0, 0 , semi_turn_right)
            motion.wait(id, 0)
            motion.setAngles(joint_names, [shoulder_pitch_angle, shoulder_roll_angle, elbow_yaw_angle, elbow_roll_angle, wrist_yaw_angle, finger_angles], speed_fraction, stiffness = 1)
            tts.say("Pour les plus jeunes, allez  a  droite a  la nursery et au mini trotteur")


            id = motion.post.moveTo(0, 0 , turn_angle_left)
            motion.wait(id, 0)
            motion.setAngles(joint_names, [shoulder_pitch_angle, shoulder_roll_angle, elbow_yaw_angle, elbow_roll_angle, wrist_yaw_angle, finger_angles], speed_fraction, stiffness = 1)
            tts.say("Pour les trotteur et les grands allez a gauche")
            time.sleep(3)
            tts.say("Bonne journer !")
            

            id = motion.post.moveTo(0,0, semi_turn_left)
            motion.wait(id, 0)

            id = motion.post.moveTo(0.5, -0.08 , 0)
            motion.wait(id, 0)

            id = motion.post.moveTo(0, 0 , height_turn)
            motion.wait(id, 0)

            id = motion.post.moveTo(0.5, -0.08 , 0)
            motion.wait(id, 0)


            id = motion.post.moveTo(0, 0 , height_turn)
            motion.wait(id, 0)

            id = motion.post.moveTo(0.5, -0.08 , 0)
            motion.wait(id, 0)


            id = motion.post.moveTo(0, 0 , height_turn)
            motion.wait(id, 0)

            id = motion.post.moveTo(0.5, -0.08 , 0)
            motion.wait(id, 0)

            id = motion.post.moveTo(0, 0 , height_turn)
            motion.wait(id, 0)

            id = motion.post.moveTo(0.5, -0.08 , 0)
            motion.wait(id, 0)


            id = motion.post.moveTo(0, 0 , height_turn)
            motion.wait(id, 0)

            id = motion.post.moveTo(0.5, -0.08 , 0)
            motion.wait(id, 0)


            id = motion.post.moveTo(0, 0 , height_turn)
            motion.wait(id, 0)

            id = motion.post.moveTo(0.5, -0.08 , 0)
            motion.wait(id, 0)

            id = motion.post.moveTo(0.5, -0.08 , 0)
            motion.wait(id, 0)

            break

    a = tactile_touch.getStatus()
    if a[8][1] == True :
        break
 
tts.say("Fin du programme")
    


