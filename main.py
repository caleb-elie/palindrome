def userInput(string):
    is_string = ''.join(char.lower() for char in string if char.isalnum())
    n = len(is_string)
    palindrome = set()
    
    
    for i in range(n):
        for j in range(i + 2, n + 1):
            substring = is_string[i:j]
            if substring == substring[::-1]:
                palindrome.add(substring)
                
        return list(palindrome)
        
input_string = input('Enter a string: ')
result = userInput(input_string)
if result:
    print(f'Palindrome substrings: {result}')
else:
    print(f'No palindrome substrings found')