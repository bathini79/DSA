def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
    currSum = 0
    maxSum = 0
    for i in range(len(arr)): 
        currSum = currSum+arr[i]
        #For negative
        if(currSum<arr[i]):
            currSum = arr[i]
        maxSum = max(maxSum,max(currSum,arr[i]))
    return maxSum
