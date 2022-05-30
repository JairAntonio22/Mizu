#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <array>
#include <string>
#include <set>
#include <map>

#include "token.cpp"
#include "lexer_table.cpp"
#include "lexer.cpp"

using namespace std;

int main() {
    string filename("test.mizu");
    ifstream input(filename);

    if (!input.is_open()) {
        cout << "Error opening file " << filename << '\n';
        exit(EXIT_FAILURE);
    }

    Lexer lexer("mizu.lt");
    lexer.analize("test.mizu");
}
