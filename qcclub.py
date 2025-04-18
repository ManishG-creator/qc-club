from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)
qc.h(0)
qc.h(1)
qc.z(1)

backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
statevector = result.get_statevector()

print("Final statevector:")
print(statevector)
qc.draw('text')
