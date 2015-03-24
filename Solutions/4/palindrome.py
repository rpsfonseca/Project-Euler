def main():
    maximum = 0
    i = 100

    while i<1001:
        j = 100
        while j<1001:
            product = i*j

            if( isPalindrome(product) == 1 ):
                if( product > maximum):
                    maximum = product

            j = j + 1
        i = i + 1
    print maximum

def isPalindrome(product):
    product = str(product)

    if(product[::-1] == product):
        return 1

if __name__ == '__main__':
    main()
