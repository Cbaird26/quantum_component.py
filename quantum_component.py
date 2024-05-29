# quantum_component.py
import pennylane as qml
from pennylane import numpy as np

# Define a 2-qubit device
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def quantum_circuit(weights):
    qml.RX(weights[0], wires=0)
    qml.RY(weights[1], wires=1)
    qml.CNOT(wires=[0, 1])
    qml.RX(weights[2], wires=1)
    return qml.expval(qml.PauliZ(1))

def run_quantum_circuit():
    weights = np.array([0.1, 0.2, 0.3], requires_grad=True)
    return quantum_circuit(weights)
