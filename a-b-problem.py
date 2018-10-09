class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """
    def aplusb(self, a, b):
        # write your code here
        ci = 0
        sum = 0
        for i in range(32):
            ai = a&1
            bi = b&1
            si = ai^bi^ci
            ci = (ai&bi)|((ai^bi)&ci)
            val = si << i
            sum = sum | val
            a = a >> 1
            b = b >> 1
        return sum
