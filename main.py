sampleFormFlag = input("Do you want to see a sample form ? (Y/N) - ")
print("")
if sampleFormFlag == 'Y' or sampleFormFlag == 'y':
    print("------------HEALTH FORM------------".center(90))
    print("NAME :   FirstName LastName")
    print("AGE :    25")
    print("SEX :    M")
    print("COUNTRY CODE :   91")
    print("CONTACT NO. :    987654321")
    print("ADDRESS :    123 Main Street , New York , NY 10030")
    print("BLOOD PRESSURE (mm/hg) :    90/60")
    print("BREATHING (breaths/minute) :    15")
    print("PULSE (beats/minute) :    80")
    print("TEMPERATURE :    98 F or 36 C")
    print("-----------------------------------".center(90))

print("")
print("Enter your details -> ")
print("------------HEALTH FORM------------".center(90))

name = input("NAME :    ")
age = input("AGE :    ")
sex = input("SEX :    ")
countryCode = input("COUNTRY CODE :    ")
contactNumber = input("CONTACT NO. :    ")
address = input("ADDRESS :    ")
bloodPressure = input("BLOOD PRESSURE (mm/hg) :    ")
breathing = input("BREATHING (breaths/minute) :    ")
pulse = input("PULSE (beats/minute) :    ")
temperature = input("TEMPERATURE :    ")Y
print("-----------------------------------".center(90))

print("")
print("Enter your password to access full report")
print("The password format is FIRST NAME@CONTACT NO")
print("For eg - If your NAME is Abc Xyz and your CONTACT NO is 987654321 then your password is ABC@987654321")
print("")

actualPassword = name.split(" ")[0].upper() + '@' + contactNumber
count = 0
while count < 5:
    password = input("PASSWORD :    ")
    if actualPassword == password:
        break
    else:
        if count != 4:
            print("Wrong Password- Try again")
        count = count + 1

if count >= 5:
    print("Maximum password attempts is exceeded")
    print("")
    print("------------HEALTH REPORT------------".center(90))
    print("NAME :   " + name)
    print("AGE :    " + age)
    print("SEX :    ***")
    print("CONTACT DETAILS :    ***")
    print("ADDRESS :    ***")
else:
    print("")
    print("------------HEALTH REPORT------------".center(90))
    print("NAME :   " + name)
    print("AGE :    " + age)
    print("SEX :    " + sex)
    print("CONTACT DETAILS :    +" + countryCode + " " + contactNumber)
    print("ADDRESS :    " + address)

high = int(bloodPressure.split("/")[0])
low = int(bloodPressure.split("/")[1])
print("BLOOD PRESSURE (mm/hg) :    " + bloodPressure)
print("Normal blood pressure is 90/60 mm/hg to 120/80 mm/hg")
if high < 90 and low < 60:
    print("Your blood pressure is low")
elif high > 120 and low > 80:
    print("Your blood pressure is high")
elif 90 <= high <= 120 and 60 <= low <= 80:
    print("Your blood pressure is normal")
else:
    print("Your blood pressure is not normal")

print("BREATHING (breaths/minute) :    " + breathing)
print("Normal breathing rate is 12 to 18 breaths per minute ")
if 12 <= int(breathing) <= 18:
    print("Your breathing rate is normal")
elif int(breathing) < 12:
    print("Your breathing rate is low")
else:
    print("Your breathing rate is high")

print("PULSE (beats/minute) :    " + pulse)
print("Normal pulse is 60 to 100 beats per minute ")
if 60 <= int(pulse) <= 100:
    print("Your pulse is normal")
elif int(pulse) < 60:
    print("Your pulse is low")
else:
    print("Your pulse is high")

print("TEMPERATURE :    " + temperature)
if temperature.split(" ")[1] == 'C':
    value = (float(temperature.split(" ")[0]) * 1.8) + 32
else:
    value = float(temperature.split(" ")[0])
print("Normal body temperature is 97.8 F to 99.1 F or 36.5 C to 37.3 C")
if 97.8 <= value <= 99.1:
    print("Your body temperature is normal")
elif value < 97.8:
    print("Your body temperature is low")
else:
    print("Your body temperature is high")

print("-----------------------------------".center(90))