class Solution:
    def binarySearch(self, arr, num):
        #print(num)
        left = 0
        right = len(arr) - 1
        while left <= right:
            #print(left, right)
            mid = (left + right) // 2
            #print(mid)
            if arr[mid] == num:
                return True, mid
            if num > arr[mid]:
                left = mid + 1
            if num < arr[mid]:
                right = mid - 1
        return False, -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for lind in range(len(numbers)):
            num = target - numbers[lind]
            
            s, rind = self.binarySearch(numbers[lind + 1 :], num)
            if s:
                return [lind + 1, rind + lind + 2]
