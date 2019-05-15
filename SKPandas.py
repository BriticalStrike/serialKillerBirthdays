import pandas as pd

csv_input=pd.read_csv("DataFiles\SKBdays.csv", names = ["Name", "Birthday"])

sign = []
for row in csv_input["Birthday"]:
    newlist = row.split()
    if newlist[1] == "January":
        sign.append("Capricorn") if (int(newlist[0])<=19) else sign.append("Aquarius")
    elif newlist[1] == "February":
        sign.append("Aquarius") if (int(newlist[0])<=18) else sign.append("Pisces")
    elif newlist[1] == "March":
        sign.append("Pisces") if (int(newlist[0])<=20) else sign.append("Aries")
    elif newlist[1] == "April":
        sign.append("Aries") if (int(newlist[0])<=19) else sign.append("Taurus")
    elif newlist[1] == "May":
        sign.append("Taurus") if (int(newlist[0])<=20) else sign.append("Gemini")
    elif newlist[1] == "June":
        sign.append("Gemini") if (int(newlist[0])<=20) else sign.append("Cancer")
    elif newlist[1] == "July":
        sign.append("Cancer") if (int(newlist[0])<=22) else sign.append("Leo")
    elif newlist[1] == "August":
        sign.append("Leo") if (int(newlist[0])<=22) else sign.append("Virgo")
    elif newlist[1] == "September":
        sign.append("Virgo") if (int(newlist[0])<=22) else sign.append("Libra")
    elif newlist[1] == "October":
        sign.append("Libra") if (int(newlist[0])<=22) else sign.append("Scorpio")
    elif newlist[1] == "November":
        sign.append("Scorpio") if (int(newlist[0])<=21) else sign.append("Sagittarius")
    elif newlist[1] == "December":
        sign.append("Sagittarius") if (int(newlist[0])<=21) else sign.append("Capricorn")

csv_input["Sign"] = sign

csv_input.to_csv('DataFiles\SKSigns.csv')

