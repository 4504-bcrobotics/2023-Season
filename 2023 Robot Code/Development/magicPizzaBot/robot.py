
#!/usr/bin/env python3

"""
#		    _/  _/    _/_/_/_/    _/    _/  _/   
#		   _/  _/    _/        _/  _/  _/  _/    
#		  _/_/_/_/  _/_/_/    _/  _/  _/_/_/_/   
#		     _/          _/  _/  _/      _/      
#		    _/    _/_/_/      _/        _/ 
"""


"""
    This is a demo program showing the use of the RobotDrive class,
    specifically it contains the code necessary to operate a robot with
    arcade drive.
"""
from magicbot import MagicRobot
import wpilib
import ctre
from componentsDrive import DriveTrainModule, ComboTalonSRX
from componentsIntake import IntakeModule
#from collections import namedtuple

# IntakeConfig = namedtuple("IntakeConfig", ["channelA", "channelB"])

class MyRobot(MagicRobot):
    
    drivetrain: DriveTrainModule
    intake: IntakeModule
    # Intake_cfg = IntakeConfig(1, 2) # TODO: this might not work... 
    

    def createObjects(self):
        """Robot initialization function"""
        
        """Intake Motor Configuration"""
        self.top_motor = ctre.TalonSRX(7)
        self.bottom_motor = ctre.TalonSRX(8)
        self.pneumatic_hub = wpilib.PneumaticHub(11)
        
        """Drivetrain Motor Configuration"""
        self.mainLeft_motor = ComboTalonSRX(6, [4,5], inverted=False)
        self.mainLeft_motor.setup()

        self.mainRight_motor = ComboTalonSRX(2, [1,3], inverted=True)
        self.mainRight_motor.setup()

        """User Controller Configuration"""
        self.flightStickLeft = wpilib.Joystick(0)
        self.flightStickRight = wpilib.Joystick(1)
        
        pass
 
    def teleopInit(self):
        return False

    def teleopPeriodic(self) -> None:
        fsL = self.flightStickLeft.getY()
        fsR = self.flightStickRight.getY()
        self.drivetrain.setLeft(fsL)
        self.drivetrain.setRight(fsR)


        

if __name__ == "__main__":

    wpilib.run(MyRobot)