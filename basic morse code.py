




import time
from machine import Pin, TouchPad

# Define timing parameters
DOT_DURATION = 1.0
DASH_DURATION = 1.0
NO_TOUCH_SPACE_DURATION = 1.0
# Define GPIO pins for touch
TOUCH_PIN_DOT = 4    # Single touch -> Dot
TOUCH_PIN_DASH = 12   # Both touched -> Dash

# Initialize touch sensors
touch_dot = TouchPad(Pin(TOUCH_PIN_DOT))
touch_dash = TouchPad(Pin(TOUCH_PIN_DASH))

# Threshold for detecting touch (adjust if needed)
TOUCH_THRESHOLD = 300

# Function to transmit a dot
def transmit_dot():
    print(".")
    time.sleep(DOT_DURATION)

# Function to transmit a dash
def transmit_dash():
    print("-")
    time.sleep(DASH_DURATION)

# Function to handle short space (no touch)
def handle_short_space():
    print("  ")
    time.sleep(NO_TOUCH_SPACE_DURATION)

# Main loop
if __name__ == "__main__":
    print("Touch sensors to transmit Morse code.")
    while True:
        # Read touch sensor values
        touch_dot_value = touch_dot.read()
        touch_dash_value = touch_dash.read()

        # Check if only the dot pin is touched
        if touch_dot_value < TOUCH_THRESHOLD and touch_dash_value >= TOUCH_THRESHOLD:
            transmit_dot()

        # Check if both pins are touched simultaneously
        elif touch_dot_value < TOUCH_THRESHOLD and touch_dash_value < TOUCH_THRESHOLD:
            transmit_dash()

        # No touch detected
        else:
            handle_short_space()
