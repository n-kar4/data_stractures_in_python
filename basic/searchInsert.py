class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1
        mid=0
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                return mid
            print(mid ,"######")
        if mid==0:
            return mid
        else:
            return mid+1

a = Solution()
print(a.searchInsert([1,3,5,6],2))

































# # s = 'RDDLRDRU'

# # x=y=0
# # for i in s:
# #     if i == 'L':
# #         x+=1
# #     elif i == 'R':
# #         x -=1
# #     elif i == 'U':
# #         y+=1
# #     elif i == 'D':
# #         y-=1
    
# # if x<0:
# #     x=-x
# # if y<0:
# #     y=-y

# # print((x+y)//2)



# s = "asdfghjkllkjhgfdsa"

# for i in range(len(s)//2):
#     if s[i] != s[-i-1]:
#         print("nuuu",)


# if s == s[::-1]:
#     print("toooo")