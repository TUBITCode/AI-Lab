solution(Q):-
    board(Q),
    queens(Q).

board([1/_,2/_,3/_,4/_,5/_,6/_,7/_,8/_]).

queens([]).
queens([R/C|Rest]):-
    queens(Rest),
    member(C, [1,2,3,4,5,6,7,8]),
    safe(R/C, Rest).

safe(_, []).
safe(R/C, [R1/C1|RCs]):-
    C =\= C1,
    C1 - C =\= R1 - R,
    C1 - C =\= R - R1,
    safe(R/C, RCs).
