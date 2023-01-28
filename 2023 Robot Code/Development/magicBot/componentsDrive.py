import ctre
import rev
import magicbot

class ComboSparkMax:
    def __init__(self, canID_leader, canID_followers, motorType, inverted = False):
        self.canID_leader = canID_leader
        self.canID_followers = canID_followers
        self.inverted = inverted
        self.mainMotor = None
        self.followerMotors = None
        self.motorType = motorType

        self.mainMotor = rev.CANSparkMax(self.canID_leader, motorType)
        self.mainMotor.setInverted(self.inverted)

        if not isinstance(self.canID_followers, list):
            self.canID_followers = [self.canID_followers]

        followerMotors = []
        for canID in self.canID_followers:
            follower = rev.CANSparkMax(canID, motorType)
            follower.setInverted(self.inverted)
            follower.follow(self.mainMotor)                              
            followerMotors.append(follower)

        self.followerMotors = followerMotors

    def setPercent(self, value):
        self.mainMotor.set(value)
        return False
        

class DriveTrainModule:
    mainLeft_motor: ComboSparkMax
    mainRight_motor: ComboSparkMax

    def __init__(self):
        self.leftSpeed = 0
        self.leftSpeedChanged = False
        
        self.rightSpeed = 0
        self.rightSpeedChanged = False           

    def setLeft(self, value):
        self.leftSpeed = value
        self.leftSpeedChanged = True
        
    def setRight(self, value):
        self.rightSpeed = value
        self.rightSpeedChanged = True
        
    def is_leftChanged(self):
        return self.leftSpeedChanged
    
    def is_rightChanged(self):
        return self.rightSpeedChanged

    def execute(self):
        '''This gets called at the end of the control loop'''
        if self.is_leftChanged():
            self.mainLeft_motor.setPercent(self.leftSpeed)
            self.leftSpeedChanged = False

        if self.is_rightChanged():
            self.mainRight_motor.setPercent(self.rightSpeed)
            self.rightSpeedChanged = False