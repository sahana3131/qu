from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
from qiskit.tools.visualization import plot_histogram

def main():
    qr=QuantumRegister(2)
    er=ClassicalRegister(2)
    circuit=QuantumCircuit(qr,er)
    plt.show()
    circuit.draw()
    circuit.h(qr[0])
    circuit.draw(output='mpl')
    circuit.measure(qr,er)
    circuit.draw(output='mpl')
    simulator=Aer.get_backend('qasm_simulator')
    result=execute(circuit,backend=simulator).result()

    plot_histogram(result.get_counts(circuit)) #h_gate
    plt.show()


if __name__ == "__main__":
    main()
