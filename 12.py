age = int(input('Напиши свой возраст, чтобы понять, как ты можешь пить водку'))
if(age >= 18):
    print ("Поздравляю, теперь ты можешь покупать себе водку")
elif (age >= 21) and (age <=24):
    print ("Для того, чтобы пить один - ты пока не дорос")
else:
    print ('К сожалению,покупать водочку ты пока не можешь')
