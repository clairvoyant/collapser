

#include <boost/test/test_tools.hpp>
#include <boost/test/test_case_template.hpp>
#include <stdio.h>
using boost::unit_test::test_suite;

// Boost.MPL
#include <boost/mpl/range_c.hpp>

BOOST_TEST_CASE_TEMPLATE_FUNCTION( free_test_function, Number )
{
    printf("jrv::callback");
    BOOST_CHECK_EQUAL( 2, (int const)Number::value );
}

test_suite*
init_unit_test_suite( int, char* [] ) 
{
    test_suite* test= BOOST_TEST_SUITE( "Test case template example" );


    typedef boost::mpl::range_c<int,0,10> numbers;

    test->add( BOOST_TEST_CASE_TEMPLATE( free_test_function, numbers ) );

    return test;
}


int
main(int argc, char* argv[])
{

  init_unit_test_suite(argc, argv);

  return 0;
}



