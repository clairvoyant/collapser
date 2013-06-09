%{
#include <cstdlib>
#include <errno.h>
#include <limits.h>
#include "csv-driver.hh"
#include "csv-parser.tab.hh"

# undef yywrap
# define yywrap() 1

    
%}

/* options asumptions.
   no need for yywrap, unput...
   - yywrap is mostly used for including files aka # include
   - non interactive user
   - unput: chars are not going to be returned. 
   - trace for debuging purposes.
*/
%option noyywrap nounput batch debug

/* 
   track of lines and pos 
*/
%{
#define YY_USER_ACTION yylloc->columns(yyleng);
%}


%%

%{
  yylloc->step();
%}

\n                         { yylloc->lines(yyleng); yylloc->step(); }
[0-9]+                     { yylval = atoi(yytext); return yy::csv_parser::token::NUM; }
\"[^\"\n]*\"               { return yy::csv_parser::token::STR; }
[a-zA-Z][a-zA-Z0-9]*       { return yy::csv_parser::token::ID; }
\)                         { return yy::csv_parser::token::RPAREN;   }
\(                         { return yy::csv_parser::token::LPAREN; }
.
%%


void
csv_driver::scan_begin ()
{
    yy_flex_debug = trace_scanning;
    if (!(yyin = fopen (file.c_str (), "r")))
    error (std::string ("cannot open ") + file);
}

void
csv_driver::scan_end ()
{
    fclose (yyin);
}
