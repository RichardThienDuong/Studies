// #include <iostream> // Standard input/output stream
// #include <math.h> // Mathematical functions
#include <bits/stdc++.h> // Include all standard C++ libraries, useful in competitive programming but not recommended for production code
using namespace std;  // so you don't have to type std:: before every standard library function

// compile file first : g++ -o cppBasics cppBasics.cpp 
// to run file : ./cppBasics.exe 
// to compile and run in one step : g++ -o cppBasics cppBasics.cpp && ./cppBasics.exe

void helloWorld() {
    cout << "Hello, World" << "\n"; // cout is used for output
    cout << "Hey Hisuby" << endl; // "\n" or endl for line breaks
}

void myfirstCin() {
    int x;
    cin >> x; // cin is used for input, it will prompt you to enter a value in terminal 
    cout << "Value of x: " << x << endl;

    int a, b;
    cin >> a >> b; // example of multiple inputs : enter 10 20 
    cout << "Value of a: " << a << " and b: " << b << endl;
}

void myfirstArray() {
    char arr[8] = {'R', 'I', 'C', 'H', 'A', 'R', 'D', '\0'}; // character array (string) with null terminator to know where the string ends
    cout << arr << endl; // prints the string "RICHARD"
    int arr2[5] = {1, 2, 3, 4, 5}; // integer array of size 5
    cout << arr2[0] << endl; // prints the first element of the array
}

void myfirstString() {
    string s = "Hello, World"; // C++ string class, more convenient than character arrays
    cout << s << endl; // prints the string "Hello, World"
    cout << s.length() << endl; // prints the length of the string
    cout << s[0] << endl; // prints the first character of the string 
    s[0] = 'h'; // modify the first character of the string
    cout << s << endl; // prints the modified string "hello, World"
}


int main() {

    return 0;
}