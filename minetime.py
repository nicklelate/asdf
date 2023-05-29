import datetime

b = True
run = 1
while b:
    x = datetime.datetime.now()
    y = x.strftime("%M")
    if y[1] == "2":
        if run == 1:
            print(x)
            run = 0
    else:
        run = 1

print("hello world")