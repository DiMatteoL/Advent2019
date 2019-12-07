# https://adventofcode.com/2019/day/5
day_5_instructions = '3,225,1,225,6,6,1100,1,238,225,104,0,1102,27,28,225,1,113,14,224,1001,224,-34,224,4,224,102,8,223,223,101,7,224,224,1,224,223,223,1102,52,34,224,101,-1768,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1002,187,14,224,1001,224,-126,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1102,54,74,225,1101,75,66,225,101,20,161,224,101,-54,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1101,6,30,225,2,88,84,224,101,-4884,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1001,214,55,224,1001,224,-89,224,4,224,102,8,223,223,1001,224,4,224,1,224,223,223,1101,34,69,225,1101,45,67,224,101,-112,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,9,81,225,102,81,218,224,101,-7290,224,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,84,34,225,1102,94,90,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,677,677,224,102,2,223,223,1005,224,329,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,344,101,1,223,223,1008,677,677,224,102,2,223,223,1005,224,359,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,374,101,1,223,223,108,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,404,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,419,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,434,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,449,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,464,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,479,101,1,223,223,8,226,226,224,1002,223,2,223,1006,224,494,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,509,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,539,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,554,101,1,223,223,107,226,677,224,1002,223,2,223,1006,224,569,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,584,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,599,101,1,223,223,1008,226,226,224,1002,223,2,223,1005,224,614,1001,223,1,223,107,226,226,224,1002,223,2,223,1005,224,629,101,1,223,223,7,226,226,224,102,2,223,223,1006,224,644,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,659,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226'.split(',')

POSITION = 'position'
IMMEDIATE = 'immediate'
CONTINUE = 'continue'


class Instruction(object):
    def __init__(self, raw_instruction):
        self.instruction = max((5 - len(raw_instruction)), 0) * '0' + raw_instruction
        self.parameter_count = 0
        self.method = self.get_method()
        self.modes = self.get_modes()

    def get_method(self):
        o = int(self.instruction[-2:])
        if o == 1:
            self.parameter_count = 3
            return self.add
        elif o == 2:
            self.parameter_count = 3
            return self.multiply
        elif o == 3:
            self.parameter_count = 1
            return self.prompt
        elif o == 4:
            self.parameter_count = 1
            return self.output
        elif o == 5:
            self.parameter_count = 2
            return self.is_true
        elif o == 6:
            self.parameter_count = 2
            return self.is_false
        elif o == 7:
            self.parameter_count = 3
            return self.less_than
        elif o == 8:
            self.parameter_count = 3
            return self.equals
        else:
            print('STOP')

    def get_modes(self):
        modes = []
        for parameter in self.instruction[:3]:
            modes.insert(0, self.get_mode(parameter))

        return modes[:self.parameter_count]

    @staticmethod
    def get_mode(number):
        if int(number) == 1:
            return IMMEDIATE
        elif int(number) == 0:
            return POSITION


    @staticmethod
    def add(a, b):
        return str(int(a) + int(b))

    @staticmethod
    def multiply(a, b):
        return str(int(a) * int(b))

    @staticmethod
    def prompt(a):
        return input('Input value:\n')

    @staticmethod
    def output(a):
        print(a)

    @staticmethod
    def is_true(a, b):
        if int(a):
            return b

    @staticmethod
    def is_false(a, b):
        if not int(a):
            return b

    @staticmethod
    def less_than(a, b):
        return 1 if int(a) < int(b) else 0

    @staticmethod
    def equals(a, b):
        return 1 if int(a) == int(b) else 0

    def __bool__(self):
        return bool(self.method)


class Program(object):
    def __init__(self, intcode, position=0):
        self.position = position
        self.instruction = Instruction(intcode[position])
        self.parameters = intcode[position + 1: position + 1 + self.instruction.parameter_count]
        self.values = self.get_values()

    def get_values(self):
        values = []
        for index, mode in enumerate(self.instruction.modes):
            values.append({
                'mode': mode,
                'value': self.parameters[index],
            })
        return values

    def __bool__(self):
        return bool(self.instruction)

class Computer(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.cursor_position = 0

    def get(self, value, mode=POSITION):
        if mode == POSITION:
            return self.instructions[int(value)]
        elif mode == IMMEDIATE:
            return value
        else:
            print('ERROR')

    def set(self, value, position):
        if value is not None:
            self.instructions[int(position)] = value

    def update_cursor(self, value, is_increment=True):
        if value:
            self.cursor_position = (self.cursor_position if is_increment else 0) + int(value)

    def diagnose(self):
        program = Program(self.instructions, self.cursor_position)

        if program:
            values = [self.get(**value) for value in program.values]
            computed_value = program.instruction.method(*values[:2])

            if program.instruction.parameter_count == 2 and computed_value is not None:
                self.update_cursor(values[-1], False)
            else:
                self.set(computed_value, program.values[-1]['value'])
                self.update_cursor(1 + len(values))

            self.diagnose()


print('day_5 (input 1 for answer 1 or 5 for answer 2)')
Computer(day_5_instructions).diagnose()
