from machine import pin
import time

LED_PIN = 4
BUTTON_PIN = 0
ON_VALUE = 1
OFF_VALUE = 0  
PRESSED_VALUE = 0  #[강사 확인]
PERIOD = 0.01 # 0.01초
levers = [0, 0.1, 0.3, 0.6, 0.9]
index = 0
was_pressed = False
ratio = 0

led = Pin(LED_PIN, Pin.OUT, value=OFF_VALUE)
button = Pin(BBUTTON_PIN, Pin.IN, Pin.PULL_UP)


def ratio_controler()
    global ratio, ON_VALUE, on time, off_time 
    if ratio > 0:
        led.value(ON_VALUE)
        time.sleep(on_time)
        led.value(OFF_VALUE)
        time.sleep(off_time)

while True:
    if button.value() == PRESSED_VALUE:
        if was_pressed == False:
            index = index + 1
            if index > 4:
                index = 0
                
    if  button.value() == PRESSED_VALUE:
         was_pressed == True :
    else :
        was_pressed = False
       
    ratio = levers[index] #0.5
    on_time = PERIOD * ratio
    off_time = PERTIO - on_time
    
    ratio_controler()
    led_controler()
    