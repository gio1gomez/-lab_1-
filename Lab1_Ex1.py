# Función para sumar n números
def add_numbers(*args):
    return sum(args)

# Función para invertir un número
def invert_number(number):
    return int(str(number)[::-1])

# Función para obtener detalles del usuario
def get_user_details():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    profession = input("Enter your profession: ")
    return f"Hello {name}, you are {age} years old and work as a {profession}."

# Función para obtener valores únicos
def get_unique_numbers():
    numbers = input("Enter numbers separated by spaces: ").split()
    unique_numbers = list(set(numbers))
    return unique_numbers

# Programa principal
if __name__ == "__main__":
    # Sumar números
    print("Sum of numbers:", add_numbers(1, 2, 3, 4, 5))

    # Invertir número
    print("Inverted number:", invert_number(619))

    # Obtener detalles del usuario
    print(get_user_details())

    # Obtener números únicos
    print("Unique numbers:", get_unique_numbers())

#fgfg
