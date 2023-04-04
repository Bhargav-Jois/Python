import random
def decor_strng(func):
    def wrap():
        print("\n------------------------")
        func()
        print("------------------------\n")
    return wrap

def decor_weak(func):
    def wrap():
        print("\n#####################")
        func()
        print("#####################\n")
        
    return wrap

print("\n##-->  Check if your password is strong  <--##")

@decor_strng
def print_strng():
    print("It is a STRONG password")

@decor_weak
def print_weak():
    print("Weak, think STRONGER")
    
while True:
    passwrd=input("\nEnter the Password: ")
    num_cnt=0;
    spl_count=0;
    spl_list=['!', '@', '#','!','$','~','%', '&', '*']
    
    if len(passwrd)<8:
        print_weak();
        print("--->Try adding more characters\n")
    else:
        for strn in passwrd:
            if strn.isdigit():
                num_cnt+=1
                
            if strn in spl_list:
                spl_count+=1
                
        if spl_count >1 and num_cnt>1:
            print_strng();
        else:
            passwrd_list=list(passwrd)
            for i in range(0,2):
                passwrd_list.insert(random.randint(0,len(passwrd)),random.choice(spl_list))
                num=random.randint(0,10)
                snum=str(num)
                passwrd_list.insert(random.randint(0,len(passwrd)),snum)
            strng_suggest=''.join(passwrd_list)
            print_weak();
            print(f"-->Try this: {strng_suggest}\n")
            
    print("Want to check another password? ", end="")
    cont=input("(y/n): ")
    
    if cont=='y' or cont=='Y':
        continue
    else:
        break
