#fixed length sliding window
def findMaxAverage(nums, k):

    if len(nums)<k:
        return 0
    cur_sum=0
    for i in range(k):
        cur_sum+=nums[i]
    max_sum=cur_sum
    for i in range(k,len(nums)):
        cur_sum+=nums[i]-nums[i-k]
        max_sum=max(cur_sum,max_sum)
    return float(max_sum)/k
print(findMaxAverage([1,2,3,-3,-9,10,2],4))