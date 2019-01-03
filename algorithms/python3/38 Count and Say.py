class Solution:
    def countAndSay(self, n):
        reading = "1"
        for i in range(n - 1):
            reading = self.getReading(reading)
        return reading
    
    def getReading(self, reading):
        string = ""
        index = 0
        while (index < len(reading)):
            curr = reading[index]
            count = 0
            while (index < len(reading) and reading[index] == curr):
                count += 1
                index += 1
            string = string + str(count) + str(curr)
        return string