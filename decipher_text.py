# Write your script here
import statistics
from statistics import mode
import fnmatch

def convert(word):
    num = ""
    for i in range(0,len(word)):
        num = num + str(i)
        for k in range(i+1,len(word)):
            if(word[k] == word[i]):
                num = num + str(i)
    return num    

def dict_search(partial_key,partial_text,cipher_text):
    with open('./source/submissions/words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    
    a = cipher_text.replace("!","").replace(".","").replace(";","").replace(",","")
    sorted_cipher = (sorted(a.split(), key=len))
    sorted_cipher.reverse()

    keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
    new_dict = dict.fromkeys(keys)
    actual = []
    for i in range(0,3):
        for cipher in sorted_cipher:
            
            new_cipher = plain_text(a,partial_key)       
            new_sorted_cipher = (sorted(new_cipher.split(), key=len))
            new_sorted_cipher.reverse()
            if (("*" in new_sorted_cipher[sorted_cipher.index(cipher)])):
                
                if(len(actual)==2):
                    coded= actual[0]
                    original = actual[1]
                    for i in range(0,len(coded)):
                        partial_key[original[i]] = coded[i]
                        
                actual.clear()

                for word in valid_words:
                
                    if(len(word)== len(cipher) and fnmatch.fnmatch(word,new_sorted_cipher[sorted_cipher.index(cipher)])):
                        if((convert(cipher)== convert(word))):
                            actual.append(cipher)
                            actual.append(word)
                            
    return (partial_key)

def word_break(cipher_text):
    words = cipher_text.split()
    single_word = 0;bigram = 0;trigram = 0;long_words = 0
    single = [];double= [];triple= [];quad= [];others =[]

    for word in words:
        length = len(word)
        if (length== 1):
            single_word += 1
            single.append(word)
        elif(length==2):
            bigram +=1
            double.append(word) 
        elif(length==3):
            trigram +=1
            triple.append(word)
        elif(length==4):
            quad.append(word)
        else:
            long_words +=1
            others.append(word)
    keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
    d = dict.fromkeys(keys)

    if(len(single) != 0):
        d['a'] = single[0]

    the = mode(triple)
    d['t'] = the[0]
    d['h'] = the[1]
    d['e'] = the[2]

    for i in range(3):

        for qua in quad:
            if(qua[1]==d.get('i') and qua[2]==d.get('t') and qua[3]==d.get('h')):
                d['w'] = qua[0]

            if(qua[0]== qua[3] and qua[2]== d.get('a')):
                d['t'] = qua[0]
                d['h'] = qua[1]

            if(qua[0]== qua[3] and qua[2]== d.get('n')):
                d['v'] = qua[1]

            if(qua[0]== d.get('e') and qua[1]== d.get('a') and qua[3]== d.get('t')):
                d['s'] = qua[2]

            if(qua[1]== d.get('i') and qua[2]== d.get('t') and qua[3]== d.get('h')):
                d['w'] = qua[0]

            if(qua[1]== d.get('o') and qua[2]== d.get('s') and qua[3]== d.get('t')):
                d['m'] = qua[0]

        for digram in double:
            if (digram[0] == d.get('t')):
                d['o'] = digram[1]
            if (digram[0] == d.get('n')):
                d['o'] = digram[1]
            if (digram[0] == d.get('a') and digram[1] != d.get('t') ):
                d['n'] = digram[1]
            if(digram[1]==d.get('t') and digram[0] != d.get('a')):
                d['i'] = digram[0]
            if (digram[0] == d.get('h')):
                d['e'] = digram[1]
            if (digram[1] == d.get('s')):
                d['i'] = digram[0]
            if (digram[0] == d.get('b') and digram[1] != d.get('e')):
                d['y'] = digram[1]
        

    return d

def generate_key(d):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for key in alphabets:
        if (d.get(key) is None):
            d[key] = '*'
    return d

def generate_key(d):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for key in alphabets:
        if (d.get(key) is None):
            d[key] = '*'
    return d

def final_key(d):
    keys = ""  
    for alpha in list(d.values()):
            keys += alpha
    return keys

def get_key(val,d):
    for key, value in d.items():
        if val == value:
            return key
        elif (val == "!" or val =="," or val =="." or val ==";" or val ==" "):
            return val
    return "*"

def plain_text(cipher_text,d):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    keys = ""  
    for alpha in list(d.values()): 
        keys += alpha  

    d2 = dict((y,x) for x,y in d.items())
    return ''.join(get_key(c,d) for c in cipher_text)

class DecipherText(object): 
    def decipher(self, ciphertext): # Do not change this
        dict_value = word_break(ciphertext)
        partial_key = generate_key(dict_value)
        partial_text=plain_text(ciphertext,partial_key)
        output_key = dict_search(partial_key,partial_text,ciphertext)
        deciphered_text =plain_text(ciphertext,output_key)
        deciphered_key = final_key(output_key)

        print("Ciphertext: " + ciphertext) # Do not change this
        print("Deciphered Plaintext: " + deciphered_text) # Do not change this
        print("Deciphered Key: " + deciphered_key) # Do not change this

        return deciphered_text, deciphered_key # Do not change this
        

if __name__ == '__main__': # Do not change this
    DecipherText() # Do not change this
