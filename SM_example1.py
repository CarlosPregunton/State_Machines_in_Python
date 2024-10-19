from transitions import Machine

# Definir las funciones de callback que actuarán como entradas
def on_enter_state1(event):
    print("Entrando en el estado 1")
    # Acceder a los parámetros pasados a través de event
    print(f"Parámetros recibidos: {event.kwargs}")

def on_exit_state1(event):
    print("Saliendo del estado 1")
    print(f"Parámetros enviados: {event.kwargs}")

def on_enter_state2(event):
    print("Entrando en el estado 2")
    print(f"Parámetros recibidos: {event.kwargs}")

def on_exit_state2(event):
    print("Saliendo del estado 2")
    print(f"Parámetros enviados: {event.kwargs}")

# Definir los estados y eventos
states = ['state1', 'state2']
transitions = [
    {'trigger': 'go_to_state2', 'source': 'state1', 'dest': 'state2',
     'before': 'on_exit_state1', 'after': 'on_enter_state2'},
    {'trigger': 'go_to_state1', 'source': 'state2', 'dest': 'state1',
     'before': 'on_exit_state2', 'after': 'on_enter_state1'},
]

# Crear la máquina de estados
# Parameters:
# send_event: Allows to pass EventData to callbacks.
machine = Machine(states=states, transitions=transitions, initial='state1', send_event=True)

# Añadir callbacks a la instancia de la máquina directamente
machine.on_enter_state1 = on_enter_state1
machine.on_exit_state1 = on_exit_state1
machine.on_enter_state2 = on_enter_state2
machine.on_exit_state2 = on_exit_state2

# Probar las transiciones pasando parámetros
print(f"Estado inicial: {machine.state}")

# Pasar un parámetro adicional al ejecutar la transición
machine.go_to_state2(param1="valor1", param2=123)
print(f"Estado actual: {machine.state}")

machine.go_to_state1(param1="otro_valor", param2=456)
print(f"Estado actual: {machine.state}")
