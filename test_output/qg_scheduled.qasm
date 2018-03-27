qubits 7

.QCirc1
    { prepz q0 | prepz q1 | prepz q2 | prepz q3 | prepz q4 | prepz q5 | prepz q6 }
    { h q0 | h q1 | h q2 }
    { x q0 | x q1 | x q2 }
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q3
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q3
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q4
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q4
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q5
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    { toffoli q2,q6,q5 | x q0 | x q1 }
    { x q0 | x q1 }
    qwait 30
    { x q2 | toffoli q0,q1,q6 }
    qwait 31
    toffoli q2,q6,q3
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q3
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q4
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q4
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q5
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    { toffoli q2,q6,q5 | x q0 | x q1 }
    x q0
    qwait 30
    { x q2 | toffoli q0,q1,q6 }
    qwait 31
    toffoli q2,q6,q4
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    { toffoli q2,q6,q4 | x q0 }
    x q0
    qwait 30
    { x q2 | toffoli q0,q1,q6 }
    qwait 31
    toffoli q2,q6,q4
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q4
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q5
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    { toffoli q2,q6,q5 | x q0 | x q1 }
    qwait 31
    { x q2 | toffoli q0,q1,q6 }
    qwait 31
    toffoli q2,q6,q3
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    { toffoli q2,q6,q3 | x q1 }
    x q1
    qwait 30
    { x q2 | toffoli q0,q1,q6 }
    qwait 31
    toffoli q2,q6,q3
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q3
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q5
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    { toffoli q2,q6,q5 | x q1 }
    qwait 31
    { x q2 | toffoli q0,q1,q6 }
    qwait 31
    toffoli q2,q6,q3
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q3
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q4
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q4
    qwait 31
    { x q2 | toffoli q0,q1,q6 }
    qwait 31
    toffoli q2,q6,q3
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q3
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q4
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q4
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q5
    qwait 31
    toffoli q0,q1,q6
    qwait 31
    toffoli q2,q6,q5
    qwait 31


