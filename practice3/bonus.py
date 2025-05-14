total_sum=0
while True:
  a=float(input("Введіть ваш місячний дохід або '0' до виходу"))
  if(a>0):
    total_sum+=a
    print("Ваш дохід збережено: ..." + str(total_sum))
  elif(a<0):
    print("Дохід не може бути від’ємним")
    continue
  else:
    break;