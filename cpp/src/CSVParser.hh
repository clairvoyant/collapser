#ifndef __CSVPARSER__
#define __CSVPARSER__

#include "CSVLexer.hh"

namespace CSV {
	class Parser {
		public:
			Parser() : parser(scanner) {}
		
			int parse() {
				return parser.parse();
			}
		
		private:
			CSV::FlexLexer scanner;
			CSV::BisonParser parser;
	};
}


#endif
