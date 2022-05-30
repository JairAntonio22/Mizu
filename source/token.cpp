// Add the following directives before including this file
// #include <string>

using namespace std;

enum TokenType {
    MODULE = 128,
    PROC, RETURN,
    DEFER,
    IF, ELSE, SWITCH, CASE,
    LOOP, BREAK, SKIP,
    NOT, AND, OR, TRUE, FALSE,
    INT, FLOAT,  CHAR, BOOL, BYTE, ANY,
    ENUM, STRUCT, UNION
};

struct Token {
    string literal;
    TokenType type;

    Token(string literal, TokenType type):
        literal(literal),
        type(type)
    {}
};
