class Meta(type):
  def __new__(meta, name, bases, class_dict: dict): #, name, bases, class_dict
    # TODO: E se o Meta tivesse args? Como seria a implementação?

    # name = "Testando"
    print(f"Creating Type {name} with bases {bases} and class_dict {class_dict}")
    # class_dict.update({ "new_prop": True })

    # print(dir(meta))

    return super().__new__(meta, name, bases, class_dict)
  

class MyClass(metaclass=Meta):
  def __new__(cls):
    print("Creating instance")
    print(cls.__annotations__)
    return super().__new__(cls)

  def __init__(self):
    # print(self, dir(self))
    print("Instance initialized")

  def __call__(self):
    print("Instance called")

if __name__ == '__main__':
  x=MyClass()
  # y=MyClass.__new__(MyClass)
  print(x, type(x), isinstance(type(x), Meta))
  # print(dir(type(int)))
  # print(y, type(y))
  # x()
