#!/usr/bin/env python3
import math
from opendbc.car.structs import CarParams
from openpilot.common.realtime import DT_CTRL
from opendbc.car import get_safety_config
from opendbc.car.interfaces import CarInterfaceBase
from opendbc.car.drone.carstate import CarState
from opendbc.car.drone.carcontroller import CarController

class CarInterface(CarInterfaceBase):
  CarState = CarState
  CarController = CarController

  @staticmethod
  def _get_params(ret: CarParams, candidate, fingerprint, car_fw, experimental_long, is_release, docs):
    ret.notCar = True
    ret.carName = "drone"
    ret.safetyConfigs = [get_safety_config(CarParams.SafetyModel.drone)]

    ret.minSteerSpeed = -math.inf
    ret.maxLateralAccel = math.inf  # TODO: set to a reasonable value
    ret.steerLimitTimer = 1.0
    ret.steerActuatorDelay = 0.1
    ret.autoResumeSng = True
    ret.stoppingControl = True

    ret.wheelSpeedFactor = 1.

    ret.radarUnavailable = True
    ret.openpilotLongitudinalControl = True
    ret.steerControlType = CarParams.SteerControlType.angle
    ret.vEgoStarting = 0.1
    ret.vEgoStopping = 0.1

    return ret
