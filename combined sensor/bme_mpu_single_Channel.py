from imu import MPU6050
from time import sleep
from machine import Pin, I2C
import bme280

# Initialize the shared I2C bus
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# Create instances of the sensors using the shared I2C bus
imu = MPU6050(i2c)
bme = bme280.BME280(i2c=i2c)


def calculate_altitude(pressure, sea_level_pressure=1013.25):
    # Calculate altitude using barometric formula
    p0 = sea_level_pressure
    p = pressure  # Pressure is already in hPa
    altitude = 44330.0 * (1.0 - (p/p0)**(1/5.255))
    return altitude

while True:
    ax = round(imu.accel.x, 2)
    ay = round(imu.accel.y, 2)
    az = round(imu.accel.z, 2)
    gx = round(imu.gyro.x)
    gy = round(imu.gyro.y)
    gz = round(imu.gyro.z)
    tem = round(imu.temperature, 2)
    temp = bme.values[0]
    pressure = bme.values[1]
    altitude = calculate_altitude(float(pressure.replace("hPa", "")))
    print("Accelerometer => x: {}, y: {}, z: {}".format(ax, ay, az))
    print("Gyroscope => x: {}, y: {}, z: {}".format(gx, gy, gz))
    print("Temperature: ", temp)
    print("Atmospheric Pressure: ", pressure)
    print("Altitude: {}m".format(altitude))
    print(" ")
    sleep(0.2)
