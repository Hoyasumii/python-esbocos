from typing import Callable, Type, TypeVar, Union, Any, Dict

T = TypeVar("T")

def typed_prop(name: str, prop_type: Type[T], default: Union[T, Any]=None, validator: Callable[[int], bool]=None):

  assert isinstance(name, str), "Name must be a string"
  assert isinstance(prop_type, type), "Type must be a type"

  def decorator(cls):

    def getter(self):
      return getattr(self, f"_{name}", default)
    
    def setter(self, value):

      if not isinstance(value, prop_type):
        raise ValueError(f"Value must be a {prop_type.__name__}")
      
      if validator and not validator(value):
        raise ValueError(f"Validation failed for value: {value}")
      
      setattr(self, f"_{name}", value)

    def deleter(self):
      delattr(self, f"_{name}")

    setattr(cls, name, property(getter, setter, deleter))
    return cls
  
  return decorator

# def typed_method(**data: Dict[str, Any]) -> T:
#   pass

@typed_prop("name", str, "Alberto")
@typed_prop("age", int, 0, validator=lambda age: 0 < age < 100)
class MyClass:

  def __init__(self):
    print(dir(self))
    # print(self.name)
    # self.name = "Alan"
    # print(self.name)
    # print(self.age)
    # self.age = 1
    print(self.age)

if __name__=="__main__":
  MyClass()