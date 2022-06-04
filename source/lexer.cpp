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

vector<Token> tokenize(string filename) {
    ifstream input(filename);

    if (!input.is_open()) {
        cerr << "Error: could not open " + filename + '\n';
        exit(EXIT_FAILURE);
    }

    vector<Token> tokens;
    string literal;
    unsigned line = 1, column = 1, state = 0;
    char c;

    while (input.get(c)) {
        if (lexer_table.at(state).contains(c)) {
            state = lexer_table.at(state).at(c);
            literal += c;

        } else {
            if (acceptance_states.contains(state)) {
                TokenType type = TokenType::PROC;
                unsigned start = column - literal.size() + 1;
                tokens.emplace_back(literal, type, line, start);
            }

            literal.clear();
            state = 0;

            if (lexer_table.at(state).contains(c)) {
                state = lexer_table.at(state).at(c);
                literal += c;
            }
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
