from machine import Pin

class SevenSeg:
    def __init__(
        self,
        pin_a: const[uint8],
        pin_b: const[uint8],
        pin_c: const[uint8],
        pin_d: const[uint8],
        pin_e: const[uint8],
        pin_f: const[uint8],
        pin_g: const[uint8],
        pin_dp: const[uint8] = 0,
        has_dp: bool = False,
        common_anode: bool = False
    ):
        self.pa = Pin(pin_a, Pin.OUT)
        self.pb = Pin(pin_b, Pin.OUT)
        self.pc = Pin(pin_c, Pin.OUT)
        self.pd = Pin(pin_d, Pin.OUT)
        self.pe = Pin(pin_e, Pin.OUT)
        self.pf = Pin(pin_f, Pin.OUT)
        self.pg = Pin(pin_g, Pin.OUT)
        self.has_dp = has_dp
        if has_dp:
            self.pdp = Pin(pin_dp, Pin.OUT)
        self.common_anode = common_anode
        self.clear()

    def clear(self):
        if self.common_anode:
            self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            if self.has_dp:
                self.pdp.value(1)
        else:
            self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            if self.has_dp:
                self.pdp.value(0)

    def show(self, digit: uint8, dp: bool = False):
        if self.common_anode:
            # Common Anode: 0 is ON, 1 is OFF
            if self.has_dp:
                if dp or digit == 46 or digit == 33:
                    self.pdp.value(0)
                else:
                    self.pdp.value(1)

            # 0 to 9
            if digit == 0 or digit == 48:
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(1)
            elif digit == 1 or digit == 49:
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 2 or digit == 50:
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(0)
            elif digit == 3 or digit == 51:
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(0)
            elif digit == 4 or digit == 52:
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(0)
            elif digit == 5 or digit == 53:
                self.pa.value(0); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(0); self.pg.value(0)
            elif digit == 6 or digit == 54:
                self.pa.value(0); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 7 or digit == 55:
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 8 or digit == 56:
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 9 or digit == 57:
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(0); self.pg.value(0)

            # Uppercase Letters
            elif digit == 65:  # 'A'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 66:  # 'B'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 67:  # 'C'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(1)
            elif digit == 68:  # 'D'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(0)
            elif digit == 69:  # 'E'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 70:  # 'F'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 71:  # 'G'
                self.pa.value(0); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 72:  # 'H'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 73:  # 'I'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(1)
            elif digit == 74:  # 'J'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(1)
            elif digit == 76:  # 'L'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(1)
            elif digit == 78:  # 'N'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(1)
            elif digit == 79:  # 'O'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(1)
            elif digit == 80:  # 'P'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 81:  # 'Q'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(0)
            elif digit == 82:  # 'R'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(1)
            elif digit == 83:  # 'S'
                self.pa.value(0); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(0); self.pg.value(0)
            elif digit == 84:  # 'T'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 85:  # 'U'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(1)
            elif digit == 89:  # 'Y'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(0); self.pg.value(0)
            elif digit == 90:  # 'Z'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(0)

            # Lowercase Letters
            elif digit == 97:  # 'a'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(0)
            elif digit == 98:  # 'b'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 99:  # 'c'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(0)
            elif digit == 100:  # 'd'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(0)
            elif digit == 101:  # 'e'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 102:  # 'f'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 103:  # 'g'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(0); self.pg.value(0)
            elif digit == 104:  # 'h'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 105:  # 'i'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 106:  # 'j'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 108:  # 'l'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(1)
            elif digit == 110:  # 'n'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(1); self.pe.value(0); self.pf.value(1); self.pg.value(0)
            elif digit == 111:  # 'o'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(0)
            elif digit == 112:  # 'p'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 113:  # 'q'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(0)
            elif digit == 114:  # 'r'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(1); self.pg.value(0)
            elif digit == 115:  # 's'
                self.pa.value(0); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(0); self.pg.value(0)
            elif digit == 116:  # 't'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 117:  # 'u'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(1)
            elif digit == 121:  # 'y'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(0); self.pg.value(0)

            # Symbols
            elif digit == 45:  # '-'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(0)
            elif digit == 95:  # '_'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 46:  # '.'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 33:  # '!'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 63:  # '?'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(1); self.pg.value(0)
            elif digit == 39:  # "'"
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(1)
            elif digit == 34:  # '"'
                self.pa.value(1); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(1)
            elif digit == 91:  # '['
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(1)
            elif digit == 93:  # ']'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 61:  # '='
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(0)
            elif digit == 43:  # '+'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(1); self.pe.value(0); self.pf.value(1); self.pg.value(0)
            elif digit == 94:  # '^'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(1)
            elif digit == 32:  # ' '
                self.clear()
            else:
                self.clear()
        else:
            # Common Cathode: 1 is ON, 0 is OFF
            if self.has_dp:
                if dp or digit == 46 or digit == 33:
                    self.pdp.value(1)
                else:
                    self.pdp.value(0)

            # 0 to 9
            if digit == 0 or digit == 48:
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(0)
            elif digit == 1 or digit == 49:
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 2 or digit == 50:
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(1)
            elif digit == 3 or digit == 51:
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(1)
            elif digit == 4 or digit == 52:
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(1)
            elif digit == 5 or digit == 53:
                self.pa.value(1); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(1); self.pg.value(1)
            elif digit == 6 or digit == 54:
                self.pa.value(1); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 7 or digit == 55:
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 8 or digit == 56:
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 9 or digit == 57:
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(1); self.pg.value(1)

            # Uppercase Letters
            elif digit == 65:  # 'A'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 66:  # 'B'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 67:  # 'C'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(0)
            elif digit == 68:  # 'D'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(1)
            elif digit == 69:  # 'E'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 70:  # 'F'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 71:  # 'G'
                self.pa.value(1); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 72:  # 'H'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 73:  # 'I'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(0)
            elif digit == 74:  # 'J'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(0)
            elif digit == 76:  # 'L'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(0)
            elif digit == 78:  # 'N'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(0)
            elif digit == 79:  # 'O'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(0)
            elif digit == 80:  # 'P'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 81:  # 'Q'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(1)
            elif digit == 82:  # 'R'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(0)
            elif digit == 83:  # 'S'
                self.pa.value(1); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(1); self.pg.value(1)
            elif digit == 84:  # 'T'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 85:  # 'U'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(0)
            elif digit == 89:  # 'Y'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(1); self.pg.value(1)
            elif digit == 90:  # 'Z'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(1)

            # Lowercase Letters
            elif digit == 97:  # 'a'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(1)
            elif digit == 98:  # 'b'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 99:  # 'c'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(1)
            elif digit == 100:  # 'd'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(1)
            elif digit == 101:  # 'e'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 102:  # 'f'
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 103:  # 'g'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(1); self.pg.value(1)
            elif digit == 104:  # 'h'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 105:  # 'i'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 106:  # 'j'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 108:  # 'l'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(0)
            elif digit == 110:  # 'n'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(0); self.pe.value(1); self.pf.value(0); self.pg.value(1)
            elif digit == 111:  # 'o'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(1)
            elif digit == 112:  # 'p'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 113:  # 'q'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(1)
            elif digit == 114:  # 'r'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(0); self.pg.value(1)
            elif digit == 115:  # 's'
                self.pa.value(1); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(1); self.pg.value(1)
            elif digit == 116:  # 't'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(1)
            elif digit == 117:  # 'u'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(1); self.pe.value(1); self.pf.value(0); self.pg.value(0)
            elif digit == 121:  # 'y'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(1); self.pg.value(1)
            
            # Symbols
            elif digit == 45:  # '-'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(1)
            elif digit == 95:  # '_'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 46:  # '.'
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 33:  # '!'
                self.pa.value(0); self.pb.value(1); self.pc.value(1); self.pd.value(0); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 63:  # '?'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(1); self.pf.value(0); self.pg.value(1)
            elif digit == 39:  # "'"
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(0)
            elif digit == 34:  # '"'
                self.pa.value(0); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(0)
            elif digit == 91:  # '['
                self.pa.value(1); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(1); self.pf.value(1); self.pg.value(0)
            elif digit == 93:  # ']'
                self.pa.value(1); self.pb.value(1); self.pc.value(1); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(0)
            elif digit == 61:  # '='
                self.pa.value(0); self.pb.value(0); self.pc.value(0); self.pd.value(1); self.pe.value(0); self.pf.value(0); self.pg.value(1)
            elif digit == 43:  # '+'
                self.pa.value(0); self.pb.value(0); self.pc.value(1); self.pd.value(0); self.pe.value(1); self.pf.value(0); self.pg.value(1)
            elif digit == 94:  # '^'
                self.pa.value(1); self.pb.value(1); self.pc.value(0); self.pd.value(0); self.pe.value(0); self.pf.value(1); self.pg.value(0)
            elif digit == 32:  # ' '
                self.clear()
            else:
                self.clear()