CC=g++
CFLAGS=-c -Wall
LDFLAGS=
OBJECTS=  lexer.o grammar.tab.o   main.o
#OBJECTS=$(SOURCES:%.cc=.o)
EXECUTABLE=main

all: $(OBJECTS) $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS)  -o $@

clean:
	rm -f $(OBJECTS) grammar.tab.* lexer.c

lexer.cc: lexer.lpp grammar.tab.cc
	flex   -+ -t $< > $@

grammar.tab.cc: grammar.ypp
	bison  -d $< -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@
