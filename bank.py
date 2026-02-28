# -*- coding: utf-8 -*-
import config
    
def validar_opcion(opcion):
    valor_retiro = 0
    
    if opcion not in config.posibles:
        print(
            """
            La opción que escogiste no existe
            """
        )
        return True
    
    if opcion == 1:
        print(
            f"""
            Su saldo actual es de ${config.saldo_inicial:,.2f}
            """
        )
        return True
    
    elif opcion == 2:
        valor_retiro = int(input(
            """
            ¿Cuanto desea retirar?: 
            """
        ))
        
        if valor_retiro < 0 \
            or valor_retiro > config.saldo_inicial:
            error()
            return True
            
        config.saldo_inicial -= valor_retiro
        
        print(
            f"""
            Saldo retirado con exito
            """
        )
        
        return True
        
    elif opcion == 3:
        valor_consignado = int(input(
            """
            ¿Cuanto desea consignar? 
            """
        ))
        
        if valor_consignado < 0:
            error()
            return True
        
        config.saldo_inicial += valor_consignado
                
        print(
            f"""
            Consignación exitosa. Su saldo actual es de ${config.saldo_inicial:,.2f}
            """
        )
        
        return True
    
    else:
        return False

def error():
    print(
        """
        Lo sentimos, esa opción no está registrada, 
        ingrese una opción válida
        """
    )

while True:
    try:
        opcion = int(input(
            """
            Bienvenido al cajero automatico ¿Qué transacción desea realizar?
            
            1. Consultar saldo
            2. Retirar dinero
            3. Consignar dinero
            4. Salir del menú de opciones
            
            >>>
            """
        ))
        
        respuesta = validar_opcion(opcion)

        if not respuesta:
            print(
            """
            Ejecución finalizada.
            """
            )
            break
        
        ask = int(input(
            """
            ¿Desea realizar otra transacción?
            1. Sí
            2. No
            """))
        
        if ask != 1:
            print(
            """
            Ejecución finalizada.
            """
            )
            break
            
    except Exception:
        error()