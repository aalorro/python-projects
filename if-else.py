var_a = "A"
var_b = "B"
var_c = "C"
var_d = "D"
var_f = "F"

score = int(input("What is your score?: "))

if score >= 90:
    print("Your grade is " + var_a)
else:
    if score >= 80 and score < 90:
        print("Your grade is " + var_b)
    else:
        if score >=70 and score < 80:
            print("your grade is " + var_c)
        else:
            if score >= 60 and score < 70:
                print("your grade is " + var_d)
            else:
                print("Your grade is " + var_f)




