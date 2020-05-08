#Lizzy Hanna, Callbox Developer Assessment, Exercise 1
#This is a program that, given an array of integers, x, sorts x and splits
#x into three smaller arrays of equal length. If x is not divisible by 3,
#then the sizes of the smaller arrays will decrease from the first array, as
#per the example.


def main():
    x = [2, 1, 3, 4, 7, 5, 9, 6, 8, 13, 12, 11, 10, 0, 15, 16, 17]
    print(array_sorter(x)) 


def array_sorter(x):
    x.sort()                 #sort array in ascending order
    final_array = []         #will hold smaller arrays
    n = int(len(x) / 3)      #min length of each smaller array

    remainder = int(len(x) % 3)
    #if remainder == 2, add 1 to the first two arrays
    #if remainder == 1, add 1 to the first array only
    
    counter = 0
    i = 0

    while i < 3:    #make 3 arrays
        sub_array = []
        j = 0
        
        while j < n: 
            sub_array.insert(j, x[counter])
            j += 1
            counter += 1
            
        if remainder > 0:
        #if n%3 != 0, then make first (and second if remainder ==2)
        #array larger
            
            if remainder == 1:
                sub_array.insert(j, x[counter])
                counter += 1
                remainder = 0
            else:
                sub_array.insert(j, x[counter])
                counter += 1
                remainder = 1

        #store smaller array in a larger array of arrays        
        final_array.append(sub_array)
        i += 1
            
    return final_array


    
        
#runs main
if __name__ == "__main__":
    main()      

      
