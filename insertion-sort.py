#insertion sort
def insertion_sort(my_list):
    for i in range(len(my_list)-1):
        for j in range(i, len(my_list)-1):
            while j>0 and my_list[j-1]<my_list[j]:
                j-=1
            my_list[i], my_list[i-1]=my_list[i-1], my_list[i]

my_list=[7,1,4,3,2]
insertion_sort(my_list)   
print(my_list)      
            
            
my_arr = [9,3,78,12,76,0,-2]

for idx in range(1, len(my_arr)): 
    temp = my_arr[idx] 
    prev_idx = idx-1
    while prev_idx >= 0 and temp < my_arr[prev_idx]: 
        my_arr[prev_idx + 1] = my_arr[prev_idx] 
        prev_idx -= 1
    my_arr[prev_idx + 1] = temp 

print(my_arr)
