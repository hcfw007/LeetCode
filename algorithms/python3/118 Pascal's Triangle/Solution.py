class Solution:
    def generate(self, numRows):
        if (numRows == 0): return []
        row = [1]
        ans = [row]
        for i in range(1, numRows):
            lastRow = row[:]
            row = []
            row.append(lastRow[0])
            for j in range(len(lastRow) - 2):
                row.append(lastRow[j] + lastRow[j + 1])
            row.append(lastRow[-1])
            ans.append(row)
        return ans