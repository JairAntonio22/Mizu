// Add the following directives before including this file
// #include <iostream>
// #include <cstdlib>
// #include <fstream>
// #include <sstream>
// #include <array>
// #include <string>
// #include <set>
// #include <map>
//
// #include "lexer_table.cpp"

class Lexer {
    map<int, map<char, int>> table;
    set<int> acceptance_states;
    int state;

public:
    Lexer(string filename):
        table(_lexer_table),
        acceptance_states(_acceptance_states),
        state(1)
    {}

    void analize(string filename) {
        ifstream input(filename);

        if (!input.is_open()) {
            cerr << "Error: could not open " + filename + '\n';
            exit(EXIT_FAILURE);
        }

        string literal;
        char c;

        while (input.get(c)) {
            if (table.contains(state)) {
                if (table[state].contains(c)) {
                    state = table[state][c];
                    literal += c;
                } else {
                    literal.clear();
                    state = 1;
                }
            }

            if (acceptance_states.contains(state)) {
                cout << literal << '\n';
                literal.clear();
                state = 1;
            }
        }
    }
};
