class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        result = "-" if (numerator < 0) != (denominator < 0) else ""
        num, den = abs(numerator), abs(denominator)
        result += str(num // den)
        remainder = num % den
        if remainder == 0:
            return result
        result += "."
        seen = {}
        while remainder:
            if remainder in seen:
                i = seen[remainder]
                return result[:i] + "(" + result[i:] + ")"
            seen[remainder] = len(result)
            result += str(remainder * 10 // den)
            remainder = remainder * 10 % den
        return result
