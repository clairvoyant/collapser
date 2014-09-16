%{
 #include "CSVLexer.hh"
%}

%option nodefault yyclass="FlexLexer" noyywrap c++

%%


,            { return CSV::BisonParser::token::COMMA; }
\"           { return CSV::BisonParser::token::DQUOTE; }
\n           { return CSV::BisonParser::token::EOL; }

