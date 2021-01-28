

if __name__ == '__main__':

    nums = input('序列：').split(',')
    nums = [int(num) for num in nums]
    nums_sum = int(input('sum：'))
    nums_length = len(nums)
    result = -1
    left, right = 0, 1
    dp = [0] * nums_length

    while left < nums_length and right <= nums_length:
        if left == right:
            right += 1
        temp_sum = sum(nums[left: right])
        if temp_sum == nums_sum:
            result = max(right-left, result)
            right += 1
        elif temp_sum < nums_sum:
            right += 1
        elif temp_sum > nums_sum:
            left += 1

    print(result)
