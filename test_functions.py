"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import new_encoder, new_decoder, binary_encoder, encryption
##
##

def test_new_encoder():  
    assert callable(new_encoder)
    assert isinstance(new_encoder('hello'), list)
    assert new_encoder('hello') == [315, 318, 311, 311, 308]
    assert new_encoder('HELLO') == [315, 318, 311, 311, 308]
    assert new_encoder(4) == 'Please input a string'
    assert new_encoder(2.0) == 'Please input a string'
    assert new_encoder(['wow', 2]) == 'Please input a string'
    assert new_encoder(('wow', 2)) == 'Please input a string'
    assert new_encoder({'wow': 2}) == 'Please input a string'
    assert new_encoder(True) == 'Please input a string'
    assert new_encoder(None) == 'Please input a string'
    
    
def test_new_decoder(): 
    assert callable(new_decoder)
    assert isinstance(new_decoder([315, 318, 311, 311, 308]), str)
    assert new_decoder([315, 318, 311, 311, 308]) == 'hello'
    assert new_decoder('hello') == 'Please input a list'
    assert new_decoder(4) == 'Please input a list'
    assert new_decoder(2.0) == 'Please input a list'
    assert new_decoder(('wow', 2)) == 'Please input a list'
    assert new_decoder({'wow': 2}) == 'Please input a list'
    assert new_decoder(True) == 'Please input a list'
    assert new_decoder(None) == 'Please input a list'


def test_binary_encoder(): 
    assert callable(binary_encoder)
    assert isinstance(binary_encoder('hello'), list)
    assert binary_encoder('hello') == ['01101000', '01100101', '01101100', '01101100', '01101111']
    assert binary_encoder(4) == 'Please input a string'
    assert binary_encoder(2.0) == 'Please input a string'
    assert binary_encoder(['wow', 2]) == 'Please input a string'
    assert binary_encoder(('wow', 2)) == 'Please input a string'
    assert binary_encoder({'wow': 2}) == 'Please input a string'
    assert binary_encoder(True) == 'Please input a string'
    assert binary_encoder(None) == 'Please input a string'
    assert binary_encoder(['wow', 'what']) == 'Please input a string'


def test_encryption(): 
    assert callable(encryption)
    assert isinstance(encryption('hello', method='new_encryption'), list)
    assert isinstance(encryption('hello', method='binary_encryption'), list)
    assert encryption('hello', method='new_encryption') == [315, 318, 311, 311, 308]
    assert encryption('hello', method='binary_encryption') == ['01101000', '01100101', '01101100', '01101100', '01101111']
    assert encryption('hello', method='augh') == "Please specify 'new_encryption' or 'binary_encryption' for your method of encryption"
    assert encryption(4) == 'Please input a string'
    assert encryption(2.0) == 'Please input a string'
    assert encryption(['wow', 2]) == 'Please input a string'
    assert encryption(('wow', 2)) == 'Please input a string'
    assert encryption({'wow': 2}) == 'Please input a string'
    assert encryption(True) == 'Please input a string'
    assert encryption(None) == 'Please input a string'
