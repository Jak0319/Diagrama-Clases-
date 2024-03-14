class Colegio:
    def __init__(self, nombreC, colegioID, direccion, numero):
        self.nombreC = nombreC
        self.colegioID = colegioID
        self.direccion = direccion
        self.numero = numero
        self.estudiantes = []
        self.coordinador_programa = None
        self.programa_co = []

    def ingresar_nombre_colegio(self):
        self.nombreC = input("Ingrese el nombre del colegio: ")

    def agregar_id_colegio(self):
        self.colegioID = input("Ingrese el ID del colegio: ")

    def agregar_direccion(self):
        self.direccion = input("Ingrese la dirección del colegio: ")

    def agregar_numero_telefono(self):
        self.numero = input("Ingrese el número de teléfono del colegio: ")

    def mostrar_datos_colegio(self):
        print("\nDatos del colegio:")
        print("Nombre:", self.nombreC)
        print("ID:", self.colegioID)
        print("Dirección:", self.direccion)
        print("Número de Teléfono:", self.numero)

    def agregar_estudiante(self):
        estudiante = Estudiante()
        estudiante.submenu_datos_estudiante()
        self.estudiantes.append(estudiante)

    def mostrar_datos_coordinador(self):
        if self.coordinador_programa:
            self.coordinador_programa.mostrar_datos()
        else:
            print("No hay datos del coordinador del programa.")

    def mostrar_estudiantes(self):
        print("\nEstudiantes registrados:")
        for i, estudiante in enumerate(self.estudiantes):
            print(f"{i + 1}. {estudiante.nombre} {estudiante.apellidos}")

    def agregar_coordinador_programa(self):
        self.coordinador_programa = CoordinadorPrograma()

    def agregar_programa_co(self, programa):
        self.programa_co.append(programa)

    def mostrar_programa_co(self):
        if self.programa_co:
            print("\nPrograma del coordinador del programa:")
            for materia, cantidad_alumnos in self.programa_co:
                print(f"Materia: {materia}, Cantidad de Alumnos: {cantidad_alumnos}")
        else:
            print("No hay programa registrado.")

class Estudiante:
    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.correo = ""
        self.celular = ""
        self.nombre_apoderado = ""

    def agregar_nombre_apellidos(self):
        self.nombre = input("Ingrese el nombre del estudiante: ")
        self.apellidos = input("Ingrese los apellidos del estudiante: ")

    def agregar_correo(self):
        self.correo = input("Ingrese el correo del estudiante: ")

    def agregar_celular(self):
        self.celular = input("Ingrese el número de celular del estudiante: ")

    def agregar_nombre_apellidos_apoderado(self):
        self.nombre_apoderado = input("Ingrese el nombre y apellidos del apoderado: ")

    def mostrar_datos(self):
        print("\nDatos del estudiante:")
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("Correo:", self.correo)
        print("Celular:", self.celular)
        print("Nombre y apellidos del apoderado:", self.nombre_apoderado)

    def agregar_datos(self):
        self.agregar_nombre_apellidos()
        self.agregar_correo()
        self.agregar_celular()
        self.agregar_nombre_apellidos_apoderado()

    def submenu_datos_estudiante(self):
        opcion = 0
        while opcion != 6:
            print("\nMenú Estudiante:")
            print("1. Agregar nombre y apellido")
            print("2. Agregar correo")
            print("3. Agregar celular")
            print("4. Agregar nombre y apellido del apoderado")
            print("5. Mostrar datos")
            print("6. Volver al menú principal")

            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                self.agregar_nombre_apellidos()
            elif opcion == 2:
                self.agregar_correo()
            elif opcion == 3:
                self.agregar_celular()
            elif opcion == 4:
                self.agregar_nombre_apellidos_apoderado()
            elif opcion == 5:
                self.mostrar_datos()
            elif opcion == 6:
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

