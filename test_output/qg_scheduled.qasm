qubits 11

.QCirc1
    { prepz q0 | prepz q1 | prepz q2 | prepz q3 | prepz q4 | prepz q5 | prepz q6 | prepz q7 | prepz q8 | prepz q9 | prepz q10 }
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

