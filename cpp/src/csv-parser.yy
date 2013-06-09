
%skeleton "lalr1.cc"
%require "2.1a"
%defines
%define "parser_class_name" "csv_parser"


%{
#include <string>
#include "csv-driver.hh"
class csv_driver;

%}


// interface is a reference to the driver.
%parse-param { csv_driver& driver }
%lex-param   { csv_driver& driver }


// in case there is a location tracking...
%locations
%initial-action 
{
     // initial location
    @$.begin.filename = @$.end.filename = &driver.file;
}


// parser tracking and verbose output.
%debug
%error-verbose


%token LPAREN RPAREN ID NUM STR


// memory allocation 


%printer    { debug_stream () << *$$; } "identifier"
%destructor { delete $$; } "identifier"

%printer    { debug_stream () << $$; } "number" "expression"



%%


program: slist;

slist: slist sexpr | sexpr;

sexpr: atom                 {printf("matched sexpr\n");}
    | list
    ;
list: LPAREN members RPAREN {printf("matched list\n");}
    | LPAREN RPAREN         {printf("matched empty list\n");}
    ;
members: sexpr              {printf("members 1\n");}
    | sexpr members         {printf("members 2\n");}
    ;
atom: ID                    {printf("   ID\n");}
    | NUM                   {printf("   NUM\n");}
    | STR                   {printf("   STR\n");}
    ;
%%

void 
yy::csv_parser::error(const yy::calcxx_parser::location_type& l,
                                    const std::string& m)
{
    driver.error(l, m);
}

int 
yyFlexLexer::yywrap()
{
    return 1;
} 

