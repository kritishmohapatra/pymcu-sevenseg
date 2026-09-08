from sevenseg import SevenSeg
from utime import sleep_ms

def main():
    # DP enabled on Pin 9
    display = SevenSeg(2, 3, 4, 5, 6, 7, 8, pin_dp=9, has_dp=True, common_anode=True)

    while True:
        # Number without DP vs Number with DP
        display.show(3, dp=False)
        sleep_ms(700)
        display.show(3, dp=True)
        sleep_ms(700)

        # Standalone dot '.' (ASCII 46)
        display.show(46)
        sleep_ms(700)

        # Exclamation '!' (ASCII 33 - automatically activates DP)
        display.show(33)
        sleep_ms(700)

        display.clear()
        sleep_ms(500)