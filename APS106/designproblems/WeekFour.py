# Define the parameters
earthquake = 1  # in richter scale
explosion = False
water_level = "Low"  # "High" "Low"
temperature = 100  # in degrees celsius
tsunami_height = 1
radiation_leak = "Low"  # "High", "Low", "None"

# Define plant status
status = "green"

if earthquake > 8.5 or explosion or water_level == "Low" or temperature  > 1000 or tsunami_height >= 5:
    status = "red"


