class DFA:
    state_count = 1
    table = dict()
    acceptance_states = set()

    word: str
    children: list()
    is_terminal: bool
    state: int


    def __init__(self):
        self.word = ''
        self.children = [None] * 256
        self.is_terminal = True
        self.state = DFA.state_count

        DFA.acceptance_states.add(DFA.state_count);
        DFA.state_count += 1


    def add(self, word, depth=0):
        self.word = word[:depth]

        if len(word) - depth > 0:
            i = ord(word[depth:][0])
            self.is_terminal = False

            if self.state in DFA.acceptance_states:
                DFA.acceptance_states.remove(self.state);

            if self.children[i] is None:
                self.children[i] = DFA()

            self.children[i].add(word, depth + 1)


    def fill_table(self):
        DFA.table[self.state] = dict()

        for i, child in enumerate(self.children):
            if child:
                DFA.table[self.state][i] = child.state
                child.fill_table()


import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Error no output file name given')
        exit(0)

    keywords = [
        'module',
        'proc', 'return',
        'defer',
        'if', 'else', 'switch', 'case',
        'loop', 'break', 'skip',
        'not', 'and', 'or', 'true', 'false',
        'int', 'float', 'char', 'bool', 'byte', 'any',
        'enum', 'struct', 'union',
    ]

    dfa = DFA()

    for keyword in keywords:
        dfa.add(keyword)

    dfa.fill_table()

    with open(sys.argv[1], 'w') as file:
        file.write('map<int, map<char, int>> _lexer_table = {')

        for state, transitions in DFA.table.items():
            file.write('{')
            file.write(f'{state},')
            file.write('{')

            for char, next_state in transitions.items():
                file.write(f'{{\'{chr(char)}\',{next_state}}},')

            file.write('}')
            file.write('},')

        file.write('};\n')
        file.write('set<int> _acceptance_states = {')

        for state in DFA.acceptance_states:
            file.write(f'{state},')

        file.write('};\n')
