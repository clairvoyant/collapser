CC=g++
CFLAGS=-c -Wall
LDFLAGS=-lboost_unit_test_framework
SOURCES=test1.cc
OBJECTS=$(SOURCES:.cc=.o)
EXECUTABLE=main

all: $(SOURCES) $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

clean:
	rm $(OBJECTS)

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@
