#!/usr/bin/python3

import glob
import re

def read_file_to_string(file):
    text_file = open(file, 'r')
    data = text_file.read().strip()
    text_file.close()
    return data


def get_keyboard_name(keyboard):
    return keyboard + '/device/name'


def write_to_file(file, value):
    text_file = open(file, 'w')
    text_file.write(str(value))
    text_file.close()

def enable_disable_scroll_lock(keyboard):
    brightness_file = keyboard + '/brightness'
    current_value = int(read_file_to_string(brightness_file))
    write_to_file(brightness_file, 1 if current_value == 0 else 0)


def enable_scroll_lock_key():
    keyboards = glob.glob('/sys/class/leds/input*::scrolllock')
    max_number = 0
    keyboard_to_be_actioned = ''
    for keyboard in keyboards:
        device_name = get_keyboard_name(keyboard)
        print('Found Keyboard device :: ', read_file_to_string(device_name))
        #whichever keyboard device has max number, assuming that one as external keyboard
        external_keyboard = re.findall('[0-9]+', keyboard)[0]
        keyboard_number = int(external_keyboard)
        if keyboard_number > max_number:
            max_number = keyboard_number
            keyboard_to_be_actioned = keyboard

    print('Triggering key press on ::', get_keyboard_name(keyboard_to_be_actioned))
    enable_disable_scroll_lock(keyboard_to_be_actioned)

if __name__ == '__main__':
    print('Enabling Scroll Lock key.......!!')
    enable_scroll_lock_key()

