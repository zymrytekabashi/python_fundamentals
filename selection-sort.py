# selection sort algorithm

def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min = i
        for j in range(i+1, len(my_list)-1):
            if my_list[j] < my_list[min]:
                min = j
        smallerNumber=my_list[min]
        my_list[min]=my_list[i]
        my_list[i]=smallerNumber
my_list = [27,11,42,5,97,11,104]
print(my_list)
selection_sort(my_list)
print(my_list)
     