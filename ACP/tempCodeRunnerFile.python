class IntegerToRoman:
    def __init__(self):
        self.roman_mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
    
    def convert_to_roman(self, number):
        if not (1 <= number <= 3999):
            raise ValueError("Number out of range (must be 1-3999)")
        
        roman_numeral = ""
        for value, numeral in self.roman_mapping:
            quotient, number = divmod(number, value)  
            roman_numeral += numeral * quotient  
        return roman_numeral




print("Welcome to the Integer to Roman Numeral Converter!")
converter = IntegerToRoman()
    
while True:
    user_input = input("Enter an integer between 1 and 3999 (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    number = int(user_input)
    roman_numeral = converter.convert_to_roman(number)
    print(f"The Roman numeral for {number} is: {roman_numeral}")
    
