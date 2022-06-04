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
    vector<Token> tokens = tokenize("primes_sieve.mizu");

    for (const Token &token : tokens) {
        cout << token << '\n';
    }
}
