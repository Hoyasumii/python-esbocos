class MyClass:
  def __init__(self, number):
    self.value = number

  def __iadd__(self, value):
    return self.value + (value*2)

  def __add__(self, value):
    print("__add__")
    return MyClass(self.value * 3)
  
  def __mul__(self, value):
    print("__mul__")
    return MyClass(self.value * 20)
  
  def __str__(self):
    return f"{self.value}"
  
if __name__=="__main__":
  n = MyClass(1)
  print(n)
  n += 2
  print(n)
  # print(n + 10)
  # print(f"{n!s}")
  # n += 2
  # print(f"{n!s}")
  # print(f"{n + 3}")
  # print(n * 2)