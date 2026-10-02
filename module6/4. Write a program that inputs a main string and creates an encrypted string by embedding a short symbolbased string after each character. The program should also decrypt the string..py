str=input("Enter string : ")
enc_str="#".join(str)
print("Encrypted String :",enc_str)
dec_str=enc_str[::2]
print("Decrypted String :",dec_str)