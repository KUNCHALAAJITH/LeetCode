class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        
        count = 0
        factor = 1  # Start with the ones place
        while factor <= n:
            # Split the number into parts
            lower_numbers = n - (n // factor) * factor
            current_digit = (n // factor) % 10
            higher_numbers = n // (factor * 10)
            
            # Count of ones contributed by higher digits
            count += higher_numbers * factor
            
            # Count of ones contributed by the current digit
            if current_digit == 1:
                count += lower_numbers + 1
            elif current_digit > 1:
                count += factor
            
            # Move to the next digit position
            factor *= 10
        
        return count