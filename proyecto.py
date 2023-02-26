import serial # importamos la librería serial para poder leer los datos enviados por el Arduino
import tkinter as tk # importamos la librería tkinter para crear una interfaz gráfica
import serial.tools.list_ports
import time

# establecemos una conexión serial con el puerto COM3 a una velocidad de 9600 baudios
ser = serial.Serial('COM5',9600,timeout=0.05)
time.sleep(1)

# creamos una ventana de tkinter
window = tk.Tk()

# agregamos una etiqueta a la ventana donde mostraremos el valor leído del potenciómetro
label = tk.Label(window, text="Valor del Potenciómetro: ")
label.pack()

# función que se ejecuta cada 1000 milisegundos para actualizar el valor mostrado en la etiqueta
def update_label():
    # leemos el valor enviado por el Arduino y lo convertimos a un string
    val = str(ser.readline().decode('ascii'))
    val2 = val.replace('\n','').replace('\r','')
    #Conversion
    decimal = 0
    binary = str(val2)
    for digit in binary:
        decimal = decimal*2 + int(digit)
    # actualizamos el texto de la etiqueta con el valor leído del potenciómetro
    label.config(text="Distancia recorrida: {} cm".format((decimal*7)/255))
    # programamos la función para que se ejecute nuevamente en 100 milisegundos
    window.after(1000, update_label)


# ejecutamos la función de actualización de la etiqueta por primera vez
update_label()

# hacemos que la ventana sea visible
window.mainloop()
