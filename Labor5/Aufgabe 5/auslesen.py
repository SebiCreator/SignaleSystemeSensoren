import redlab as rl

read = rl.cbAIn(0,0,1)
print(read)
messreihe = rl.cbAInScan(0,0,0,300,8000,1)
print(messreihe)
readSpannung = rl.cbVIn(0,0,1)
messreiheSpannung = rl.cbVInScan(0,0,0,300,8000,1)
print(readSpannung)
print(messreiheSpannung)


vout = rl.cbVOut(0,0,101, input())