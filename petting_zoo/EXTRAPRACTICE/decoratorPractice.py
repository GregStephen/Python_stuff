def kids(chore_func):
  def ammended_chore(*args, **kwargs):
    original_chore = chore_func(*args, **kwargs)
    return f"{original_chore} by the kids"
  return ammended_chore

def dad(chore_func):
  def ammended_chore(*args, **kwargs):
    original_chore = chore_func(*args, **kwargs)
    return f"{original_chore} by dad"
  return ammended_chore

@dad
def laundry():
  return "The dirty laundry was cleaned"

@kids
def garbage():
  return "The garbage was taken out"

def dust():
  return "The house was dusted"

def groom():
  return "The dog was brushed"


result = garbage()
print(result)
dads = laundry()
print(dads)



class Queries:
  def sort_by_name(sql_call):
    def sorted_by(*args, **kwargs):
      original_sql = sql_call(*args, **kwargs)
      return f"""{original_sql}\nORDER BY last_name ASC, first_name ASC"""
    return sorted_by

  @sort_by_name
  def customers(self):
      return "SELECT * FROM Customer"

  def coffins(self):
      return "SELECT * FROM Coffin"

  @sort_by_name
  def employees(self):
      return "SELECT * FROM Employee"

  def gravestones(self):
      return "SELECT * FROM GraveStones"

  @sort_by_name
  def deceased(self):
      return "SELECT * FROM Deceased"

  def obelisks(self):
      return "SELECT * FROM Obelisk"

  @sort_by_name
  def vendors(self):
      return "SELECT * FROM Vendor"

queries = Queries()

print(queries.customers())
print(queries.coffins())
print(queries.employees())