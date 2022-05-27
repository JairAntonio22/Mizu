class DFA:
    state_count = 0
    table = dict()

    word: str
    children: list()
    is_terminal: bool
    state: int


    def __init__(self):
        self.state = DFA.state_count
        DFA.state_count += 1

        self.word = ''
        self.children = [None] * 256
        self.is_terminal = True


    def add(self, word, depth=0):
        self.word = word[:depth]

        if len(word) - depth > 0:
            i = ord(word[depth:][0])
            self.is_terminal = False

            if self.children[i] is None:
                self.children[i] = DFA()

            self.children[i].add(word, depth + 1)


    def print(self, depth=0):
        if self.is_terminal:
            print(self.word)

        for i, child in enumerate(self.children):
            if child:
                child.print(depth + 1)


    def fill_table(self):
        if self.is_terminal:
            DFA.table[self.state] = self.word
        else:
            DFA.table[self.state] = dict()

        for i, child in enumerate(self.children):
            if child:
                DFA.table[self.state][chr(i)] = child.state
                child.fill_table()


if __name__ == '__main__':
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

    dfa.print()
    dfa.fill_table()

    with open('mizu.tt', 'w') as file:
        for state, transitions in dfa.table.items():
            file.write(f'{state}\n')

            if isinstance(transitions, dict):
                for char, next_state in transitions.items():
                    file.write(f'{char} {next_state}\n')
            else:
                file.write(f'{transitions}\n')

            file.write('\n')

        file.write('-1')
