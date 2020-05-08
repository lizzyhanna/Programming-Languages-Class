

#reads text from a file and turns text into list of words
def read_file(file_name):
    f = open(file_name, "r")
    word_list = []
    for x in f:
        for word in x.split():
            word_list.append(word)
    return word_list

#creates dictionary from list (key: word, value: quantity)    
def word_freq(word_list):
    dictionary = {}
    for x in word_list:
        if(dictionary.get(x) == None):
            dictionary[x] = 1
        else:
            dictionary[x] = dictionary.get(x) + 1
    return dictionary  

#accepts list, returns set
def word_no_duplicate(word_list):
    word_set = set()
    for x in word_list:
        word_set.add(x)
    return word_set

#accepts dictionary, return set
def dic_no_duplicate(dictionary):
    word_set = set()
    for k in dictionary:
        word_set.add(k)    
    return word_set
#main method
def main():
    while True:
        try:
            file_name = input("Enter the name of the file: ")
            word_list = read_file(file_name)
        except IOError:
            print("Unable to open file.")
        else:
            print("Word List")
            print(word_list)
            dictionary = word_freq(word_list)
            print()
            print("Dictionary")
            print(dictionary)
            word_set = word_no_duplicate(word_list)
            print()
            print("word_no_duplicates Set")
            print(word_set)
            word_set = dic_no_duplicate(dictionary)
            print()
            print("dic_no_duplicates Set")      
            print(word_set)
            break


#runs main
if __name__ == "__main__":
    main()    
