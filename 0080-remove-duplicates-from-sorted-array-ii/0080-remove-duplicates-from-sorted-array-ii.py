class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        size = len(nums)
        if size < 3:
            return size

        i, j = 0, 1
        n = 1

        repeat = 1

        while j < size:
            if nums[i] == nums[j]:
                if repeat == 1:
                    nums[n] = nums[j]
                    n += 1
                    i += 1
                    repeat += 1
                j += 1

            else:
                nums[n] = nums[j]
                i = j
                n += 1
                j += 1
                repeat = 1

        return n


            