#pragma once

#include "opendbc/safety/safety_declarations.h"

static void drone_rx_hook(const CANPacket_t *to_push) {
  // body is never at standstill
  UNUSED(to_push);
  vehicle_moving = true;

  controls_allowed = true;
}

static bool drone_tx_hook(const CANPacket_t *to_send) {
  UNUSED(to_send);
//  return tx;
  return true;
}

static safety_config drone_init(uint16_t param) {
  static const CanMsg DRONE_TX_MSGS[] = {{0x265, 0, 6, .check_relay = false}, {0x266, 0, 8, .check_relay = false}, {0x267, 0, 2, .check_relay = false}};
  static RxCheck drone_rx_checks[] = {};

  UNUSED(param);
  safety_config ret = BUILD_SAFETY_CFG(drone_rx_checks, DRONE_TX_MSGS);
  ret.disable_forwarding = true;
  return ret;
}

const safety_hooks drone_hooks = {
  .init = drone_init,
  .rx = drone_rx_hook,
  .tx = drone_tx_hook,
  };
