

// programing record
//            Fri 26, 19:30

#include <map>


namespace bayes {



class CCollapser: public CObject
{

   public:
        virtual ~CCollapser();
        void init();
        void release();

        int  do(Record&);

        public operator<<(&CCollapser);

   private:
        CCollapser();
        Collapser& CCollapser();
        Collapser& CCollapser(Collapser& );

};


} // namespace bayes
