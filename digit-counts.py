class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        # write your code here
        num_list = self.split_num(n)
        num_list = num_list.reverse()
        num = 0
        for idx, ele in enumerate(num_list):
            num += self.get_num(idx, ele, num_list)
    def split_num(self, n):
        temp_list = []
        while n>0:
            temp_list.append(n%10)
            n = int(n/10)
        return temp_list

    def get_num(self, idx, ele, num_list):
        num_lower = self.compute_lower(self, idx, ele, num_list)
        if idx==0:
            return num_lower
        else:
            num_others = self.compute_others(self, idx, ele, num_list)
            return num_lower+num_others
    def compute_lower(self, idx, ele, num_list):
        pass
    def compute_others(self, idx, ele, num_list):
        pass

