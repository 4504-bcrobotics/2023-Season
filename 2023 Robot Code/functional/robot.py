
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
from subclassDrivetrain import drivetrain
from subclassIntake import intake
import wpilib

"""Global Configuration Parameters"""


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """Robot initialization function"""
        
        """Intake Motor Configuration"""
        # self.intake = intake()
        
        """Drivetrain Motor Configuration"""
        self.drivetrain = drivetrain()         

        """User Controller Configuration"""
        self.flightStickLeft = wpilib._wpilib.Joystick(0)
        self.flightStickRight = wpilib._wpilib.Joystick(1)
        
        pass
        
    def autonomousInit(self) -> None:
        return super().autonomousInit() 
    
    def autonomousPeriodic(self) -> None:
        return super().autonomousPeriodic() 
 
    def teleopInit(self):
        return False

    def teleopPeriodic(self) -> None:
        fsL = self.flightStickLeft.getY()
        fsR = self.flightStickRight.getY()
        self.drivetrain.setPercentLeft(fsL*0.4)
        self.drivetrain.setPercentRight(fsR)
        
        # return super().teleopPeriodic()



        

if __name__ == "__main__":

    wpilib.run(MyRobot)