import random, string

print("\nPASSWORD GENERATOR in Python \U0001F512")
print("******************************")

try: 
    length_password = int(input("Desired Length of Password: "))
    if length_password<=0:
        print("Length of the password should be non-zero and positive...")
    else:
        s = string.ascii_lowercase+string.ascii_uppercase + string.digits + string.punctuation

            # string.ascii_lowercase - 'abcdefghijklmnopqrstuvwxyz'
            # string.ascii_uppercase - 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            # string.digits - '0123456789'
            #string.punctuation - !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.

    psd= ''.join(random.sample(s, length_password)) #generates random passsword
    print("Password ",psd) 
except:
    print("Enter in correct format...")