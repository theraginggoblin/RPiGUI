from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO

# Set pins for the LEDs

red_led = 8
green_led = 10
blue_led = 12

def setup_led_pin_out(led_pin):
    GPIO.setup(led_pin, GPIO.OUT)

# configure pin layout and configure our pins

def pin_setup():
    GPIO.setmode(GPIO.BOARD)
    setup_led_pin_out(red_led)
    setup_led_pin_out(green_led)
    setup_led_pin_out(blue_led)

def led_on(led_pin):
    GPIO.output(led_pin, GPIO.HIGH)

def led_off(led_pin):
    GPIO.output(led_pin, GPIO.LOW)

def led_red_on():
    led_on(red_led)
    led_off(green_led)
    led_off(blue_led)

def led_green_on():
    led_on(green_led)
    led_off(red_led)
    led_off(blue_led)

def led_blue_on():
    led_on(blue_led)
    led_off(red_led)
    led_off(green_led)

def exit_program():
    GPIO.cleanup()
    controls_window.destroy()

pin_setup()

# GUI

controls_window = Tk()
controls_window.title('LED Control')

my_font = tkinter.font.Font(family = 'Helvetica', size = 12, weight = 'bold')

# Buttons

led_red_button = Button(controls_window, text = 'RED LED', font = my_font, command = led_red_on, bg = 'red', height = 1, width = 24)
led_red_button.grid(row = 0, column=0)

led_green_button = Button(controls_window, text = 'GREEN LED', font = my_font, command = led_green_on, bg = 'green', height = 1, width = 24)
led_green_button.grid(row = 1, column = 0)

led_blue_button = Button(controls_window, text = 'BLUE LED', font = my_font, command = led_blue_on, bg = 'blue', height = 1, width = 24)
led_blue_button.grid(row = 2, column = 0)

exit_button = Button(controls_window, text = 'EXIT', font = my_font, command = exit_program, bg = 'white', height = 1, width = 24)
exit_button.grid(row = 3, column = 0)

# handle exiting cleanly when X pressed on window instead of the exit button

controls_window.protocol('WM DELETE WINDOW', exit_program)
controls_window.mainloop()
