#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

#include "lexer_table.cpp"
#include "lexer.cpp"

int main(int argc, char *argv[]) {
    if (argc != 2) {
        cout << "Usage: mizu <filename>\n";
        exit(EXIT_FAILURE);
    } 

    ifstream input(argv[1]);

    if (!input.is_open()) {
        cerr << "Error: could not open " << argv[1] << '\n';
        exit(EXIT_FAILURE);
    }

    vector<Token> tokens = tokenize(input);

    for (const Token &token : tokens) {
        cout << token << '\n';
    }
}
