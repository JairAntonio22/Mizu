all: build/mizu
	cd ./build && ./mizu

build/mizu: source/lexer_table.cpp $(wildcard ./source/*.cpp)
	clang++ -o ./build/mizu -std=c++20 -g ./source/main.cpp

source/lexer_table.cpp: tools/dfa.py
	python3 tools/dfa.py source/lexer_table.cpp

clean:
	rm -rf build/mizu build/mizu.dSYM source/lexer_table.cpp
