

#include <vector>
#include <string>
#include<tr1/memory>

namespace bayes {


// CRITICAL all object are managed by shared ptr, even the containers. 
// only access to vector string is  by ... shared ptr.
// this make daunting sintax on
// pointers.


// class with an _ are not mean to be accesed directly
// class without an _ are the ones to be instanted

using   std::tr1::shared_ptr;
typedef shared_ptr<string> CString;
typedef shared_ptr<vector<StringPtr>> VectorString;
typedef VectorString::iterator VectorStringPtrIterator;


typedef shared_ptr<CSVReader> _CSVReader;


int 
parseCSV(VectorString filenames, Callback& cb, Memento& Params)
{
  int result = 0;


   for(StringPtr& filename=filenames.begin(); filename!=filenames.end(); it++) {
        CSVReader csv= CSVReader::open(filename);


        StringPtr row = csv.getRow(); // oops the big problem in C++ return and managing memory
                                  // either 
                                  //    - bottleneck.
                                  //    - memory leak. 
                                  //  note that vector is created, copied and their 
                                  // contents depend on shared pointers but the vector
                                  // is created and passed. 
                                  // a pool of object is a better option. 
                                  // shared_ptr is a good compromise by the time being
                                  // but a shared-ptr with an observer and pool is the key 
                                  // for performance, scalability, zero-copy and leak free code. 


        while (row !=NULL) {
           cb(row, params);
        }
        


   }




   return result;

};
