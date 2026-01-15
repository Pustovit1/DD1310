class Inköpslista(list):
  """En klass som beskriver en inköpslista, ärver från klassen list"""
  
  def __str__(self):
    sträng = ""
    for vara in self:
      sträng += " * " + str(vara)  + "\n"
    return sträng
    
if __name__ == "__main__":
  lista = ["ägg", "mjölk", "vetemjöl"]
  print(lista)

inköpslista = Inköpslista(lista)
print(inköpslista)