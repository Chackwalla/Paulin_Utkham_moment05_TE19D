def hello_world():
  print('Hallå, världen!')

def summa(tal1, tal2):
  return tal1 + tal2

def division(täljare, nämnare):
  return täljare / nämnare
  
def rektangel_area(sida1, sida2):
  if sida1 == sida2:
    area = sida1**2
    return area
  else:
    area = sida1 * sida2
    return area