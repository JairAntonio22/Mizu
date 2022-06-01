FLAGS=-std=c++20 -Wall -Wextra -pedantic

all: build/mizu
	cd ./build && ./mizu

build/mizu: source/lexer_table.cpp ./source/*.cpp
	clang++ -o ./build/mizu ./source/main.cpp $(FLAGS)

source/lexer_table.cpp: tools/dfa.py
	python3 tools/dfa.py source/lexer_table.cpp

clean:
	rm -rf build/mizu build/mizu.dSYM source/lexer_table.cpp
