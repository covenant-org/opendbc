from opendbc.car import Bus, structs
from opendbc.can.parser import CANParser
from opendbc.car.interfaces import CarStateBase
from opendbc.car.drone.values import DBC

STARTUP_TICKS = 100

class CarState(CarStateBase):
  def update(self, can_parsers):
    cp = can_parsers[Bus.main]
    ret = structs.CarState()

    ret.vEgoRaw = cp.vl['DRONE_DATA']['SPEED']
    ret.cruiseState.speed = cp.vl['DRONE_DATA']['SPEED']

    #TODO: add altitude to car state for drone
    ret.wheelSpeeds.rl = cp.vl['DRONE_DATA']['ALTITUDE']
    #TODO: add height target to car state for drone
    ret.wheelSpeeds.rr = cp.vl['DRONE_DATA']['HEIGHT_TARGET']
    print(f"height target: {ret.wheelSpeeds.rr}")
#
    ret.vEgo, ret.aEgo = self.update_speed_kf(ret.vEgoRaw)
    ret.standstill = False
    ret.steerFaultPermanent = False

    # irrelevant for non-car
    ret.gearShifter = structs.CarState.GearShifter.drive
    ret.cruiseState.enabled = True
    ret.cruiseState.available = True
    ret.canValid = True
    ret.steeringPressed = not cp.vl['DRONE_MODE']['OFFBOARD']

    return ret

  @staticmethod
  def get_can_parser(CP):
    messages = [
      ("DRONE_DATA", 100),
      ("DRONE_MODE", 100),
    ]
    return {Bus.main: CANParser(DBC[CP.carFingerprint][Bus.main], messages, 0)}
