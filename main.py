from time import sleep
sleep(2)
print("Astronaut: 'Mission control, are we set?'") ; sleep(3)
print("Mission Control: 'Yes.'") ; sleep(2)
print("Austronaut: 'Alright, here we go.'") ; sleep(2)
print("Mission control: '")
count = 10
while count > 0:
  print(count)
  count = count - 1 ; sleep(1)
print ("BLAST OFF!!'") ; sleep(1)
print("*rocket noises*")