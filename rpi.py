import RPi.GPIO as GPIO
from time import sleep
import car

GPIO.setmode(GPIO.BCM)
Motor1A = 16
Motor1B = 18
Motor1E = 22
Motor2A = 23
Motor2B = 21
Motor2E = 19

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

def shift1up():
    print("Motor 1 X axis left")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor1E, GPIO.LOW)
    print("Motor 2 Y axis up")
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor2E, GPIO.LOW)

def shift2up():
    print("Motor 2 Y axis down")
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor2E, GPIO.LOW)
    print("Motor 1 X axis not moved")

def shift3up():
    print("Motor 2 Y axis up")
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor2E, GPIO.LOW)
    print("Motor 1 X axis right")
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor1E, GPIO.LOW)
    print("Motor 2 Y axis UP")
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor2E, GPIO.LOW)

def shift4up():
    print("Motor 2 Y axis down")
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor2E, GPIO.LOW)
    print("Motor 1 X axis not moved")

def shift3down():
    print("MOtor 2 Y axis up")
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor2E, GPIO.LOW)
    print("Motor 1 X axis not moved")

def shift2down():
    print("Motor 2 Y axis down")
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor2E, GPIO.LOW)
    print("Motor 1 X axis left")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor1E, GPIO.LOW)
    print("Motor 2 Y axis down")
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor2E, GPIO.LOW)

def shift1down():
    print("Motor 2 Y axis up")
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor2E, GPIO.LOW)
    print("Motor 1 X axis not moved")

def neutral():
    print("Motor 2 Y axis down")
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor2E, GPIO.LOW)
    print("Motor 1 X axis right")
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor1E, GPIO.LOW)

# For first gear, test with precautions
if(car.read_rpm >= 2500):
    shift1up()
elif(car.read_rpm <= 1500):
    neutral()