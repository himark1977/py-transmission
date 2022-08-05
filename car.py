import obd
from obd import OBDStatus

connection = obd.OBD() # auto-connects to USB or RF port
ports = obd.scan_serial()      # return list of valid USB or RF ports
connectstats = connection.status()

read_speed = obd.commands[1][13] # select an OBD command (sensor)
read_rpm = obd.commands[1][12]
read_fuel = obd.commands.FUEL_LEVEL
response_fuel = connection.query(read_fuel)
response_speed = connection.query(read_speed) # send the command, and parse the response
response_rpm = connection.query(read_rpm)


