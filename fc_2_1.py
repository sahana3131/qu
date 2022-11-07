from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
from qiskit.tools.visualization import plot_histogram
import tkinter as tk

def main():
    qr=QuantumRegister(2)
    er=ClassicalRegister(2)
    circuit=QuantumCircuit(qr,er)
    circuit=QuantumCircuit(1,1)
    circuit.x(1)
    simulator=Aer.get_backend('unitary_simulator')
    result=execute(circuit,backend=simulator).result()
    unitary=result.get_unitary()
    circuit.draw(output='mpl')
    root2 = tk.Tk()
    root2.title("X")

    label = tk.Label(root2, text = str(unitary)).pack(padx=20, pady=20)
    plt.show()
    root2.mainloop()

if __name__=="main":
    main()