.QCirc3
    { cnot q0,q3 | cnot q1,q4 | cnot q2,q5 }
    qwait 15
    { cnot q3,q0 | cnot q4,q1 | cnot q5,q2 }
    qwait 15
    { cnot q0,q3 | cnot q1,q4 | cnot q2,q5 }
    qwait 15
    { rz q0, -3.141593 | rz q1, 1.570796 | rz q2, -1.570796 }
    qwait 7
    ry q0, -1.749068
    qwait 7
    rz q0, -1.570796
    qwait 7
    cnot q0,q1
    qwait 15
    rz q1, -1.570796
    qwait 7
    cnot q0,q1
    qwait 15
    { rz q0, -3.141593 | ry q1, 1.733418 }
    qwait 7
    ry q0, -0.504834
    qwait 7
    rz q0, 3.141593
    qwait 7
    cnot q0,q1
    qwait 15
    ry q1, 0.762379
    qwait 7
    cnot q0,q1
    qwait 15
    { rz q0, -0.535601 | rz q1, -0.785398 }
    qwait 7
    ry q0, -1.437175
    qwait 7
    rz q0, -1.157558
    qwait 7
    cnot q0,q1
    qwait 15
    rz q1, 0.960879
    qwait 7
    cnot q0,q1
    qwait 15
    rz q0, 0.626540
    qwait 7
    ry q0, -1.040477
    qwait 7
    rz q0, -0.626540
    qwait 7
    cnot q0,q2
    qwait 15
    rz q2, -0.021343
    qwait 7
    cnot q1,q2
    qwait 15
    rz q2, 0.021343
    qwait 7
    cnot q0,q2
    qwait 15
    { rz q2, -1.570796 | rz q0, 2.285636 }
    qwait 7
    { cnot q1,q2 | ry q0, -2.217616 }
    qwait 7
    rz q0, 0.654520
    qwait 7
    { rz q1, -0.785398 | ry q2, 0.523599 }
    qwait 7
    cnot q0,q1
    qwait 15
    rz q1, -1.088849
    qwait 7
    cnot q0,q1
    qwait 15
    { rz q0, 2.140665 | ry q1, 0.536833 }
    qwait 7
    ry q0, -0.797715
    qwait 7
    rz q0, -2.140665
    qwait 7
    cnot q0,q1
    qwait 15
    ry q1, 0.536833
    qwait 7
    cnot q0,q1
    qwait 15
    rz q0, 4.712389
    qwait 7
    ry q0, -1.570796
    qwait 7
    rz q0, 0.815214
    qwait 7
    cnot q0,q1
    qwait 15
    rz q1, -0.815214
    qwait 7
    cnot q0,q1
    qwait 15
    ry q0, -1.570796
    qwait 7
    rz q0, -1.570796
    qwait 7
    cnot q0,q2
    qwait 15
    ry q2, 0.523599
    qwait 7
    cnot q1,q2
    qwait 15
    ry q2, 0.523599
    qwait 7
    cnot q0,q2
    qwait 15
    { ry q2, 0.523599 | rz q0, -3.141593 }
    qwait 7
    { cnot q1,q2 | ry q0, -2.326379 }
    qwait 7
    rz q0, -1.570796
    qwait 7
    { rz q1, 1.570796 | rz q2, -0.785398 }
    qwait 7
    cnot q0,q1
    qwait 15
    rz q1, 1.570796
    qwait 7
    cnot q0,q1
    qwait 15
    { ry q0, -0.815214 | ry q1, 0.536833 }
    qwait 7
    cnot q0,q1
    qwait 15
    ry q1, 0.536833
    qwait 7
    cnot q0,q1
    qwait 15
    rz q0, -2.780856
    qwait 7
    ry q0, -1.231483
    qwait 7
    rz q0, -2.779386
    qwait 7
    cnot q0,q1
    qwait 15
    rz q1, -2.293740
    qwait 7
    cnot q0,q1
    qwait 15
    rz q0, 1.931533
    qwait 7
    ry q0, -1.231483
    qwait 7
    rz q0, -1.931533
    qwait 7
    cnot q0,q2
    qwait 15
    rz q2, -0.806741
    qwait 7
    cnot q1,q2
    qwait 15
    rz q2, -0.764055
    qwait 7
    cnot q0,q2
    qwait 15
    { rz q2, -0.785398 | rz q0, 1.234435 }
    qwait 7
    { cnot q1,q2 | ry q0, -0.814217 }
    qwait 7
    rz q0, 3.055660
    qwait 7
    { rz q1, 0.785398 | cnot q2,q5 }
    qwait 7
    cnot q0,q1
    qwait 7
    cnot q5,q2
    qwait 7
    rz q1, 1.806353
    qwait 7
    { cnot q0,q1 | cnot q2,q5 }
    qwait 15
    { rz q0, -2.208546 | ry q1, 1.733418 }
    qwait 7
    ry q0, -1.024349
    qwait 7
    rz q0, 2.208546
    qwait 7
    cnot q0,q1
    qwait 15
    ry q1, 0.762379
    qwait 7
    cnot q0,q1
    qwait 15
    { rz q0, 3.141593 | rz q1, -1.570796 }
    qwait 7
    ry q0, -2.636759
    qwait 7
    rz q0, 1.570796
    qwait 7
    cnot q0,q1
    qwait 15
    rz q1, 1.570796
    qwait 7
    cnot q0,q1
    qwait 15
    { rz q0, 3.141593 | cnot q1,q4 }
    qwait 7
    ry q0, -1.392524
    qwait 7
    { rz q0, -3.141593 | cnot q4,q1 }
    qwait 7
    cnot q0,q3
    qwait 7
    cnot q1,q4
    qwait 7
    cnot q3,q0
    qwait 15
    cnot q0,q3
    qwait 15

