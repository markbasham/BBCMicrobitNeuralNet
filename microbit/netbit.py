import machine

def get_serial_number(type=hex):
    NRF_FICR_BASE = 0x10000000
    DEVICEID_INDEX = 25 # deviceid[1]
    return type(machine.mem32[NRF_FICR_BASE + (DEVICEID_INDEX*4)]& 0xFFFFFFFF)
