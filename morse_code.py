#moss code translator for string inputs
def translator(text_tr):
    #Dictionary with morse code translation as value. 
    # * represents dots in morse code    
    morse_code = {
        'a' : ' * - ',
        'b' : ' - * * * ',
        'c' : ' - * - *',
        'd' : ' - * *',
        'e' : ' * ',
        'f' : ' * * - *',
        'g' : ' - - * ',
        'h' : ' * * * * ',
        'i' : ' * * ',
        'j' : ' * - - - ',
        'k' : ' - * - ',
        'l' : ' * - * * ',
        'm' : ' - - ',
        'n' : ' - * ',
        'o' : ' - - - ',
        'p' : ' * - - * ',
        'q' : ' - - * - ',
        'r' : ' * - * ',
        's' : ' * * * ',
        't' : ' - ',
        'u' : ' * * - ',
        'v' : ' * * * - ',
        'w' : ' * - - ',
        'x' : ' - * * - ',
        'y' : ' - * - - ',
        'z' : ' - - * * ',
        '1' : ' * - - - - ',
        '2' : ' * * - - - ',
        '3' : ' * * * - - ',
        '4' : ' * * * * - ',
        '5' : ' * * * * * ',
        '6' : ' - * * * * ',
        '7' : ' - - * * * ',
        '8' : ' - - - * * ',
        '9' : '  - - - - * ',
        '0' : ' - - - - - '
    }
    
    #split the sentence received into a list of strings at the whitespaces
    words = text_tr
    word = words.split(' ')
    
    #separating each string from the created list into single letter
    for item in word:
        for i in range(len(item)):
            item_obj = (item[i].lower())
            
            #compared the letters from the list to the keys in dictionary and output the value(Morse code equivalent)
            for key, value in morse_code.items():
                if key == item_obj:
                    print(morse_code.get(item_obj))
        #print a space at the end of a word            
        print(' ')
        
text_tr = input("Enter the text to translate: ")
print(translator(text_tr))
