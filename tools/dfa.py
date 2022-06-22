class DFA:
    state_count = 0
    table = dict()
    acceptance_states = dict()

    state: int
    children: dict


    def __init__(self):
        self.state = DFA.state_count
        self.children = dict()
        DFA.state_count += 1


    def add(self, token, literal):
        if literal:
            i = ord(literal[0])

            if i not in self.children:
                self.children[i] = DFA()

            self.children[i].add(token, literal[1:])

        else:
            DFA.acceptance_states[self.state] = token


    def fill_table(self):
        DFA.table[self.state] = dict()

        for i, child in self.children.items():
            DFA.table[self.state][i] = child.state
            child.fill_table()


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Error no output file name given')
        exit(0)

    tokens = {
        # control flow
        ('IF', 'if'),
        ('ELSE', 'else'),
        ('SWITCH', 'switch'),
        ('CASE', 'case'),
        ('DEFER', 'defer'),

        # loops
        ('LOOP', 'loop'),
        ('IN', 'in'),
        ('BREAK', 'break'),
        ('SKIP', 'skip'),

        # function
        ('PROC', 'proc'),
        ('RETURN', 'return'),

        # data types
        ('INT', 'int'),
        ('FLOAT', 'float'),

        # declaration operators
        ('DEF_CONST', '::'),
        ('DEF_VAR', ':='),

        # declaration delimiters
        # ('dot', '.'), ('comma', ','),

        # misc symbols
        ('LPAREN', '('),
        ('RPAREN', ')'),
        ('LBRACE', '{'),
        ('RBRACE', '}'),
        ('LBRACKET', '['),
        ('RBRACKET', ']'),

        # arithmetic operators
        ('PLUS', '+'),
        ('MINUS', '-'),
        ('MULT', '*'),
        ('DIV', '/'),
        ('MOD', '%'),

        # relational operators
        ('EQUALS', '=='),
        ('LESS', '<'),
        ('GREAT', '>'),
        ('LEQ', '<='),
        ('GEQ', '>='),

        # boolean operators
        ('NOT', 'not'),
        ('AND', 'and'),
        ('OR', 'or'),

        # bolean constants
        ('TRUE', 'true'),
        ('FALSE', 'false'),
    }

    dfa = DFA()

    for token, literal in tokens:
        dfa.add(token, literal)

    dfa.fill_table()

    with open(sys.argv[1], 'w') as file:
        # lexer table
        file.write('const map<int, const map<char, int>> lexer_table = {')

        for state, transitions in DFA.table.items():
            file.write(f'{{{state},{{')

            for char, next_state in transitions.items():
                file.write(f'{{\'{chr(char)}\',{next_state}}},')

            file.write('}},')

        file.write('};\n')

        # tokens enumeration
        file.write('enum class TokenType {')

        for token in DFA.acceptance_states.values():
            file.write(f'{token},')

        # acceptance states
        file.write('};\nconst map<int, TokenType> acceptance_states = {')

        for state, token_name in DFA.acceptance_states.items():
            file.write(f'{{{state},TokenType::{token_name}}},')

        file.write('};')
