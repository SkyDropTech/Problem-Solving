class Solution:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        n = len(num)

        for i in range(n):
            if num[i] == "6":
                num = num[:i] + "9" + num[i+1:]
                break

        return int(num)