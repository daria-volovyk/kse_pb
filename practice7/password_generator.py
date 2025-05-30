import random
import string
def generate_password(length, allow_symbols):
    l=[]
    symbols=string.ascii_letters+string.digits
    symbols2=string.ascii_letters+string.digits+string.punctuation
    if(allow_symbols==True):
        for i in range(0, length):
            l.append(random.choice(symbols2))
        return("".join(l))
    if(allow_symbols==False):
        for i in range(0, length):
            l.append(random.choice(symbols2))
        return("".join(l))





