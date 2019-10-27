CC=gcc
CFLAGS=-Wall -Wextra -I. -O1
LDFLAGS=-lgmp -lm -lprimesieve
DEPS=euler.h
OBJ=$(patsubst %.h, %.o, $(DEPS))
EXE=$(patsubst %.c, %, $(wildcard *.c))

e026 e031 e074 e076 e077 e092: $(OBJ) $(DEPS) *.c
	$(CC) $(CFLAGS) -c $@.c -o $@.o $(LDFLAGS)
	$(CC) $(CFLAGS) $(OBJ) $@.o -o $@ $(LDFLAGS)
default:
	$(CC) $(CFLAGS) $@.c -o $@ $(LDFLAGS)

.PHONY: clean
clean:
	rm -f *.o $(EXE)
