print('Сейчас мы посмотрим все твои сбережения, а также и оценим твое финансовое состояние')
karta=int(input('Сколько денег у тебя на дебетовой карте?'))
nal=int(input('Если есть наличка, то напиши, сколько?'))
kopilka=int(input('Сколько денег у тебя в копилке?'))
vsego=karta+nal+kopilka
minimum=20000
print(minimum,'это тот минимум, который должен быть у тебя')
print('Ну а у тебя',vsego,'рублей')
if vsego>20000:
    print('Поздравляю,ты можешь позволить себе больше, чем 50% людей')
else:
    print("Работай, пролетариат")
