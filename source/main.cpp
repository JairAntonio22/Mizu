#include <iostream>
#include <type_traits>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

#include "lexer_table.cpp"
#include "lexer.cpp"

int main() {
    Lexer lexer;
    vector<Token> tokens = lexer.analize("test.mizu");

    for (const auto &token : tokens) {
        cout << token << '\n';
    }
}
