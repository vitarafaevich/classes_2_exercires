class RomanNumber:
    """
    Class representing the Roman and decimal Numbers.
    :method is_int(value):
    :method is_roman(value):
    :method decimal_number(self):
    :method roman_number(self):
    """
    decimal_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    decimal_couple = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}

    def __init__(self, number):
        if isinstance(number, int):
            if self.is_int(number):
                self.int_value = number
                self.rom_value = RomanNumber.roman_number(self)
            else:
                self.int_value = None
                self.rom_value = None
                print('error: Incorrect Roman or Regular number')
        elif isinstance(number, str):
            if self.is_roman(number):
                self.rom_value = number
                self.int_value = RomanNumber.decimal_number(self)
            else:
                self.rom_value = None
                print('error: Incorrect Roman or Regular number')
        else:
            self.rom_value = None
            self.int_value = None
            print('error: Incorrect Roman or Regular number')


    @staticmethod
    def is_int(value):
        """
        Static method is_int(value): check if the decimal number can be transferred to roman one
        :param value: the Roman number that is being checked
        :return: boolean (True or False)
        """
        if 0 < value < 4000:
            return True
        else:
            return False

    @staticmethod
    def is_roman(value):
        """
        Static method is_roman(value): check if the roman number can be transferred to decimal one
        :param value: the Roman number that is being checked
        :return: boolean (True or False)
        """
        if not isinstance(value, str):
            return False
        # Invalid characters check.
        for char in value:
            if char not in RomanNumber.decimal_dict:
                return False

        # Check for more than 3 consecutive identical characters, except for M.
        max_consecutive = 1
        current_consecutive = 1
        previous_char = None
        for char in value:
            if char == previous_char:
                current_consecutive += 1
                max_consecutive = max(max_consecutive, current_consecutive)
                if max_consecutive > 3:
                    return False
            else:
                current_consecutive = 1
            previous_char = char
        for symbol in "VLD":
            if value.count(symbol) > 1:
                return False

        # Check for valid subtractive notation.
        i = 0
        while i < len(value) - 1:
            pair = value[i:i + 2]
            if pair in RomanNumber.decimal_couple:
                # Valid combination
                if RomanNumber.decimal_dict[value[i]] < RomanNumber.decimal_dict[value[i + 1]]:
                    i += 2
                # Invalid combo: Smaller value before larger one.
                else:
                    return False
            else:
                i += 1
        return True

    def decimal_number(self):
        """
        Method decimal_number(self): transfer roman number to the decimal one
        :return decimal_value: decimal value of the roman number
        """
        decimal_value = 0
        i = 0
        if self.rom_value is not None:
            while i < len(self.rom_value):
                if i < (len(self.rom_value) - 1) and self.rom_value[i:i + 2] in self.decimal_couple:
                    decimal_value += self.decimal_couple[self.rom_value[i:i + 2]]
                    i += 2
                else:
                    decimal_value += RomanNumber.decimal_dict[self.rom_value[i]]
                    i += 1
            return decimal_value
        # Invalid roman numerals.
        else:
            return None

    def roman_number(self):
        """
        Method roman_number(self): transfer decimal number to the roman one
        :return decimal_value: roman value of the decimal number
        """
        if self.int_value is None:
            return None
        roman = ''
        num = self.int_value
        for value, numeral in RomanNumber.decimal_dict.items():
            while num >= numeral:
                roman += value
                num -= numeral
        return roman

    def __repr__(self):
        return str(self.rom_value)

    def __add__(self, other):
        result = self.int_value + other.int_value
        return RomanNumber(result)

    def __sub__(self, other):
        result = self.int_value - other.int_value
        return RomanNumber(result)

    def __mul__(self, other):
        result = self.int_value * other.int_value
        return RomanNumber(result)

    def __truediv__(self, other):
        result = self.int_value / other.int_value
        if str(result)[-1] == '0':
            result = int(result)
        return RomanNumber(result)

    def __floordiv__(self, other):
        result = self.int_value // other.int_value
        return RomanNumber(result)

    def __mod__(self, other):
        result = self.int_value % other.int_value
        return RomanNumber(result)

    def __pow__(self, other):
        result = self.int_value ** other.int_value
        return RomanNumber(result)

    def __iadd__(self, other):
        result = self.int_value
        result += other.int_value
        return RomanNumber(result)

    def __isub__(self, other):
        result = self.int_value
        result -= other.int_value
        return RomanNumber(result)

    def __imul__(self, other):
        result = self.int_value
        result = result * other.int_value
        return RomanNumber(result)

    def __itruediv__(self, other):
        result = self.int_value
        result = result / other.int_value
        if str(result)[-1] == '0':
            result = int(result)
        return RomanNumber(result)

    def __ifloordiv__(self, other):
        result = self.int_value
        result //= other.int_value
        return RomanNumber(result)

    def __ipow__(self, other):
        result = self.int_value
        result **= other.int_value
        return RomanNumber(result)

    def __imod__(self, other):
        result = self.int_value
        result %= other.int_value
        return RomanNumber(result)


a = RomanNumber('XI')
b = RomanNumber('VII')
c = a + b
print(c)
d = RomanNumber('XII')
print(c - d)
e = RomanNumber('XXXIV')
f = e * a
print(f)
print(f / RomanNumber('II') )
g = f / b
print(g.rom_value)
print(f // b)
print(f % b)
print(RomanNumber('II') ** RomanNumber('X'))
a -= b
print(a)
b += RomanNumber('XX')
print(b)
b /= RomanNumber('III')
print(b)
b *= a
print(b)
b /= RomanNumber('X')
print(b)
e //= RomanNumber('X')
print(e)
e %= RomanNumber('II')
print(e)