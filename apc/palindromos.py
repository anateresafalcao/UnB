#string até 100 caracteres

def palindromo(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
string = input()    

if palindromo(string) == True:
    print('ON')

else:
    i = -1
    while palindromo(string) == False:
        i += 1
        
        if palindromo(string) == False:
            string = string.replace(string[i], string[-i], 1)
            
        elif palindromo(string) == True:
            funcionou = 'sim'
            print('ON')
            break
        
    funcionou = 'sim' 
    
    if funcionou != 'sim':
        print('OFF')
    else:
        print('ON')