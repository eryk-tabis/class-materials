heightInCm=float(input("Enter your height in cm: "))
heightInFeet=int(heightInCm/30.48)
heightInInch=int(round((heightInCm-heightInFeet*30.48)/2.54))
print("I am ",heightInCm,"cm tall, i.e. ",heightInFeet," feet and ", heightInInch," icnhes.")

#I am  166.0 cm tall, i.e.  5  feet and  5  icnhes.