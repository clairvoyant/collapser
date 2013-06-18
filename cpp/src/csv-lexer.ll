%{
	#include "csv-scanner.h"
%}

%option nodefault yyclass="FlexLexer" noyywrap c++

%%

[1-9][0-9]*  { *yylval = atoi(yytext); return CSV::BisonParser::token::INTEGER; }
.+|\n        { /* Ignore everything that isn't an integer */ }

