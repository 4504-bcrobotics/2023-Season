
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

import wpilib
import ctre
# import rev

"""Global Configuration Parameters"""
INVERT_LEFT = False
INVERT_RIGHT = True

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """Robot initialization function"""

        # self.camera = wpilib.CameraServer
        # self.camera.launch()
        
        # Start accelerometer using I2C attached to roborio
       # self.accelerometer = wpilib.ADXL345_I2C(wpilib.I2C.Port.kOnboard)

        """Pigeon Configuration"""
        self.imu = ctre.Pigeon2(11)
        self.imu.configMountPose(ctre.AxisDirection.NegativeX, ctre.AxisDirection.PositiveZ)
        
        
        """Motor Configuration"""
        self.RightMotor = ctre.TalonSRX(1)
        self.RightMotor.setInverted(INVERT_RIGHT)
        self.RightMotor2 = ctre.TalonSRX(2)
        self.RightMotor2.setInverted(INVERT_RIGHT)
        self.RightMotor2.follow(self.RightMotor)
        self.RightMotor3 = ctre.TalonSRX(3)
        self.RightMotor3.setInverted(INVERT_RIGHT)
        self.RightMotor3.follow(self.RightMotor)

        self.LeftMotor = ctre.TalonSRX(4)
        self.LeftMotor.setInverted(INVERT_LEFT)
        self.LeftMotor5 = ctre.TalonSRX(5)
        self.LeftMotor5.setInverted(INVERT_LEFT)
        self.LeftMotor5.follow(self.LeftMotor)
        self.LeftMotor6 = ctre.TalonSRX(6)
        self.LeftMotor6.setInverted(INVERT_LEFT)
        self.LeftMotor6.follow(self.LeftMotor)

        """User Controller Configuration"""
        self.flightStickLeft = wpilib._wpilib.Joystick(0)
        self.flightStickRight = wpilib._wpilib.Joystick(1)
        
    def autonomousInit(self) -> None:
        self.RightMotor.set(ctre._ctre.TalonSRXControlMode.PercentOutput, 0.2)
        self.LeftMotor.set(ctre._ctre.TalonSRXControlMode.PercentOutput, -0.2)
       
        return super().autonomousInit()
    
    def autonomousPeriodic(self) -> None:
        heading = self.imu.getAbsoluteCompassHeading()
        # heading = self.imu.getYaw()
        # print(heading)
        # error = (1 - heading)
        # error = 0.5-heading/360
        error = heading/360
        self.RightMotor.set(ctre._ctre.TalonSRXControlMode.PercentOutput, error)
        self.LeftMotor.set(ctre._ctre.TalonSRXControlMode.PercentOutput, error)
        return super().autonomousPeriodic()

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        # self.controller = wpilib.PS4Controller(0)
        # self.myRobot.setSafetyEnabled(True)
        return False

    def teleopPeriodic(self) -> None:
        Yleft = self.flightStickLeft.getY()
        Yright = self.flightStickRight.getY()
        
        self.RightMotor.set(ctre._ctre.TalonSRXControlMode.PercentOutput, Yright)
        self.LeftMotor.set(ctre._ctre.TalonSRXControlMode.PercentOutput, Yleft)
        
        # return super().teleopPeriodic()
    
    # def teleopPeriodic(self):
        # self.motor_drive_update()


    def motor_drive_update(self, clampL = 0.25, clampR = 0.25, boost_enable = True):
        """Runs the motors with arcade steering"""

        # Boost on both drive sides is enabled only when both bumpers are pressed simultaniously
        if self.controller.getL1Button() and self.controller.getR1Button() and boost_enable:
            clampL = 1.0
            clampR = 1.0

        # Right Drive
        Rightval = self.controller.getLeftY() * clampR
        # Rightval = self.accelerometer.getX()
        self.RightMotor1.set(ctre._ctre.TalonSRXControlMode.PercentOutput, Rightval)
        self.RightMotor2.set(ctre._ctre.TalonSRXControlMode.PercentOutput, Rightval)
        self.RightMotor3.set(ctre._ctre.TalonSRXControlMode.PercentOutput, Rightval)

        #Left Drive
        Leftval = self.controller.getRightY() * -clampL
        # Leftval = self.accelerometer.getY()
        self.LeftMotor4.set(ctre._ctre.TalonSRXControlMode.PercentOutput, Leftval)
        self.LeftMotor5.set(ctre._ctre.TalonSRXControlMode.PercentOutput, Leftval)
        self.LeftMotor6.set(ctre._ctre.TalonSRXControlMode.PercentOutput, Leftval)        

if __name__ == "__main__":

    wpilib.run(MyRobot)