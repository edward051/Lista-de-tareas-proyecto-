import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../Controlador"))
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea
from Controlador_De_Tareas import Controlador_De_Tareas
from Vista_Creacion import Vista_Creacion

class Vista_Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Da Fare")
        self.setMinimumSize(400, 600)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        titulo = QLabel("DA FARE")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(titulo)

        barra = QHBoxLayout()
        self.busqueda = QLineEdit()
        self.busqueda.setPlaceholderText("🔍 Buscar...")
        self.btn_agregar = QPushButton("+")
        self.btn_agregar.setFixedSize(40, 40)
        barra.addWidget(self.busqueda)
        barra.addWidget(self.btn_agregar)
        layout.addLayout(barra)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        self.contenedor_tareas = QWidget()
        self.layout_tareas = QVBoxLayout(self.contenedor_tareas)
        self.layout_tareas.addStretch()
        scroll.setWidget(self.contenedor_tareas)
        layout.addWidget(scroll)

        self.controlador = Controlador_De_Tareas()
        self.btn_agregar.clicked.connect(self.abrir_creacion)

    def abrir_creacion(self):
        dialogo = Vista_Creacion(self.controlador, self)
        if dialogo.exec():
            self.refrescar_tareas()

    def refrescar_tareas(self):
        while self.layout_tareas.count() > 1:
            item = self.layout_tareas.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        for tarea in self.controlador.lista.LT:
            print(f"[DEBUG] ID:{tarea.ID} | T:{tarea.T} | DT:{tarea.DT} | FL:{tarea.FL} | FC:{tarea.FC} | E:{tarea.E} | SUBT:{tarea.SUBT}")
            texto = QLabel(f"{tarea.T}\n{tarea.DT}")
            self.layout_tareas.insertWidget(self.layout_tareas.count() - 1, texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Vista_Principal()
    ventana.show()
    sys.exit(app.exec())
