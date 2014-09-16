%require "2.4.1"
%skeleton "lalr1.cc"
%defines
%define namespace "CSV"
%define parser_class_name "BisonParser"
%parse-param { CSV::FlexLexer &scanner }
%lex-param   { CSV::FlexLexer &scanner }

%code requires {
	// Forward-declare the Scanner class; the Parser needs to be assigned a 
	// Scanner, but the Scanner can't be declared without the Parser
	namespace CSV {
		class FlexLexer;
	}
}

%code {
	// Prototype for the yylex function
	static int yylex(CSV::BisonParser::semantic_type * yylval, CSV::FlexLexer &scanner);
}

%token COMMA
%token STRING
%token DQUOTE
%token EOL

%%

csv
	: csv record 
	| record 
	;

record
	: fields field
    ;
fields
    : fields field
    | field
field
    : COMMA STRING COMMA
    | STRING 
    ;
    




%%

// We have to implement the error function
void CSV::BisonParser::error(const CSV::BisonParser::location_type &loc, const std::string &msg) {
	std::cerr << "Error: " << msg << std::endl;
}

// Now that we have the Parser declared, we can declare the Scanner and implement
// the yylex function
#include "CSVLexer.hh"
static int yylex(CSV::BisonParser::semantic_type * yylval, CSV::FlexLexer &scanner) {
	return scanner.yylex(yylval);
}
