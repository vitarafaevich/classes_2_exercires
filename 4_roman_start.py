class RomanNumber:

    translating = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    possible_combos = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    combos_translating = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    def __init__(self, line):
        if RomanNumber.is_roman(line) is False:
            self.rom_value = None
            print('ошибка')
        else:
            self.rom_value = line

    @staticmethod
    def is_roman(value):
        errors = 0
        for i in range(len(value)):
            if value[i] not in 'XLDCMIV':
                errors += 1
            else:
                if (i + 3 <= len(value) - 1) and (value[i] == value[i + 1] == value[i + 2] == value[i + 3]):
                    errors += 1
                else:
                    if (i + 1 <= len(value) - 1) and (
                            RomanNumber.translating[value[i]] < RomanNumber.translating[value[i + 1]]) and (
                            value[i] + value[i + 1] not in RomanNumber.possible_combos):
                        errors += 1
        if errors == 0:
            return True
        else:
            return False

    def decimal_number(self):
        result = 0
        number = self.rom_value
        while len(number) > 0:
            if (len(number) >= 3) and (number[0] == number[1] == number[2]):
                result += RomanNumber.translating[number[0]] * 3
                number = number[3:]
            elif (len(number) >= 2) and (number[0] == number[1]):
                result += RomanNumber.translating[number[0]] * 2
                number = number[2:]
            elif (len(number) >= 2) and (RomanNumber.translating[number[0]] < RomanNumber.translating[number[1]]) and (
                    number[0] + number[1] in RomanNumber.possible_combos):
                result += RomanNumber.combos_translating[number[0] + number[1]]
                number = number[2:]
            else:
                result += RomanNumber.translating[number[0]]
                number = number[1:]
        return result

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
print(RomanNumber.is_roman('MMMMMLXXXVI'))