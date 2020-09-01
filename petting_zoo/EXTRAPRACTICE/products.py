class Product:

  def __init__(self, serial_num):
    self.__serial_num = serial_num #setting privately scoped attribute on instantiation
 
  @property #the getter
  def serial_num(self):
    return self.__serial_num

  @serial_num.setter # The setter
  def serial_num(self, number):
    pass # here, we simply tell the function to do nothing, effectively preventing the setting of a value for .serial_num. Without the setter, though, an attempt to assign a value to foo.serial_num would throw an Attribute Error and break stuff.
    
  @property # the getter
  def price(self):
    try:
      return self.__price
    except AttributeError:
      return 0

  @price.setter # the setter
  def price(self, new_price):
    if type(new_price) is float:
      self.__price = new_proce
    else:
      raise TypeError('Please provide a floating point value for the price')