class RomanNumber:
    """
    Class representing the Roman Numbers.
    :method is_roman(value):
    :method decimal_number(self):
    """
    decimal_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    decimal_couple = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}

    def __init__(self, number):
        if isinstance(number, str) and self.is_roman(number):
            self.rom_value = number
        else:
            self.rom_value = None
            print('error: Incorrect Roman number')

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

    def __repr__(self):
        return str(self.rom_value)


num_1 = RomanNumber('VI')
print(num_1.rom_value)
print(num_1.decimal_number())
print(num_1)
num_2 = RomanNumber('IIII')
print(num_2.rom_value)
num_3 = RomanNumber('XXIV')
print(num_3.decimal_number())
num_4 = RomanNumber('QER2')
nums = []
nums.append(num_1)
nums.append(num_2)
nums.append(num_3)
nums.append(num_4)
print(nums)
print(RomanNumber.is_roman('MMMCMLXXXVI'))
print(RomanNumber.is_roman('MMMMLXXXVI'))
