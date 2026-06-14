// #include <iostream> // Standard input/output stream
// #include <math.h> // Mathematical functions
#include <bits/stdc++.h> // Include all standard C++ libraries, useful in competitive programming but not recommended for production code
using namespace std;  // so you don't have to type std:: before every standard library function

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

void firstIfStatement() {
    int x = 10;
    if (x > 5) {
        cout << "x is greater than 5" << endl;
    } else {
        cout << "x is not greater than 5" << endl;
    }
}

void ifElseStatement() {
    int x = 'c';
    if (x == 'a') {
        cout << "x is a" << endl;
    } else if (x == 'b') {
        cout << "x is b" << endl;
    } else if (x == 'c') {
        cout << "x is c" << endl;
    } else {
        cout << "x is not a, b, or c" << endl;
    }
}

void switchStatement() {
    char grade = 'B';
    switch (grade) {
        case 'A':
            cout << "Excellent!" << endl;
            break; // break is necessary to prevent fall-through
        case 'B':
            cout << "Good job!" << endl;
            break;
        case 'C':
            cout << "You can do better." << endl;
            break;
        case 'D':
            cout << "Needs improvement." << endl;
            break;
        case 'F':
            cout << "Failing grade." << endl;
            break;
        default:
            cout << "Invalid grade." << endl;
    }
}

void firstForLoop() {
    for (int i = 0; i < 10; i++) {
        cout << i << " "; // prints numbers from 0 to 9
    }
}

void nestedForLoop() {
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            cout << "(" << i << ", " << j << ") "; // prints pairs of (i, j)
        }
        cout << endl; // new line after each row
    }
}

void whileLoop() {
    int i = 0;
    while (i < 5) {
        cout << i << " "; // prints numbers from 0 to 4
        i++;
    }
}

void firstFunctionPassByValue(int a) {
    a = a + 10; // modifies the local copy of a, does not affect the original variable passed to the function
    cout << "Value of a inside function: " << a << endl;
}

void firstFunctionPassByReference(int &a) {
    a = a + 10; // modifies the original variable passed to the function because it's passed by reference
    cout << "Value of a inside function: " << a << endl;
}

void rectangularStarPattern(int n) {
    for (int i = 0; i < n; i++) { // prints n number of lines 
        for (int i = 0; i < n; i++) { // prints n number of '*'
            cout << "* "; 
        }
        cout << endl; // makes new line 
    }
}

void rightAngledTrianglePattern(int n){
    for ( int i = 1; i < ( n + 1 ); i++ ) { // prints n number of rows 
        for ( int j = 0; j < i; j++ ) { // prints i numbers of "* " 
            cout << "* ";
        }
        cout << endl; // makes new line
    }
}

void rightAngledTriangleCountingNumberedPattern(int n){
    if ( n < 1 ){
        cout << "input is not a valid value";
        return;
    }
    for ( int i = 1; i < (n + 1); i++ ){ // prints n number of lines 
        for ( int j = 1; j < i; j++ ){ // prints i number of numbers 
            cout << j;
        }
        cout << endl;
    }

}

void rightAngledTriangleNumberedPattern(int n){
    for ( int i = 1; i < ( n + 1 ); i++ ) { // prints n number of rows
        for ( int j = 0; j < i; j++ ) { // prints i numbers of i value
            cout << i;
        }
        cout << endl; // makes new line
    }
}

int main() {
    rightAngledTriangleCountingNumberedPattern(10);
    return 0;
}

// Compile = g++ filename.cpp -o outputname
// Run = ./outputname

// while DSA : Ctrl + , to go to settings -> type "inline sugguestions" in search bar -> look for "Editor > Inline Suggest: Enabled" -> uncheck/check the box. 