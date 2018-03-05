grammar TIS100;
start : (line? EOL)* line? EOF;
line : comment
     | instr
     | label;

//instr : label? opcode (argument | argument argument)?;
//instr : label? op=opcode (argument | argument argument)?;
instr : label? op=opcode argumentList;

argumentList : argument # ArgsOne
			 | argument argument #ArgsTwo
			 | # ArgsEmpty
			 ;
//argument : const | port;
argument : const
         | reg
         | commport
         | labelRef;

opcode : Nop | Mov | Add | Sub | Neg | Sav | Swp | Jmp | Jez | Jnz | Jgz | Jlz | Jro;
// port : reg | commport;

const : CONST;

reg : REG;
commport : COMMPORT;

label : LABEL_ID ':';
labelRef : LABEL_ID;

comment : COMMENT;

// I don't know yet how to do this as keywords or similar so that
// it doesn't scream or so that it gives proper error info
Nop : N O P;
Mov : M O V;
Add : A D D;
Sub : S U B;
Neg : N E G;
Sav : S A V;
Swp : S W P;
Jmp : J M P;
Jez : J E Z;
Jnz : J N Z;
Jgz : J G Z;
Jlz : J L Z;
Jro : J R O;


REG : N I L | A C C;
COMMPORT : L E F T | R I G H T | U P | D O W N | A N Y | L A S T;

CONST : SIGN? [0-9]+;
fragment SIGN : [-];

LABEL_ID : [a-zA-Z][a-zA-Z0-9]*;

COMMENT : '#' ~[\r\n]* -> skip;
EOL : [\r\n]+;
WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];