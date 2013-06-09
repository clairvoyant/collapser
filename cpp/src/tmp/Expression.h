


#ifndef _EXPRESSION_H_
#define _EXPRESSION_H_

typedef enum tag
{

    VALUE,
    MULTIPLY,
    PLUS
} SOperation;

typedef struc expression {

    int value;
    struct expression* left;
    struct expression* right;

} SExpression;

SExpression* createNumber(int value);
SExpression* createOperation(operation, SExpression*, SExpression* );




#endif // _EXPRESSION_H_
