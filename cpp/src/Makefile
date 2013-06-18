CC=g++
CFLAGS=-c -Wall
LDFLAGS=
OBJECTS=      csv-lexer.o main.o  csv-parser.tab.o
#OBJECTS=$(SOURCES:%.cc=.o)
EXECUTABLE=main

all: $(OBJECTS) $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS)  -o $@

clean:
	rm -f $(OBJECTS) csv-parser.tab.* lexer.c position.hh location.hh *.yy.cc stack.hh csv-lexer.cc

csv-lexer.cc: csv-lexer.ll csv-parser.tab.cc
	flex   -o $@ $<

csv-parser.tab.cc: csv-parser.yy
	bison  $< -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@
