qubits 17

.QCirc1
    { prepz q0 | prepz q1 | prepz q2 | prepz q3 | prepz q4 | prepz q5 | prepz q6 | prepz q7 | prepz q8 | prepz q9 | prepz q10 | prepz q11 | prepz q12 | prepz q13 | prepz q14 | prepz q15 | prepz q16 }
    { h q0 | h q1 | h q2 | x q7 | x q9 }
    { x q0 | x q1 | x q2 }
    toffoli q0,q1,q11
    qwait 31
    toffoli q2,q11,q12
    qwait 31
    cnot q12,q3
    qwait 15
    toffoli q2,q11,q12
    qwait 31
    toffoli q0,q1,q11
    qwait 31
    toffoli q0,q1,q11
    qwait 31
    toffoli q2,q11,q12
    qwait 31
    cnot q12,q4
    qwait 15
    toffoli q2,q11,q12
    qwait 31
    { toffoli q0,q1,q11 | x q2 }
    qwait 31
    { x q0 | x q1 }
    { x q0 | x q1 }
    toffoli q0,q1,q11
    qwait 31
    toffoli q2,q11,q12
    qwait 31
    cnot q12,q3
    qwait 15
    toffoli q2,q11,q12
    qwait 31
    toffoli q0,q1,q11
    qwait 31
    toffoli q0,q1,q11
    qwait 31
    toffoli q2,q11,q12
    qwait 31
    cnot q12,q6
    qwait 15
    toffoli q2,q11,q12
    qwait 31
    { toffoli q0,q1,q11 | x q2 }
    qwait 31
    { x q0 | x q1 }
    x q0
    toffoli q0,q1,q11
    qwait 31
    toffoli q2,q11,q12
    qwait 31
    cnot q12,q5
    qwait 15
    toffoli q2,q11,q12
    qwait 31
    { toffoli q0,q1,q11 | x q2 }
    qwait 31
    x q0
    x q0
    toffoli q0,q1,q11
    qwait 31
    toffoli q2,q11,q12
    qwait 31
    cnot q12,q4
    qwait 15
    toffoli q2,q11,q12
    qwait 31
    toffoli q0,q1,q11
    qwait 31
    toffoli q0,q1,q11
    qwait 31
    toffoli q2,q11,q12
    qwait 31
    cnot q12,q6
    qwait 15
    toffoli q2,q11,q12
    qwait 31
    { toffoli q0,q1,q11 | x q2 }
    qwait 31
    { x q0 | x q1 }
    toffoli q0,q1,q11
    qwait 31
    toffoli q2,q11,q12
    qwait 31
    cnot q12,q3
    qwait 15
    toffoli q2,q11,q12
    qwait 31
    toffoli q0,q1,q11
    qwait 31
    toffoli q0,q1,q11
    qwait 31
    toffoli q2,q11,q12
    qwait 31
    cnot q12,q5
    qwait 15
    { toffoli q2,q11,q12 | cnot q9,q5 }
    qwait 15
    x q5
    qwait 15
    { toffoli q0,q1,q11 | x q2 }
    qwait 31
    x q1
    x q1
    toffoli q0,q1,q11
    qwait 31
    toffoli q2,q11,q12
    qwait 31
    cnot q12,q4
    qwait 15
    { toffoli q2,q11,q12 | cnot q8,q4 }
    qwait 15
    x q4
    qwait 15
    { toffoli q0,q1,q11 | x q2 }
    qwait 31
    x q1
    toffoli q0,q1,q11
    qwait 31
    toffoli q2,q11,q12
    qwait 31
    cnot q12,q3
    qwait 15
    { toffoli q2,q11,q12 | cnot q7,q3 }
    qwait 15
    x q3
    h q3
    qwait 14
    { toffoli q0,q1,q11 | x q2 }
    qwait 31
    toffoli q0,q1,q11
    qwait 31
    toffoli q2,q11,q12
    qwait 31
    cnot q12,q6
    qwait 15
    { toffoli q2,q11,q12 | cnot q10,q6 }
    qwait 15
    x q6
    qwait 15
    toffoli q0,q1,q11
    qwait 31
    toffoli q4,q5,q11
    qwait 31
    toffoli q6,q11,q12
    qwait 31
    cnot q12,q3
    qwait 15
    { toffoli q6,q11,q12 | h q3 }
    x q3
    qwait 30
    { toffoli q4,q5,q11 | x q6 }
    qwait 31
    { x q4 | x q5 }


.QCirc3
    { h q0 | h q1 | h q2 | h q3 | h q4 | h q5 | h q6 }
    { x q0 | x q1 | x q2 | x q3 | x q4 | x q5 | x q6 }
    { h q0 | toffoli q1,q2,q11 }
    qwait 31
    toffoli q3,q11,q12
    qwait 31
    toffoli q4,q12,q13
    qwait 31
    toffoli q5,q13,q14
    qwait 31
    toffoli q6,q14,q15
    qwait 31
    cnot q15,q0
    qwait 15
    { toffoli q6,q14,q15 | h q0 }
    x q0
    h q0
    qwait 29
    { toffoli q5,q13,q14 | x q6 }
    h q6
    qwait 30
    { toffoli q4,q12,q13 | x q5 }
    h q5
    qwait 30
    { toffoli q3,q11,q12 | x q4 }
    h q4
    qwait 30
    { toffoli q1,q2,q11 | x q3 }
    h q3
    qwait 30
    { x q1 | x q2 }
    { h q1 | h q2 }

