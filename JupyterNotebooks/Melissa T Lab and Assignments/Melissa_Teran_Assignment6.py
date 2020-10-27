def leap_year(year):
# check if year is divisible by 4 then it is leap year
    if year % 4 == 0:
        print ("Is a Leap Year")
    # check if year is divisible by 100
    if year % 100 == 0:
        print ("Not a Leap Year")
        # check if year is divisble by 400
        if year % 400 == 0:
            print ("Is a Leap Year")
if __name__ == "__main__":
    years = [2000, 1994, 1912, 3002, 1700, 1400]
    answers = []
    for year in years:
        answers.append(leap_year(year))
    
    print(answers)