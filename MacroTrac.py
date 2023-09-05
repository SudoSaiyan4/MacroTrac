#This program will help you calculate your required daily macro-nutrient intake to achieve your fitness goals.

while True:
    input("\033[1;31m Let's learn a little about you. Press Enter to continue. \n \033[1;37m \n")

    gender = float(input("Gender(1=male/2=female): "))
    
    age = float(input("Age in years: "))
    print("Man, you are old! (just kidding)")
    
    height = float(input("Height in inches: "))
    
    cweight = float(input ("Current weight in lbs: "))
    
    activity = float(input("Weekly activity lvl(0=inactive, 1=1-3 days, 2=3-5 days, 3=5-7 days, 4=More than 7 times a week): "))

    gweight = float(input("Goal Weight in lbs: "))


    if gender == 1:
        bmr = 66.47 + 6.24 * cweight + 12.7 * height - 6.755 * age
    else :
        bmr = 655.1 + 4.35 * cweight + 4.7 * height - 4.7 * age

    float(bmr)

    if activity == 0:
        tdee = bmr * 1.1
    elif activity == 1:
        tdee = bmr * 1.27
    elif activity == 2:
        tdee = bmr * 1.38
    elif activity == 3:
        tdee = bmr * 1.62
    elif activity == 4:
        tdee = bmr * 1.75
    else :
        print("Error: Invalid entry")

    import math

    if cweight >= gweight:
        TDEE = math.floor(tdee)
    else :
        TDEE = math.ceil(tdee)
    float(TDEE)

    if gweight < cweight:
        GBDCI = TDEE - 500
    elif gweight > cweight:
        GBDCI = TDEE + 500
    else :
        GBDCI = TDEE

    float(GBDCI)

    protein_intake = float(input("Protein intake lvl: 0=Conservative, 1=Neutral, 2=Aggressive: \033[1;34m - Conservative daily intake is 0.8 grams per pound of your target body weight/Neutral intake is 1 gram per pound/Aggressive is 1.2 grams per pound. \n \033[1;37m \n"))
    if protein_intake == 0:
        proteincal = (gweight * .8) * 4
    elif protein_intake == 1:
        proteincal = gweight * 4
    elif protein_intake == 2:
        proteincal = (gweight * 1.2) * 4
    else :
        print("Error: Invalid entry")

    fat_intake = float(input("Fat intake lvl: 0=Light, 1=Neutral, 2=Moderate: \033[1;34m - Conservation daily intake is 0.3 grams per pound of your target body weight/Neutral is 0.35 grams per pound/Moderate is 0.4 grams per pound. \n \033[1;37m \n"))
    if fat_intake == 0:
        fatcal = (gweight * .3) * 9
    elif fat_intake == 1:
        fatcal = (gweight * .35) * 9
    elif fat_intake == 2:
        fatcal = (gweight * .4) * 9
    else :
        print("Error: Invalid entry")

    float(proteincal)
    float(fatcal)

    carbcal = GBDCI - proteincal - fatcal
    float(carbcal)

    protein_grams = proteincal / 4
    carb_grams = carbcal / 4
    fat_grams = fatcal / 9

    float(protein_grams)
    float(carb_grams)
    float(fat_grams)

    if gweight >= cweight:
        Protein = math.ceil(protein_grams)
    else :
        Protein = math.floor(protein_grams)

    if gweight >= cweight:
        Carbs = math.ceil(carb_grams)
    else :
        Carbs = math.floor(carb_grams)
    if gweight >= cweight:
        Fat = math.ceil(fat_grams)
    else :
        Fat = math.floor(fat_grams)
    float(Protein)
    float(Carbs)
    float(Fat)

    ProteinCals = Protein * 4
    CarbCals = Carbs * 4
    FatCals = Fat * 9

    float(ProteinCals)
    float(CarbCals)
    float(FatCals)

    Total_Calories = (ProteinCals + CarbCals + FatCals)
    float(Total_Calories)
    print()
    input("\033[1;31m Are you ready? Hit that enter button! \n")
    print()
    print()
    print ("\033[1;37m Your Personalized Goals are Here! \n")
    print()
    print("\033[1;35m Total Calories:", Total_Calories, "calories \n")
    print()
    print("\033[1;37m And for your Macro-Nutrient breakdown! \n")
    print()
    print("\033[1;34m Protein:", Protein,"g \n")
    print("\033[1;34m Carbohydrates:", Carbs,"g \n")
    print("\033[1;34m Fat:", Fat,"g \n")
    print()
    print("\033[1;37m Thank you for trying out my first program! \n")
    print()
    while True:
        answer = str(input('Run Again? \033[1;32m Yes? \n \033[1;31m No? \n \033[1;37m \n'))
        if answer in ('yes', 'no'):
            break
        print("Error: Invalid input.")
    if answer == 'yes':
        print("\033[1;32m YAY :) \n \033[1;37m \n")
        print()
        continue
    else :
        print("\033[1;31m Goodbye! \n")
        break
