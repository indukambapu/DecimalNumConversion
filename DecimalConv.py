
def binaryConv(num):
    if num >= 1:
        binaryConv(num//2)
    print(num%2,end="")

def ocatalConv(num):
    if num>=1:
        ocatalConv(num//8)
    print(num%8,end='')

def hexaConv(num):
    if num>=1:
        hexaConv(num//16)
    print(num%16,end='')



cont = "yes"
while cont == "yes":
    choice = input(("Choose any to convert the decimal number to following conversions : 1.Binary, 2.Octal, 3.Hexa  : "))
    num = int(input("Enter the decimal number : "))
    if choice.lower()=='binary'.lower():
        binaryConv(num)
        print('\n')
    elif choice.lower()=='octal'.lower():
        ocatalConv(num)
        print('\n')
    elif choice.lower()=='hexa'.lower():
        hexaConv(num)
        print('\n')
    else:
        print("Enter a valid input")
        print('\n')

    cont = input("do you want to continue Yes/No : ").lower()
    print("--------------------------------------------------------------------------")
    print('\n')
