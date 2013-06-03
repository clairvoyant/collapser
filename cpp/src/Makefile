CC=g++
CFLAGS=-c -Wall
LDFLAGS=
OBJECTS=  csv-lexer.o csv-parser.tab.o   main.o
#OBJECTS=$(SOURCES:%.cc=.o)
EXECUTABLE=main

all: $(OBJECTS) $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS)  -o $@

clean:
	rm -f $(OBJECTS) csv-parser.tab.* lexer.c

csv-lexer.cc: csv-lexer.ll csv-parser.tab.cc
	flex   -+ -t $< > $@

csv-parser.tab.cc: csv-parser.yy
	bison  -d $< -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@
