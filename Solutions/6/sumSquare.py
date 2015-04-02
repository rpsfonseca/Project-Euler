def squareIt(num):
    return num*num

if __name__ == '__main__':
    array = range(1,101)
    total = sum(array)

    for i in range(len(array)):
        array[i] = squareIt(array[i]) 
   
    print squareIt(total) - sum(array) 