class CoordinadorPrograma:
    def __init__(self):
        self.nombre_apellido = ""
        self.correo = ""
        self.telefono = ""
        self.programa = []

    def agregar_nombre_apellido(self):
        self.nombre_apellido = input("Ingrese el nombre y apellido del coordinador de programa: ")

    def agregar_correo(self):
        self.correo = input("Ingrese el correo del coordinador de programa: ")

    def agregar_telefono(self):
        self.telefono = input("Ingrese el número de teléfono del coordinador de programa: ")

    def crear_programa(self):
        cant_materias = int(input("Ingrese la cantidad de materias: "))
        for _ in range(cant_materias):
            nombre_materia = input("Ingrese el nombre de la materia: ")
            cant_alumnos = int(input(f"Ingrese la cantidad de alumnos para {nombre_materia}: "))
            self.programa.append((nombre_materia, cant_alumnos))

    def ver_programa(self):
        if self.programa:
            print("\nPrograma del coordinador de programa:")
            for materia, cant_alumnos in self.programa:
                print(f"Materia: {materia}, Cantidad de Alumnos: {cant_alumnos}")
        else:
            print("No hay programa registrado.")

    def agregar_datos(self):
        self.agregar_nombre_apellido()
        self.agregar_correo()
        self.agregar_telefono()
        self.crear_programa()


def ejecutar_programa():
    opcion = 0
    colegio = Colegio("", "", "", "")

    while opcion != 5:
        print("\nMenú Principal:")
        print("1. Colegio")
        print("2. Estudiante")
        print("3. Coordinador Programa")
        print("4. Profesor_Docente")
        print("5. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            while True:
                print("\nMenú Colegio:")
                print("1. Ingresar Nombre Colegio")
                print("2. Agregar ID Colegio")
                print("3. Agregar Dirección")
                print("4. Agregar Número de Teléfono")
                print("5. Mostrar Datos Colegio")
                print("6. Mostrar Estudiantes")
                print("7. Volver al menú principal")

                opcion_colegio = int(input("Seleccione una opción: "))
                if opcion_colegio == 1:
                    colegio.ingresar_nombre_colegio()
                elif opcion_colegio == 2:
                    colegio.agregar_id_colegio()
                elif opcion_colegio == 3:
                    colegio.agregar_direccion()
                elif opcion_colegio == 4:
                    colegio.agregar_numero_telefono()
                elif opcion_colegio == 5:
                    colegio.mostrar_datos_colegio()
                elif opcion_colegio == 6:
                    colegio.mostrar_estudiantes()
                elif opcion_colegio == 7:
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")

        elif opcion == 2:
            colegio.agregar_estudiante()

        elif opcion == 3:
            colegio.agregar_coordinador_programa()
            while True:
                print("\nMenú Coordinador Programa:")
                print("1. Agregar Nombre y Apellido")
                print("2. Agregar Correo")
                print("3. Agregar Teléfono")
                print("4. Crear Programa")
                print("5. Ver Programa")
                print("6. Volver al menú principal")

                opcion_coordinador = int(input("Seleccione una opción: "))
                if opcion_coordinador == 1:
                    colegio.coordinador_programa.agregar_nombre_apellido()
                elif opcion_coordinador == 2:
                    colegio.coordinador_programa.agregar_correo()
                elif opcion_coordinador == 3:
                    colegio.coordinador_programa.agregar_telefono()
                elif opcion_coordinador == 4:
                    colegio.coordinador_programa.crear_programa()
                elif opcion_coordinador == 5:
                    colegio.coordinador_programa.ver_programa()
                elif opcion_coordinador == 6:
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")

        elif opcion == 4:
            while True:
                print("\nMenú Profesor_Docente:")
                print("1. Ingrese Nombre y Apellido Profesor")
                print("2. Ingrese Correo")
                print("3. Ingrese Celular")
                print("4. Ver Programa Materia")
                print("5. Ver Estudiante")
                print("6. Volver al menú principal")

                opcion_profesor = int(input("Seleccione una opción: "))
                if opcion_profesor == 1:
                    colegio.coordinador_programa.agregar_nombre_apellido()  # Agregar nombre y apellido del profesor
                elif opcion_profesor == 2:
                    colegio.coordinador_programa.agregar_correo()  # Agregar correo del profesor
                elif opcion_profesor == 3:
                    colegio.coordinador_programa.agregar_telefono()  # Agregar celular del profesor
                elif opcion_profesor == 4:
                    colegio.mostrar_programa_co()
                elif opcion_profesor == 5:
                    colegio.mostrar_estudiantes()
                elif opcion_profesor == 6:
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")

        elif opcion == 5:
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    ejecutar_programa()
