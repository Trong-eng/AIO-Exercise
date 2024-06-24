num_list = list(map(int,input().split()))
k = int(input())
def max_kernel(num_list, k):
    subarray = []   # creat a subarray to keep k numbers here 
    max_num_list = []
    for i in range(len(num_list)-k+1):# run from num_list[0] to num_list[len(num_list)-k] 
        for j in range(i, i+k):
            subarray.append(num_list[j])
        max_num_list.append(max(subarray))
        subarray.clear() # remove all the numbers here in order to the next subarray according to the code in line 5
    return max_num_list
assert max_kernel ([3 , 4 , 5 , 1 , -44] , 3) == [5 , 5 , 5]
print(max_kernel(num_list, k))