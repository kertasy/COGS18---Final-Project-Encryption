"""A collection of function for doing my project.""" 


def new_encoder(input_string, key = 200):
    """
    Encodes a string using a substitution cipher with a specified key, then .

    Parameters
    ----------
    input_string : str
        The string to be encoded. 
    key : int, optional
        The key value for the encoding process. Default = 200.

    Returns
    -------
    new_list: list
        A list of ASCII numerical values that represent the encoded string that was input by the user.
    """
    
    # 
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reverse_alphabet = 'zyxwvutsrqponmlkjihgfedcba'
    starter_list = []
    new_list = []
    
    # addresses if user inputs something that is not encryptable with this encryption method (i.e., not a string)
    if type(input_string) != str: 
        return 'Please input a string'
    
    # code from Lecture Notes 15-Code Projects
    for char in input_string: 
        char = char.lower()
        if char in alphabet: 
            position = alphabet.find(char)
            new_char = reverse_alphabet[position]
            
            # code from Assignment 2
            encoded_char = chr(ord(new_char) + key)
            starter_list.append(encoded_char)
    
    # creates a ASCII numerical value that corresponds to the letters in the given string
    for new_char in starter_list: 
        num_char = ord(new_char)
        new_list.append(num_char)
            
    return new_list


def new_decoder(new_list, key = 200):
    """
    Decodes a list of ASCII numerical values back to the original string using a specified key.

    Parameters
    ---------
    new_list : list 
        A list of ASCII numerical values that represent the encoded string.
    key : int, optional
        The key value used for the decoding process. Default = 200.

    Returns
    -------
    old_string: str
        The decoded string.
    """
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reverse_alphabet = 'zyxwvutsrqponmlkjihgfedcba'
    old_list = []
    old_string = ''
    
    # addresses if user inputs something that is not encryptable with this encryption method (i.e., not a list)
    if type(new_list) != list: 
        return 'Please input a list'
    
    # reverse the order of the new_encoder function
    for num_char in new_list: 
        new_char = chr(num_char)
        old_list.append(new_char)
        
    for new_char in old_list:
        decoded_char = chr(ord(new_char) - key)
        position = reverse_alphabet.find(decoded_char)
        input_char = alphabet[position]
        input_char = input_char.lower() 
        old_string += input_char
        
    return old_string


def binary_encoder(input_string): 
    """
    Encodes a string into its binary representation in a list format.

    Parameters
    ----------
    input_string : str 
        The string to be encoded.

    Returns
    -------
    binary_list : list
        A list of binary numbers that represent each letter in the input string.

    Reference
    ---------
    Geeks for Geeks : https://www.geeksforgeeks.org/python-convert-string-to-binary/# 
        Learned how to code a string into a singular line of joined binary code
    """
    
    binary_list = []
    
    # addresses if user inputs something that is not encryptable with this encryption method (i.e., not a string)
    if type(input_string) != str: 
        return 'Please input a string'
    
    # referenced Geeks for Geeks; instead of joining all binary codes, edited code to keep them separate for each letter
    for char in input_string: 
        binary_char = format(ord(char), '08b')
        binary_list.append(binary_char)
        
    return binary_list


def encryption(input_string, method='new_encryption'): 
    """
    Encrypts a string using a specified encyrption method by the user.

    Paramters
    ---------
    input_string : str 
        The string to be encrypted.
    method : str, optional 
        The encryption method to use. Defaults to 'new_encryption'.
            Supported methods: 
                - 'new_encryption': Uses a substitution cipher with a default key.
                - 'binary_encryption': Encodes the string into binary representation of numbers.

    Returns
    -------
    output : list
        The encrypted list of ASCII numbers or binary numbers, depending on the chosen encryption method.
    """
    
    # addresses if user inputs something that is not encryptable with this encryption method (i.e., not a string)
    if type(input_string) != str: 
        return 'Please input a string'
    
    # checks user's method input, then uses the corresponding function for the desired encryption type
    if method == 'new_encryption': 
        output = new_encoder(input_string)
    elif method == 'binary_encryption':
        output = binary_encoder(input_string)
    else: 
        output = "Please specify 'new_encryption' or 'binary_encryption' for your method of encryption"
    
    return output