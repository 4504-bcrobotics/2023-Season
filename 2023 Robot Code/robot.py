
#!/usr/bin/env python3
"""
    This is a demo program showing the use of the RobotDrive class,
    specifically it contains the code necessary to operate a robot with
    arcade drive.
"""

import wpilib
import ctre
# import rev


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """Robot initialization function"""

        # self.camera = wpilib.CameraServer
        # self.camera.launch()
        
        # Start accelerometer using I2C attached to roborio
       # self.accelerometer = wpilib.ADXL345_I2C(wpilib.I2C.Port.kOnboard)

        # object that handles basic drive operations
        self.RightMotor1 = ctre.TalonSRX(1)
        self.RightMotor2 = ctre.TalonSRX(2)
        self.RightMotor3 = ctre.TalonSRX(3)

        self.LeftMotor4 = ctre.TalonSRX(4)
        self.LeftMotor5 = ctre.TalonSRX(5)
        self.LeftMotor6 = ctre.TalonSRX(6)


        self.controller = None
        self.flightStick = wpilib._wpilib.Joystick[0]
        
    def autonomousInit(self) -> None:
        self.RightMotor1.set(ctre._ctre.TalonSRXControlMode.PercentOutput, .2)
        self.RightMotor2.set(ctre._ctre.TalonSRXControlMode.PercentOutput, .2)
        self.RightMotor3.set(ctre._ctre.TalonSRXControlMode.PercentOutput, .2)
        self.LeftMotor4.set(ctre._ctre.TalonSRXControlMode.PercentOutput, -.2)
        self.LeftMotor5.set(ctre._ctre.TalonSRXControlMode.PercentOutput, -.2)
        self.LeftMotor6.set(ctre._ctre.TalonSRXControlMode.PercentOutput, -.2)
       
        return super().autonomousInit()
    
    def autonomousPeriodic(self) -> None:
        return super().autonomousPeriodic()

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        # self.controller = wpilib.PS4Controller(0)
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self) -> None:
        a = 1
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