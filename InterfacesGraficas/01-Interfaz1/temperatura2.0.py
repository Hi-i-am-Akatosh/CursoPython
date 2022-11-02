#conversion de temperatura
import tkinter as tk 

#Logica del aplicativo
def convertir_temp():
  temp_celsius = float(caja_temp_celsius.get())
  temp_kelvin = temp_celsius + 273.15
  temp_fahrenheit = temp_celsius*1.8 + 32

  etiqueta_temp_kelvin.config(text=f"Temperatura en ºK: {temp_kelvin}")

  etiqueta_temp_fahrenheit.config(text=f"Temperatura en ºF: {temp_fahrenheit}")


ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.geometry("520x480")
ventana.iconbitmap("temperaturs.ico")

#etiqueta
etiqeuta_temp_celsius = tk.Label(text="Temperatura en ºC:")
etiqeuta_temp_celsius.place(x=20, y=20)

#creacion label
caja_temp_celsius = tk.Entry()
caja_temp_celsius.place(x=140, y=20, width=60)

#boton de conversion
boton_convertir = tk.Button(text="Convertir", command=convertir_temp)
boton_convertir.place(x=20, y=60)

#creacion de otra etiqueta
etiqueta_temp_kelvin = tk.Label(text="Temperatura en ºK: ")
etiqueta_temp_kelvin.place(x=20, y=120)

etiqueta_temp_fahrenheit = tk.Label(text="Temperatura en ºF:")
etiqueta_temp_fahrenheit.place(x=20, y=160)


ventana.mainloop()

