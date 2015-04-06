#include <iostream>

using namespace std;

int checkPrime(int current) {
    int i;
    for(i=2; i<current; i++) {
        if(i!=current && (current%i==0)) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int check;
    int lastPrime;
    int numPrimes = 6;
    int currentNum = 13;

    while(numPrimes < 10001) {
        currentNum++;
        check = checkPrime(currentNum);
        
        if(check) {
            lastPrime = currentNum;
            numPrimes++;
        }
    }
    
    cout << "The 10001st prime number is: " << lastPrime << endl;

    return 0;
}
