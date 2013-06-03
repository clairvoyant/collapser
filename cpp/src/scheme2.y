%%
sexpr: atom                 {printf("matched sexpr\n");}
    | list
    ;
list: '(' members ')'       {printf("matched list\n");}
    | '('')'                {printf("matched empty list\n");}
    ;
members: sexpr              {printf("members 1\n");}
    | sexpr members         {printf("members 2\n");}
    ;
atom: ID                    {printf("ID\n");}
    | NUM                   {printf("NUM\n");}
    | STR                   {printf("STR\n");}
    ;
%%
