Input1= input("Enter a sentence: ")
search_word = 'CodeAcademy'

if(search_word in Input1):
    word1 = Input1.split()
    search_index1 = word1.index(search_word) + 1
    print("I found",search_word,"at",search_index1)
else:
    print("I didn't find CodeAcademy")
