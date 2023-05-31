sw = 1
op = 0
cantidad = 0
total = 0
totaln = 0
totalj = 0
totala = 0
contn = 0
contj = 0
conta = 0
vniño = 0
vjoven = 0
vadulto = 0
totaldia = 0
cdia = 0
totalf = 0

print("---------------Bienvenido a Cine Moro--------------")
while sw == 1:
   print("╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗")
   print("┃             OPCIONES CATEGORIA Y TARIFAS          ┃")
   print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
   print("┃      ENTRADA      ┃      COSTO     ┃     EDAD     ┃")
   print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
   print("┃      1.Niño       ┃      $5500     ┃    1 - 3     ┃")
   print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
   print("┃      2.Joven      ┃      $7000     ┃   14 - 21    ┃")
   print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
   print("┃      3.Adulto     ┃      $9000     ┃  Mayor a 22  ┃")
   print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
   print("┃      4.BOLETA PARA PAGAR                          ┃")
   print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
   print("┃      5.ANULAR LA COMPRA                           ┃")
   print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
   print("┃      6.FINALIZAR JORNADA                          ┃")
   print("╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝")

   try:
      op = int(input("Ingrese categoria de la entrada que desea comprar u alguna de las opciones: "))
      if op>0 and op<4:
         cantidad = int(input("Ingrese la cantidad de entradas que desea: "))
         if op == 1: 
           total = cantidad * 5500
           contn += cantidad
           totaln += total
           totaldia += total
           cdia += cantidad 
    
         if op == 2:
           total = cantidad * 7000
           contj += cantidad
           totalj += total
           totaldia += total
           cdia += cantidad 
      
         if op == 3:
           total = cantidad * 9000
           conta += cantidad
           totala += total
           totaldia += total
           cdia += cantidad 

      if op == 4:
          totalf = totaln+totalj+totala
          print(f"Aqui tiene su boleta para proceder al pago") 
          print(f"==================================================")
          print(f" Categoria | Cantidad | PrecioEntrada | SubTotal ")  
          print(f"==================================================")
          print(f" Niño      |    {contn}     |     5500      |   {totaln}  ")
          print(f" Joven     |    {contj}     |     7000      |   {totalj}   ")
          print(f" Adulto    |    {conta}     |     9000      |   {totala}   ")
          print(f"==================================================")
          print(f"            Total a Pagar             |   {totalf}   ")
          print(f"==================================================")
          print("   Gracias por su compra, disfrute la función!")


          sw = 1
          op = 0
          cantidad = 0
          total = 0
          totaln = 0
          totalj = 0
          totala = 0
          contn = 0
          contj = 0
          conta = 0
          vniño = 0
          vjoven = 0
          vadulto = 0
          totalf = 0

      if op == 5:
         sw = 1
         op = 0
         cantidad = 0
         total = 0
         totaln = 0
         totalj = 0
         totala = 0
         contn = 0
         contj = 0
         conta = 0
         vniño = 0
         vjoven = 0
         vadulto = 0
         totalf = 0

      if op == 6:
         por1=contn*100/cdia
         por2=contj*100/cdia
         por3=conta*100/cdia
         print("INGRESO DE HOY")
         print("=============================================")
         print(f"Cantidad Entradas Vendidas: {cdia}")
         print(f"Valor total vendido: {totaldia}")
         print(f"Porcentaje de Entradas Tipo Niño {int(por1)}%")
         print(f"Porcentaje de Entradas Tipo Joven {int(por2)}%")
         print(f"Porcentaje de Entradas Tipo Adulto {int(por3)}%")
         print("=============================================")

   except:
      print("Dato Invalido")


 