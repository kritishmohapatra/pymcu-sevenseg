from sevenseg import SevenSeg
from utime import sleep_ms

def main():
    # Segment pins: A=2, B=3, C=4, D=5, E=6, F=7, G=8
    # Common Cathode: common_anode=False (change to True if using Common Anode)
    display = SevenSeg(2, 3, 4, 5, 6, 7, 8, common_anode=False)

    count: uint8 = 0
    while True:
        display.show(count)
        sleep_ms(1000)
        count = count + 1
        if count > 9:
            count = 0