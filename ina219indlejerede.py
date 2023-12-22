from ina219_lib import INA219
from machine import I2C, Pin
from time import sleep


##########################################################
# CONFIRGURATION
ina219_i2c_addr = 0x40

##########################################################
# OBJECTS
i2cHw0 = I2C(0)

ina219 = INA219(i2cHw0, ina219_i2c_addr)

##########################################################
# VARIABLER OG KONSTANTER
cur_max = -9999
cur_min = 9999
cur_sum = 0
cur_measurements = 0

##########################################################
# PROGRAM

print("INA219 program kører")

ina219.set_calibration_16V_400mA()

while True:
    cur = ina219.get_current()
    shunt_voltage = ina219.get_shunt_voltage()
    bus_voltage = ina219.get_bus_voltage()
    
    print(cur)
    print(shunt_voltage)
    print(bus_voltage)
    
    print()
    
    sleep(1)