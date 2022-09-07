#  PID控制一階慣性系統測試程序

import numpy as np
import pid_GUI

# *****************************************************************#
#                      增量式PID系統                              #
# *****************************************************************#
class IncrementalPID:
    def __init__(self, P, I, D):
        self.Kp = P
        self.Ki = I
        self.Kd = D

        self.PIDOutput = 0.0  # PID控制器輸出
        self.SystemOutput = 0.0  # 系統輸出值
        self.LastSystemOutput = 0.0  # 上次系統輸出值

        self.Error = 0.0  # 輸出值與輸入值的偏差
        self.LastError = 0.0
        self.LastLastError = 0.0

    # 設置PID控制器參數
    def SetStepSignal(self, StepSignal):
        self.Error = StepSignal - self.SystemOutput
        IncrementValue = self.Kp * (self.Error - self.LastError) + self.Ki * self.Error + self.Kd * (
                    self.Error - 2 * self.LastError + self.LastLastError)
        self.PIDOutput += IncrementValue
        self.LastLastError = self.LastError
        self.LastError = self.Error

    # 設置一階慣性環節系統  其中InertiaTime為慣性時間常數
    def SetInertiaTime(self, InertiaTime, SampleTime):
        self.SystemOutput = (InertiaTime * self.LastSystemOutput + SampleTime * self.PIDOutput) / (
                    SampleTime + InertiaTime)
        self.LastSystemOutput = self.SystemOutput


# *****************************************************************#
#                      位置式PID系統                              #
# *****************************************************************#
class PositionalPID:
    def __init__(self, P, I, D):
        self.Kp = P
        self.Ki = I
        self.Kd = D

        self.SystemOutput = 0.0
        self.ResultValueBack = 0.0
        self.PidOutput = 0.0
        self.PIDErrADD = 0.0
        self.ErrBack = 0.0

    def SetInertiaTime(self, InertiaTime, SampleTime):
        self.SystemOutput = (InertiaTime * self.ResultValueBack + SampleTime * self.PidOutput) / (
                    SampleTime + InertiaTime)
        self.ResultValueBack = self.SystemOutput

    def SetStepSignal(self, StepSignal):
        Err = StepSignal - self.SystemOutput
        KpWork = self.Kp * Err
        KiWork = self.Ki * self.PIDErrADD
        KdWork = self.Kd * (Err - self.ErrBack)
        self.PidOutput = KpWork + KiWork + KdWork
        self.PIDErrADD += Err
        self.ErrBack = Err


