score = input("Enter Score: ")
score1 = float(score)
if score1>=0.9 :
    print('A')
elif score1<0.9 and score1>=0.8 :
    print('B')
elif score1<0.8 and score1>=0.7 :
    print('C')
elif score1<0.7 and score1>=0.6 :
    print('D')
elif score1<0.6 :
    print('F') 
else:
    print('ERROR')
