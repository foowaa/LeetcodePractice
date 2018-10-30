class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        # 转化为判断5的质因数问题
        if n==0:
            return 1
        else:
            num = 0
            while n>0:
                num += int(n/5)
                n /= 5
            return num


if __name__=="__main__":
    x = Solution()
    print(x.trailingZeros(105))