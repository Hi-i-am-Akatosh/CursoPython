import tkinter as tk

#Logica del aplicativo
#def convertir_temp():


ventana = tk.Tk()
ventana.title("Conversor de temperatura.")

ventana.geometry("520x480")
ventana.iconbitmap("temperatura.ico")

#Etiqueta
etiqueta_temp_celcius = tk.Label(text="Temperatura en °C:")
etiqueta_temp_celcius.place(x = 20, y = 20)
#Creacion label
caja_temp_celcius = tk.Entry()
caja_temp_celcius.place(x = 148, y = 28, width = 60)

#Boton de conversión
boton_convertir = tk.Button(text= "Convertir")
boton_convertir.place(x = 20, y = 20)




ventana.mainloop()