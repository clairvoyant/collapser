


#include <iostream>
#include "csv-driver.hh"

int
main (int argc, char *argv[])
{
    csv_driver driver;

    // input parameters.
    for (++argv; argv[0]; ++argv)
        if (*argv == std::string ("-p"))
            driver.trace_parsing = true;
        else if (*argv == std::string ("-s"))
            driver.trace_scanning = true;
        else
        {
            driver.parse (*argv);
            std::cout << driver.result << std::endl;
        }
}

