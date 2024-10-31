
def decorator(func):
  def inner(*args, **kwargs):
    print(func.__annotations__)
    print(func(*args, **kwargs))
  return inner

@decorator
def test(a: int, b: int):
  return a + b

if __name__ == '__main__':
  test(1, 2)