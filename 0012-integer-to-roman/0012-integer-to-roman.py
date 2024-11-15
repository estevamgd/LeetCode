class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of integer values to their respective Roman numerals
        val_to_roman = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        # Result string
        roman = ""
        
        # Iterate over the mappings
        for value, symbol in val_to_roman:
            # While num is greater than or equal to the value
            while num >= value:
                roman += symbol  # Append the Roman numeral
                num -= value     # Subtract the value from num
        
        return roman
