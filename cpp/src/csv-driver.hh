

#ifndef __GRAMMAR_H_
#  define __GRAMMAR_H_
#  include <string>
#  include <map>
#  include <FlexLexer.h>
 
namespace yy  {
class csv_driver; // forward reference... do not touch!!!!
}

#  define YY_DECL               \
   yy::csv_parser::token_type   \
      yylex (yy::csv_parser::semantic_type* yylval,      \
          yy::csv_parser::location_type* yylloc,      \
          yy::csv_driver& driver)
   // ... and declare it for the parser's sake.



#  include "csv-parser.tab.hh" 
namespace yy { 
class csv_driver: public yyFlexLexer
{
    public:
        csv_driver ();
        virtual ~csv_driver ();

        std::map<std::string, int> variables;

        int result;


        // Handling the scanner.
        void scan_begin ();
        void scan_end ();
        bool trace_scanning;

        //Similarly for the parser itself.

        // Handling the parser.
        void parse (const std::string& f);
        std::string file;
        bool trace_parsing;

        // Error handling.
        void error (const yy::location& l, const std::string& m);
        void error (const std::string& m);

    private:
        // save the pointer to yylval so we can change it, and invoke scan
        int yylex(yy::csv_driver::semantic_type * lval) { 
             yylval = lval;
             return yylex(); 
        }

    private:
        // Scanning function created by Flex; make this private to force u
        // of the overloaded method so we can get a pointer to Bison's yyl
        int yylex();

        // point to yylval (provided by Bison in overloaded yylex)
        semantic_type * yylval;
};


};


YY_DECL;



#endif
