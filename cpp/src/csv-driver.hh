

#ifndef __GRAMMAR_H_
#  define __GRAMMAR_H_

#  include <string>
#  include <map>
#  include "csv-parser.tab.hh" 

#  define YY_DECL               \
#  yy::csv_parser::token_type   \
   yylex (yy::csv_parser::semantic_type* yylval,      \
          yy::csv_parser::location_type* yylloc,      \
          csv_driver& driver)
   // ... and declare it for the parser's sake.
YY_DECL;

class csv_driver
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
};



#endif
