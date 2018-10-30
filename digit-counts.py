class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        # write your code here
        num_list = self.split_num(n)
        num = 0
        for idx, ele in enumerate(num_list):
            num += self.get_num(idx, ele, num_list)
    def split_num(self, n):
        pass

    def get_num(self, idx, ele, num_list):
        pass
