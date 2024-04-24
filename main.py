#main que se corre en thonny
from random import randint
#debe tener comprobacion de goles, sonidos, led que indiquen las paletas

sistema_de_palas=[[1,2],[3,4],[5,6]]
sistema_de_palas_escogido=0
sistema_de_palas_escogido=randint(0,2)
while True:
      
      print(sistema_de_palas[sistema_de_palas_escogido])
