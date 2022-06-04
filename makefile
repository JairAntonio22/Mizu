FLAGS=-std=c++20 -Wall -Wextra -pedantic

all: build/mizu build/primes_sieve.mizu
	cd ./build && ./mizu

build/mizu: source/lexer_table.cpp ./source/*.cpp
	clang++ -o ./build/mizu ./source/main.cpp $(FLAGS)

build/primes_sieve.mizu: examples/primes_sieve.mizu
	cp examples/primes_sieve.mizu build

source/lexer_table.cpp: tools/dfa.py
	python3 tools/dfa.py source/lexer_table.cpp

clean:
	rm -rf build/* source/lexer_table.cpp
