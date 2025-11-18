def matte(tal1, tal2):
    devison = tal1/tal2
    multiplikation = tal1*tal2
    addition = tal1+tal2
    return devison, multiplikation, addition

def main():
    tal1 = int(input("Tal1: "))
    tal2 = int(input("Tal2: "))
    print(matte(tal1,tal2))

main()