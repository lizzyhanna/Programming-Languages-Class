
#turns word list into a dictionary of key, value pairs based on number of names
def word_freq(items):
    dictionary ={}
    for x in items:
        if(dictionary.get(x) == None):
            dictionary[x] = 1
        else:
            dictionary[x] = dictionary.get(x) + 1

    return dictionary        


#arranges dictionary from smallest to largest by value
def asc_word_freq(dictionary):
    my_list = list(dictionary.items())
    my_list.sort(key=lambda x: x[1])
    return my_list

#arranges dictionary from largest to smallest by value
def desc_word_freq(dictionary):
    dictionary.reverse()
    return dictionary

#trims dictionary based on user input
def size_dict(dictionary, n):
    if(n<0): #returns a blank dictionary if user gives a negative number
        return []
    elif(n > len(dictionary)): #returns entire dictionary if user's number is longer than length of dictionary
        return dictionary
    else: #trims dictionary to desired length
        i = 0
        dict = []
        for x in dictionary:
            if i == n:
                break
            else:
                dict.insert(i, dictionary[i])
                i += 1
        return dict        
            
            
        

        
        

def main():
    #list of words
    items = ["Liam", "Mason", "William", "Noah", "William", "James", "Sophia",
             "Logan", "Benjamin", "Mason", "Elijah", "Oliver", "Jacob", "Emma",
             "Olivia", "Ava", "William", "Isabella", "Oliver", "Sophia", "Mia",
             "Charlotte", "Amelia", "William", "Evelyn", "Abigail", "Olivia",
             "Ava", "Mason", "Isabella", "Noah", "William", "James", "Olivia",
             "Amelia", "Oliver", "William"]

    
     
    #send to function that will turn list into dictionary by counting number of words in list 
    dictionary = word_freq(items)
    print("Dictionary:")
    print(dictionary)

    #sorts by value lowest to highest
    dictionary = asc_word_freq(dictionary)
    print("Ascending Word Order:")
    print(dictionary)


    #sorts by value highest to lowest
    dictionary = desc_word_freq(dictionary)
    print("Descending Word Order:")
    print(dictionary)

    #receives int n from user to determine length of dictionary
    while True:
        try:
            n = int(input("Enter the number of terms to be displayed from the dictionary: "))
        except ValueError: #if user enters something other than a number, ask again
            print("Error: please enter a number.")
        else:
            #adjusts length of dictionary based on user's input
            dictionary = size_dict(dictionary, n)
            print(dictionary)
            break


#runs main
if __name__ == "__main__":
    main()
