
class Solution:
    
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        
        def B(temp):
            if len(temp) == len(nums):
                ans.append(temp[:])
                return
            for num in nums:
                if num not in temp:
                    temp.append(num)
                    B(temp)
                    temp.pop()
        B([])
        return ans
    
    def F16(self):

        # Input
        N = int(input())

        # Processing
        def F(N):
            if N < 3:
                return 1
            x = N // 2
            resum = 1
            for i in range(1, x + 1):
                y = N - i
                resum += F(i)
                if y == i:
                    resum -= 1
            return resum
                
        ans = F(N)

        # Output
        print(ans)
    
    def F350(self):

        # Input
        satr = input()

        # Processing
        def F(satr: str) -> dict:
            remap = {}
            for i in range(len(satr)):
                remap[i] = satr[i]
            return remap
        
        def F1(satr: str, nums: list[list[int]]) -> list[str]:
            relist = []
            for i in nums:
                remap = F(satr)
                relist.append("".join([remap[j] for j in i]))
            return relist
        
        nums = self.permute(list(range(len(satr))))
        ans = F1(satr, nums)
        
        # Output
        for i in ans:
            print(i)
        

def main():
    sol = Solution()
    sol.F16()


if __name__ == "__main__":
    main()
