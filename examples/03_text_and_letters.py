from sevenseg import SevenSeg
from utime import sleep_ms

def main():
    display = SevenSeg(2, 3, 4, 5, 6, 7, 8, common_anode=True)

    while True:
        # Spell "HELP"
        display.show(72)  # 'H'
        sleep_ms(600)
        display.show(69)  # 'E'
        sleep_ms(600)
        display.show(76)  # 'L'
        sleep_ms(600)
        display.show(80)  # 'P'
        sleep_ms(600)

        # Dash separator '-' (ASCII 45)
        display.show(45)
        sleep_ms(400)

        display.clear()
        sleep_ms(1000)