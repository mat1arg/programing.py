from abc import abstractclassmethod, abstractmethod
from ast import Expression
from distutils.log import error
from multiprocessing.sharedctypes import Value
import queue
from sqlite3 import DateFromTicks
from tkinter import *
from turtle import clear
from types import BuiltinFunctionType
from typing_extensions import Self
from wsgiref.validate import validator
from setuptools import Command

root = Tk()
root.litle("calculadora")

display = Entry(root)
display.grid(row= 1, columnspan= 6, sticky= W+E)

i = 0

def get_numbers(n):
    global i
    display.insert(i,n)
    i+=1

def get_operation(operator):
    global i
    operator_length=len(operator)
    display.insert(i,operator)
    i+=operator_length

def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len (display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, 'Error')

def calculate():
    display_state = display_get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display() 
        display.insert(0, result)
    except expression as identifier:
        clear_display()
        display.insert('error')



# numeric Buttons

Button(root, text="1",command=lambda:get_numbers(1)).grid(row=2, column=0,sticky= W+E)
Button(root, text="2",command=lambda:get_numbers(2)).grid(row=2, column=1,sticky= W+E)
Button(root, text="3",command=lambda:get_numbers(3)).grid(row=2, column=2,sticky= W+E)

Button(root, text="4",command=lambda:get_numbers(4)).grid(row=3, column=0,sticky= W+E)
Button(root, text="5",command=lambda:get_numbers(5)).grid(row=3, column=1,sticky= W+E)
Button(root, text="6",command=lambda:get_numbers(6)).grid(row=3, column=2,sticky= W+E)

Button(root, text="7",command=lambda:get_numbers(7)).grid(row=4, column=0,sticky= W+E)
Button(root, text="8",command=lambda:get_numbers(8)).grid(row=4, column=1,sticky= W+E)
Button(root, text="9",command=lambda:get_numbers(9)).grid(row=4, column=2,sticky= W+E)

 #buttons part2

Button(root, text="AC").grid(row=5, column=0,sticky= W+E)
Button(root, text="0",command=lambda:get_numbers(0).grid(row=5, column=1,sticky= W+E)
Button(root, text="%").grid(row=5, column=2,sticky= W+E)

Button(root, text="+",command=lambda:get_operation("+")).grid(row=2, column=3,sticky= W+E)
Button(root, text="-",command=lambda:get_operation("-")).grid(row=3, column=3,sticky= W+E)
Button(root, text="*",command=lambda:get_operation("*")).grid(row=4, column=3,sticky= W+E)
Button(root, text="/",command=lambda:get_operation("/")).grid(row=5, column=3,sticky= W+E)

Button(root, text="→", command=lambda: undo()).grid(row=2, column=4,sticky= W+E, columnspan=2)
Button(root, text="exp", command=lambda:get_operation("**")).grid(row=3, column=4,sticky= W+E)
Button(root, text="^2", command=lambda:get_operation("**2")).grid(row=3, column=5,sticky= W+E)
Button(root, text="(", command=lambda:get_operation("(")).grid(row=4, column=4,sticky= W+E)
Button(root, text=")", command=lambda:get_operation(")")).grid(row=4, column=5,sticky= W+E)
Button(root, text="=",command=lambda:calculate()).grid(row=5, column=4,sticky= W+E, columnspan=2)

class calculadora:
    Value = "calculadora"
    def compare(self, calculadora)
      if calculadora.value > Self.Value:
          return calculadora.Value
          return self.Value
          print(calculadora.Value)

class moneda:
    Value = "moneda"
    def compare(self, moneda):
        if moneda Value > self.Value
         return moneda.Value
        return self Value
        print("moneda.Value")

class bitcoin:
    value = "bitcoin"
    def compare(self,bitcoin)
    if bitcoin Value > self.Value
    return bitcoin.Value
    return self.Value
    print("bitcoin.Value")

class dolares:
    value = "dolares"
    def compare(self,dolares)
    if dolares Value > self.Value
    return dolares.Value
    return self.Value
    print("dolares.Value")

class pesos:
    value = "pesos"
    def compare(self,Value)
    if pesos Value > self.Value
    return pesos.Value
    return self.Value
    print("pesos.Value")

from abc import ABC, abstractmethod
 
 #clase abstracta :
 class EstructuraAbstracta(ABC)

 @abstractmethod
 def obtener():
     pass

class hash (EstructuraAbstracta):
    monedas = {}

class queue:
    monedas = {}

def obtener(self, candtidad)
    monedas {0}

def agregar (self,bitcoin):
    bitcoin[len((cantidad)-1)] valor 

class Bitcoin:

    def__init__(self,cantidad_bitcoin)
    if not insistance(cantidad_bitcoin, EstructuraAbstracta):
    raise ValueError ('valor incorrecto del pasaje de moneda')

self.monedas = cantidad_monedas

def cantidad_monedas(self):
    #implementacion
return monedas_obtener

def calcular_monedas(self,cantidad,monedas):
    self cantidad.agregar(cantidad,monedas)

bitcoin(Queue([]))

from abc import ABC, abstractmethod
 
 #clase abstracta :
 class EstructuraAbstracta(ABC)

 @abstractmethod
 def obtener():
     pass

class hash (EstructuraAbstracta):
    pesos = {}

class queue:
    pesos = {}

def obtener(self, candtidad)
    pesos {0}

def agregar (self,pesos):
    pesos[len((valor)-1)] valor 

class dolares:

    def__init__(self,valor_pesos)
    if not insistance(valor_pesos, EstructuraAbstracta):
    raise ValueError ('valor incorrecto del pasaje de dolares')

self.pesos = valor_pesos

def pesos_dolares(self):
    #implementacion
return valor_obtener

def obtener_pesos(self,pesos,dolares):
    self pesos.agregar(dolares,pesos)

pesos(Queue([]))


for dolorares in [0,10000]
    contador [0,10000]
    print(dolares)

for bitcoint in [0,10000]
    contador[0,10000]
    print(bitcoin)
   


 root.mainloop()

   
   







