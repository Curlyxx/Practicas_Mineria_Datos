# #Crear un sistema para gestionar una biblioteca con las siguientes clases: Libro, Usuario, Biblioteca

# class Libro:

#     def __init__(self):
        
#         self.id = "12345"
#         self.titulo = "Supremacia Cuantica"
#         self.autor = "Michio Kaku"
#         self.publicacion = "2004"
#         self.disponible = False
    
#     #Metodos

#     def mostrarInformacion(self, id):
#         self.id = id
#         if self.id == "12345":
#             print(f"Titulo: {self.titulo}, Autor:  {self.autor}, Año: {self.publicacion}, Disponible: {self.disponible}")
#         else: 
#             print("El codigo no existe")
    
#     def prestarLibro(self, id):
#         self.id = id
#         if self.id == "12345":
#             if self.disponible:
#                 print("Libro disponible- El libro se puede prestar")
#                 self.disponible = False
#             else: 
#                 print("Libro no disponible")
        
#     def devolverLibro(self,id):
#         self.id = id
#         if self.id == "12345":
#             if self.disponible:
#                 print("El libro ya esta prestado")
#                 self.disponible = False
#             else:
#                 print("Libro devuelto")
    
