import string


def is_pangram(sentence):
    uppercase_list = list(string.ascii_uppercase)
    sentence1 = sentence.replace(" ", "")
    finalsentence = sentence1.upper()

    for i in finalsentence:
        if i in uppercase_list:
            uppercase_list.remove(i)

    if uppercase_list == []:
        return True
    else:
        return False

is_pangram('test1')
is_pangram('test2')



     
    
