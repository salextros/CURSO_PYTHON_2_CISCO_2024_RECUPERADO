stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())

############################################################################################

class Stack:  # Definiendo la clase Stack.
    def __init__(self):  # Definiendo la función del constructor.
        print("¡Hola!")


stack_object = Stack()  # Instanciando el objeto.

##############################################################################################

# class Stack:
#     def __init__(self):
#         self.stack_list = []


# stack_object = Stack()
# print(len(stack_object.stack_list))

# class Stack:
#     def __init__(self):
#         self.__stack_list = []


# stack_object = Stack()
# print(len(stack_object.__stack_list))

################################################################################################

class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
    
stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
print()
print()

###################################################################################

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object_1 = Stack()
stack_object_2 = Stack()

stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop())

print(stack_object_2.pop())
print()
print()

#################################################################################

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()

little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)

print(funny_stack.pop())
print()
print()

###############################################################################################

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

##########################################################################################

class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val  # Actualiza la suma acumulada
        super().push(val)  # Llama al método push de la clase base

    def pop(self):
        val = super().pop()  # Llama al método pop de la clase base
        self.__sum -= val  # Actualiza la suma acumulada
        return val

    def get_sum(self):
        return self.__sum


# Ejemplo de uso
stack = AddingStack()
stack.push(5)
stack.push(10)
stack.push(20)
print("Suma acumulada:", stack.get_sum())  # Salida esperada: Suma acumulada: 35
print()
print()

##################################################################################################

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
print()
print()

##################################################################################################

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val
 
    def set_second(self, val):
        self.second = val
 
 
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
 
example_object_2.set_second(3)
 
example_object_3 = ExampleClass(4)
example_object_3.third = 5
 
print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
 
print()
print()

########################################################################################################
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5


print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
print()
print()

########################################################################################################

print(example_object_1._ExampleClass__first)
print()
print()

#########################################################################################################

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)
print()
print()

##########################################################################################################

class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)
print()
print()

##########################################################################################################

class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)
print()
print()
##########################################################################################################

# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1


# example_object = ExampleClass(1)

# print(example_object.a)
# print(example_object.b)
# print()
# print()

############################################################################################################

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

try:
    print(example_object.b)
except AttributeError:
    pass

print()
print()

############################################################################################################

class ExampleClass:
    attr = 1

print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))
print()
print()

class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))



    



