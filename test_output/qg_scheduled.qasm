qubits 8

.QCirc1
    { prepz q0 | prepz q1 | prepz q2 | prepz q3 | prepz q4 | prepz q5 | prepz q6 | prepz q7 }
    { h q0 | h q1 | h q2 }
    { x q0 | x q1 | x q2 }
    toffoli q0,q1,q7
    qwait 31
    toffoli q2,q7,q3
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    toffoli q2,q7,q3
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    toffoli q2,q7,q4
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    { toffoli q2,q7,q4 | x q0 | x q1 }
    { x q0 | x q1 }
    qwait 30
    { x q2 | toffoli q0,q1,q7 }
    qwait 31
    toffoli q2,q7,q3
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    toffoli q2,q7,q3
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    toffoli q2,q7,q6
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    { toffoli q2,q7,q6 | x q0 | x q1 }
    x q0
    qwait 30
    { x q2 | toffoli q0,q1,q7 }
    qwait 31
    toffoli q2,q7,q5
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    { toffoli q2,q7,q5 | x q0 }
    x q0
    qwait 30
    { x q2 | toffoli q0,q1,q7 }
    qwait 31
    toffoli q2,q7,q4
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    toffoli q2,q7,q4
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    toffoli q2,q7,q6
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    { toffoli q2,q7,q6 | x q0 | x q1 }
    qwait 31
    { x q2 | toffoli q0,q1,q7 }
    qwait 31
    toffoli q2,q7,q3
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    toffoli q2,q7,q3
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    toffoli q2,q7,q5
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    { toffoli q2,q7,q5 | x q1 }
    x q1
    qwait 30
    { x q2 | toffoli q0,q1,q7 }
    qwait 31
    toffoli q2,q7,q4
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    { toffoli q2,q7,q4 | x q1 }
    qwait 31
    { x q2 | toffoli q0,q1,q7 }
    qwait 31
    toffoli q2,q7,q3
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    toffoli q2,q7,q3
    qwait 31
    { x q2 | toffoli q0,q1,q7 }
    qwait 31
    toffoli q2,q7,q6
    qwait 31
    toffoli q0,q1,q7
    qwait 31
    toffoli q2,q7,q6


.QCirc2
    { x q3 | x q5 }


.QCirc3
    { x q3 | x q4 | x q5 | x q6 }
    { h q3 | toffoli q4,q5,q0 }
    qwait 31
    toffoli q6,q0,q3
    qwait 31
    toffoli q4,q5,q0
    qwait 31
    { toffoli q6,q0,q3 | x q4 | x q5 }
    qwait 31
    { h q3 | x q6 }
    x q3


.QCirc4
    { h q0 | h q1 | h q2 | h q3 | h q4 | h q5 | h q6 }
    { x q0 | x q1 | x q2 | x q3 | x q4 | x q5 | x q6 }
    { h q0 | toffoli q1,q2,q4 }
    qwait 31
    toffoli q3,q4,q7
    qwait 31
    toffoli q1,q2,q4
    qwait 31
    toffoli q3,q4,q7
    qwait 31
    { toffoli q4,q5,q2 | toffoli q6,q7,q1 }
    qwait 31
    toffoli q2,q1,q0
    qwait 31
    toffoli q6,q7,q1
    qwait 31
    toffoli q2,q1,q0
    qwait 31
    { toffoli q4,q5,q2 | toffoli q6,q7,q1 }
    qwait 31
    toffoli q2,q1,q0
    qwait 31
    toffoli q6,q7,q1
    qwait 31
    toffoli q2,q1,q0
    qwait 31
    toffoli q1,q2,q4
    qwait 31
    toffoli q3,q4,q7
    qwait 31
    toffoli q1,q2,q4
    qwait 31
    toffoli q3,q4,q7
    qwait 31
    { toffoli q4,q5,q2 | toffoli q6,q7,q1 | x q3 }
    h q3
    qwait 30
    toffoli q2,q1,q0
    qwait 31
    toffoli q6,q7,q1
    qwait 31
    toffoli q2,q1,q0
    qwait 31
    { toffoli q4,q5,q2 | toffoli q6,q7,q1 }
    qwait 31
    { toffoli q2,q1,q0 | x q4 | x q5 }
    { h q4 | h q5 }
    qwait 30
    toffoli q6,q7,q1
    qwait 31
    { toffoli q2,q1,q0 | x q6 }
    h q6
    qwait 30
    { h q0 | x q1 | x q2 }
    { x q0 | h q1 | h q2 }
    h q0


.QCirc3
    { x q3 | x q4 | x q5 | x q6 }
    { h q3 | toffoli q4,q5,q0 }
    qwait 31
    toffoli q6,q0,q3
    qwait 31
    toffoli q4,q5,q0
    qwait 31
    { toffoli q6,q0,q3 | x q4 | x q5 }
    qwait 31
    { h q3 | x q6 }
    x q3


.QCirc4
    { h q0 | h q1 | h q2 | h q3 | h q4 | h q5 | h q6 }
    { x q0 | x q1 | x q2 | x q3 | x q4 | x q5 | x q6 }
    { h q0 | toffoli q1,q2,q4 }
    qwait 31
    toffoli q3,q4,q7
    qwait 31
    toffoli q1,q2,q4
    qwait 31
    toffoli q3,q4,q7
    qwait 31
    { toffoli q4,q5,q2 | toffoli q6,q7,q1 }
    qwait 31
    toffoli q2,q1,q0
    qwait 31
    toffoli q6,q7,q1
    qwait 31
    toffoli q2,q1,q0
    qwait 31
    { toffoli q4,q5,q2 | toffoli q6,q7,q1 }
    qwait 31
    toffoli q2,q1,q0
    qwait 31
    toffoli q6,q7,q1
    qwait 31
    toffoli q2,q1,q0
    qwait 31
    toffoli q1,q2,q4
    qwait 31
    toffoli q3,q4,q7
    qwait 31
    toffoli q1,q2,q4
    qwait 31
    toffoli q3,q4,q7
    qwait 31
    { toffoli q4,q5,q2 | toffoli q6,q7,q1 | x q3 }
    h q3
    qwait 30
    toffoli q2,q1,q0
    qwait 31
    toffoli q6,q7,q1
    qwait 31
    toffoli q2,q1,q0
    qwait 31
    { toffoli q4,q5,q2 | toffoli q6,q7,q1 }
    qwait 31
    { toffoli q2,q1,q0 | x q4 | x q5 }
    { h q4 | h q5 }
    qwait 30
    toffoli q6,q7,q1
    qwait 31
    { toffoli q2,q1,q0 | x q6 }
    h q6
    qwait 30
    { h q0 | x q1 | x q2 }
    { x q0 | h q1 | h q2 }
    h q0

