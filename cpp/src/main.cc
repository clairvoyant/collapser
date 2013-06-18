


#include <iostream>
#include "CSVParser.hh"

int
main (int argc, char *argv[])
{
    CSV::Parser driver;

    // input parameters.
    for (++argv; argv[0]; ++argv) {
        if (*argv == std::string ("-p")) {
            std::cout << "jrv: option -p" << std::endl;
        } else if (*argv == std::string ("-s")) {
            std::cout << "jrv: option -s" << std::endl;
        } else
        {
            driver.parse ();
        }
    }
}

