CC=g++
CFLAGS=-c -Wall
LDFLAGS=
SOURCES=main.cc
OBJECTS=$(SOURCES:.cc=.o)
EXECUTABLE=main

all: $(SOURCES) $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

clean:
	rm $(OBJECTS)

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@
