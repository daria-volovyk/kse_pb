i=0
for i in range(10, 101, 5):
  print("Ціна без пдв:" + str(i) + "грн")
  i*=1.2
  print("з ПДВ:" + str(i) + "грн")