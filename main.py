from functools import reduce

class Process:
    def __init__(self, initial_state=0):
        self.state = initial_state

    @staticmethod
    def compose_functions(func_list):
        return lambda x: reduce(lambda v, f: f(v), func_list, x)

    @staticmethod
    def add(value):
        return lambda x: x + value

    @staticmethod
    def subtract(value):
        return lambda x: x - value

    @staticmethod
    def multiply(value):
        return lambda x: x * value

    @staticmethod
    def divide(value):
        if value != 0:
            return lambda x: x / value
        else:
            print("Error: Cannot divide by zero")

    def set_state(self, update_lambda):
        if update_lambda is not None:
            self.state = update_lambda(self.state)

    def get_state(self):
        return self.state

# Example usage:
process = Process(initial_state=10)

print("Initial State:", process.get_state())  # Output: Initial State: 10

add_5 = Process.add(5)
process.set_state(add_5)
print("After Adding 5:", process.get_state())  # Output: After Adding 5: 15

subtract_3 = Process.subtract(3)
process.set_state(subtract_3)
print("After Subtracting 3:", process.get_state())  # Output: After Subtracting 3: 12

multiply_2 = Process.multiply(2)
process.set_state(multiply_2)
print("After Multiplying by 2:", process.get_state())  # Output: After Multiplying by 2: 24

divide_4 = Process.divide(4)
process.set_state(divide_4)
print("After Dividing by 4:", process.get_state())  # Output: After Dividing by 4: 6

# Example usage:
process2 = Process(initial_state=10)

print("Initial State:", process2.get_state())  # Output: Initial State: 10


compose_operations = Process.compose_functions([add_5, subtract_3, multiply_2, divide_4])
process2.set_state(compose_operations)
print("After Composing Operations:", process2.get_state())  # Output: After Composing Operations: 6
