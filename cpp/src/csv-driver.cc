
#include "csv-driver.hh"

csv_driver::csv_driver ():
   trace_scanning(false),
   trace_parsing(false)
{


}

virtual ~csv_driver::csv_driver ();
{
   //TODO free shared ptr...


}

void csv_driver::scan_begin ();
{


}
void csv_driver::scan_end ();

{


}

// Handling the parser.
void csv_driver::parse (const std::string& f);
{
   file = f;
   scan_begin();
   yy::csv_parser parser(*this);
   parser.set_debug_level(trace_parsing);
   parser.parse();
   scan_end();

}
void csv_driver::error (const yy::location& l, const std::string& m);
{
   std::cerr << l << ": " << m << std::endl;
}

void csv_driver::error (const std::string& m);
{
   std::cerr << m << std::endl;
}
