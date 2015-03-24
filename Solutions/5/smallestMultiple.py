def main():
    i = 20
    while smallest(i):
        i = i + 1
    print i

def smallest(num):
    i = 1
    while (i<21) and ((num%i) == 0):
        i = i + 1
        if(i == 21):
            return 0
    return 1

if __name__ == '__main__':
    main()
