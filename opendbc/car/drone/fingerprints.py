# ruff: noqa: E501
from opendbc.car.structs import CarParams
from opendbc.car.drone.values import CAR

Ecu = CarParams.Ecu

# debug ecu fw version is the git hash of the firmware


FINGERPRINTS = {
  CAR.DRONE: [{
    613: 8, 614: 4
  }],
}

FW_VERSIONS = {
  CAR.DRONE: {
    (Ecu.engine, 0x722, None): [
      b'ncl.0.01',
    ],
  },
}
