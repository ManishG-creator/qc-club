from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply Hadamard gate to qubit 0
qc.h(0)

# Apply Hadamard gate to qubit 1
qc.h(1)

# Apply Z gate to qubit 1
qc.z(1)

# Display the circuit
print("Quantum Circuit:")
print(qc)

# Simulate the circuit to get the final statevector
backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()
statevector = result.get_statevector()

# Display the final statevector
print("\nFinal Statevector:")
print(statevector)
