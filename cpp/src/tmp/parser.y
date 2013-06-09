

{%

#include "Expression.h"
#include "Parser.h"
#include "Lexer.h"



int
yyerror(yyscan_t scanner, SExpression** exp, const char* msg)



%}


%code requires (
#ifndef YY_TYPEDEF_YY_SCANNER_T
#define YY_TYPEDEF_YY_SCANNER_T

  typedef void* yyscan_t;

#endif

}



%output  "Parser.c"
%defines "Parser.h"


%define api.pure
%lex-param { yyscan_t       scanner }
%parse-param {SExpression** Expression }
%parse-param {yyscan_t      scanner }


%union {
   int          value;
   SExpression* expression;
}


%left '+' TOKEN_PLUS
%left '*' TOKEN_MUL


%token EOL
%token EOF
%token SEP
%token STR
%token <value>     TOKEN_NUMBER

%type <expression> expr



csv:  /* empty * /
      | records EOF
    ;
records: records | record 
      ;
record: fields EOL
      ;

field: escapedfield 
      | normalfield;
      ;
escapedfield : STR STRING STR;
normalfield  : STRING;



