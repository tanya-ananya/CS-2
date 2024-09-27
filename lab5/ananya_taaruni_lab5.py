class Computer:
    def __init__(self,manufacturer,model,processor,ram,display_size):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = processor
        self.ram = ram
        self.display_size = display_size
        
    def print_info(self):
        print(f'Manufacturer: {self.manufacturer}, Model: {self.model}, Processor: {self.processor}, RAM: {self.ram}, Display Size: {self.display_size}')

class Laptop(Computer):
    def __init__(self,manufacturer,model,processor,ram,display_size,w,it):
        super().__init__(manufacturer,model,processor,ram,display_size)
        self.weight = w
        self.is_touch_screen = it

    def print_info(self):
        print(f'Manufacturer: {self.manufacturer}, Model: {self.model}, Processor: {self.processor}, RAM: {self.ram}, Display Size: {self.display_size}, Weight: {self.weight}, Touch Screen: {self.is_touch_screen}')

class Desktop(Computer):
    def __init__(self,manufacturer,model,processor,ram,display_size,type):
        super().__init__(manufacturer,model,processor,ram,display_size)
        self.type = type

    def print_info(self):
        print(f'Manufacturer: {self.manufacturer}, Model: {self.model}, Processor: {self.processor}, RAM: {self.ram}, Display Size: {self.display_size}, Type: {self.type}')


# driver code. No modification is necessary after this line.
computer1 = Laptop('Apple', 'MacBook Air', 'Apple M1', '16GB', '13.3"', '2.7 lbs', False)
computer2 = Laptop('HP', 'Envy', 'core i5', '8GB', '15.6"', '4lbs', True)
computer3 = Desktop('Dell', 'Inspiron', 'core i7', '32GB', '27"', 'All-in-One')
computer1.print_info()
computer2.print_info()
computer3.print_info()