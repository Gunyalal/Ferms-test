#21?
import random

st = False
tc = 10
n = 10001
for i in range(0,tc):
  r = random.randint(1,n-1)
  if ((pow(r,n-1,n)!=1)):
    st = True
    break
if st:
  print("Число - составное")
else:
  print("Число, вероятно, простое")