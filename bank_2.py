# -*- coding: utf-8 -*-
import config
    
def validar_opcion(opcion):
    valor_retiro = 0
    cuenta = config.cuenta
    
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
            Su saldo actual es de ${config.cuentas[cuenta]:,.2f}
            """
        )
        return True
    
    elif opcion == 2:
        try:
            valor_retiro = int(input(
                """
                ¿Cuanto desea retirar?: 
                """
            ))
        except ValueError:
            error()
            return True
            
        if valor_retiro < 0 or valor_retiro > config.cuentas[cuenta]:
            error()
            return True
            
        comision = 4/1000
        comision_retiro = valor_retiro  * comision
        total_retiro = valor_retiro + comision_retiro
        
        if total_retiro > config.cuentas[cuenta]:
            for account, balance in config.cuentas.items():
                if balance >= comision_retiro and account != cuenta:
                    cuenta_secundaria = account
                    break
                
            config.cuentas[cuenta] -= valor_retiro 
            config.cuentas[cuenta_secundaria] -= comision_retiro
        else:
            config.cuentas[cuenta] -= total_retiro  
        
        print(
            f"""
            Retiro exitoso
            Comosión aplicada: ${comision_retiro:,.2f}
            Saldo actual: ${config.cuentas[cuenta]:,.2f}
            """                             
        )

        return True
        
    elif opcion == 3:
        try:
            valor_consignado = int(input(
                """
                ¿Cuanto desea consignar? 
                """
            ))
        except ValueError:
            error()                              
            return True
        
        if valor_consignado <= 0:
            error()
            return True
        
        config.cuentas[cuenta] += valor_consignado
                
        print(
            f"""
            Consignación exitosa. 
            Su saldo actual es de ${config.cuentas[cuenta]:,.2f}
            """
        )
        
        return True

    elif opcion == 4:
        try:
            nueva_cuenta = int(input(
                """
                Ingrese el número de la cuenta:
                """
            ))
        except ValueError:
            error()
            return True
        
        if nueva_cuenta in config.cuentas:
            print("La cuenta ya existe.")
            return True
        
        config.cuentas[nueva_cuenta] = config.saldo_inicial
        
        print(
            f"""
            Se ha creado la cuenta con exito.
            """
        )
    
        return True
    
    # else:
    #     return False

def error():
    print(
        """
        Lo sentimos, esa opción no está registrada, 
        ingrese una opción válida
        """
    )

while True:
    try:        
        if len(config.cuentas) > 1:
            print(
                """
                Elige una cuenta:
                """
            )
           
            for key in config.cuentas.keys():
                print(
                    f"""
                    - {key}
                    """
                )
            
            while True:
                try:    
                    cuenta_escoger = int(input(
                        """
                        >>>
                        """
                    ))
                    
                    if cuenta_escoger not in config.cuentas:
                        print("La cuenta no existe. Intente nuevamente")
                        continue
                    
                    config.cuenta = cuenta_escoger
                    break
                
                except ValueError:
                    print("Debe ingresar un número válido.")
            
            
        elif len(config.cuentas) == 1 and not config.cuenta:
            config.cuenta = next(iter(config.cuentas))
        
        try:
            
            opcion = int(input(
                """
                Bienvenido al cajero automatico ¿Qué transacción desea realizar?
                
                1. Consultar saldo
                2. Retirar dinero
                3. Consignar dinero
                4. Agregar cuenta
                5. Salir del menú de opciones
                
                >>>
                """
            ))
        except ValueError:
            error()
            continue
        
        if opcion not in [4, 5] and not config.cuentas:
            print(
            """
            Primero debe crear una cuenta.
            """
            )
            continue
        
        respuesta = validar_opcion(opcion)
 
        if not respuesta:
            print(
            """
            Ejecución finalizada.
            """
            )
            break
        
        while True:
            try: 
                ask = int(input(
                    """
                    ¿Desea realizar otra transacción?
                    1. Sí
                    2. No
                    """))
                if ask not in [1,2]:
                    print("Inggrese solo 1 o 2.")
                    continue    
                break
            except ValueError:
                print("Ingrese un número válido.")
                
        
        if ask == 2:
            print(
            """
            Ejecución finalizada.
            """
            )
            break
            
    except Exception as e:
        print(e)
        error()