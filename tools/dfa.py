class DFA:
    state_count = 1
    table = dict()
    acceptance_states = set()

    state: int
    children: dict


    def __init__(self):
        self.state = DFA.state_count
        self.children = dict()
        DFA.state_count += 1


    def add(self, word):
        if word:
            i = ord(word[0])

            if i not in self.children:
                self.children[i] = DFA()

            self.children[i].add(word[1:])

        else:
            DFA.acceptance_states.add(self.state);


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
        'module',
        'proc', 'return', 'defer',
        'if', 'else', 'switch', 'case',
        'loop', 'break', 'skip',
        'not', 'and', 'or', 'true', 'false',
        'int', 'float', 'char', 'bool', 'byte', 'any',
        'enum', 'struct', 'union',
        '::', ':=', '=', '.', ',',
        '(', ')', '{', '}', '[', ']',
        '==', '<=', '>=' '<', '>'
        '+' '-', '*' '/', '%'
    }

    dfa = DFA()

    for token in tokens:
        dfa.add(token)

    dfa.fill_table()

    with open(sys.argv[1], 'w') as file:
        file.write('const map<int, const map<char, int>> _lexer_table = {')

        for state, transitions in DFA.table.items():
            file.write('{')
            file.write(f'{state},')
            file.write('{')

            for char, next_state in transitions.items():
                file.write(f'{{\'{chr(char)}\',{next_state}}},')

            file.write('}')
            file.write('},')

        file.write('};\n')
        file.write('const set<int> _acceptance_states = {')

        for state in DFA.acceptance_states:
            file.write(f'{state},')

        file.write('};')
