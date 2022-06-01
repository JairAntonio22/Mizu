enum class TokenType {
    MODULE = 128,
    PROC, RETURN,
    DEFER,
    IF, ELSE, SWITCH, CASE,
    LOOP, BREAK, SKIP,
    NOT, AND, OR, TRUE_CONST, FALSE_CONST,
    INT, FLOAT, CHAR, BOOL, BYTE, ANY,
    ENUM, STRUCT, UNION
};

struct Token {
    const string literal;
    const TokenType type;
    const unsigned line;
    const unsigned column;

    Token(string literal, TokenType type, unsigned line, unsigned column):
        literal(literal),
        type(type),
        line(line),
        column(column)
    {}
};

ostream& operator<<(ostream &os, Token token) {
    os << token.literal;
    return os;
}

class Lexer {
    const map<int, const map<char, int>> table = _lexer_table;
    const set<int> acceptance_states = _acceptance_states;
    int state = 1;

public:
    vector<Token> analize(string filename) {
        ifstream input(filename);

        if (!input.is_open()) {
            cerr << "Error: could not open " + filename + '\n';
            exit(EXIT_FAILURE);
        }

        vector<Token> tokens;
        string literal;
        unsigned line = 1, column = 1;
        char c;

        while (input.get(c)) {
            if (table.at(state).contains(c)) {
                state = table.at(state).at(c);
            } else {
                literal.clear();
                state = 1;
            }

            if (acceptance_states.contains(state)) {
                TokenType type = TokenType::PROC;
                unsigned start_column = column - literal.size() + 1;
                tokens.emplace_back(literal, type, line, start_column);
            } else {
                literal += c;
            }

            if (c == '\n') {
                line++;
                column = 1;
            } else {
                column++;
            }
        }

        return tokens;
    }
};
