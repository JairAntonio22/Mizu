FLAGS=-std=c++20 -Wall -Wextra -pedantic
TEST_FILE=factorial.mizu

all: build/mizu build/$(TEST_FILE)
	cd ./build && ./mizu $(TEST_FILE)

build/mizu: source/lexer_table.cpp ./source/*.cpp
	clang++ -o ./build/mizu ./source/main.cpp $(FLAGS)

build/$(TEST_FILE): examples/$(TEST_FILE)
	cp examples/$(TEST_FILE) build

source/lexer_table.cpp: tools/dfa.py
	python3 tools/dfa.py source/lexer_table.cpp

clean:
	rm -rf build/* source/lexer_table.cpp
