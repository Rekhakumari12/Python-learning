def change(str):
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z','A','B','C','E','F','G','H','I','J','K','L','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','@','2','#','3','$','4','*','5','6','@','7','&','8','9','*','0']
    if str.isalnum():
        original_lst = []
        changed_lst = []
        for char1 in str:
            original_lst.append(char1)
        for char in original_lst:
            v = alpha.index(char)
            if alpha[v+1] in 'aioue':
                changed_lst.append(alpha[v+1].upper())
            else:
                changed_lst.append(alpha[v+1])
    return 'Your Passward : '+''.join(changed_lst)

def hint(choice):
    if choice=='y' or choice=='Y':
        print("\nyou can enter your- \nfavorite song\nfavorite festival\nfavorite movie\nfavorite food\nfavorite Actor/Actoress\nand many more..".title())
        
print("-----------PASSWORD PICKER----------------")
print("\nEnter any word:")
choice=input("Do you want any hint(y/n)")
hint(choice)
password=input("\nEnter Word : ")

print(change(password))

