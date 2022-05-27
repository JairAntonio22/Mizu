#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream input("test.mizu");

    if (!input.is_open()) {
        cout << "Error opening file\n";
    }

    while (!input.eof()) {
        char c = input.get();
    }
}
