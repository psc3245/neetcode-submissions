class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        toReturn = [[1]]
        if (numRows < 2): return toReturn
        toReturn.append([1, 1])
        for i in range(2, numRows):
            row = [1]
            for j in range(1, (len(toReturn[-1]))):
                row.append(toReturn[-1][j - 1] + toReturn[-1][j])
            row.append(1)
            toReturn.append(row)
        return toReturn
        