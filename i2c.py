import smbus
import time

# Defining the I2C address for the BH1750 light sensor
BH1750_I2C_ADDR = 0x23

# Creating an instance of the I2C bus (SMBus)
bus = smbus.SMBus(1)  

# Function for reading light level from the sensor
def read_light_level():
    # Reading light data from the sensor in continuous mode
    data = bus.read_i2c_block_data(BH1750_I2C_ADDR, 0x20)
    
    # Converting raw data to lux units for light intensity
    light_level = (data[1] + (256 * data[0])) / 1.2
    return light_level

# Function for categorizing the light level
def categorize_light(light_level):
    if light_level < 10:
        return "Too Dark"
    elif 10 <= light_level < 50:
        return "Dark"
    elif 50 <= light_level < 200:
        return "Medium"
    elif 200 <= light_level < 500:
        return "Bright"
    else:
        return "Too Bright"

try:
    while True:
        # Reading the current light level from the sensor
        light_level = read_light_level()
        
        # Categorizing the light level based on predefined thresholds
        category = categorize_light(light_level)
        
        # Printing the current light level in lux and its category
        print(f"Light Level: {light_level} lux - Category: {category}")
        
       
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    # Closing the I2C bus when the script is interrupted
    bus.close()
