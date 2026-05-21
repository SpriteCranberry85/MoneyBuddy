running = True

print("Welcome to MoneyBuddy!")
print("Here is a list of things I can do! Just enter the associated number to begin!")

while (running == True):

    inputChoice = input("Calculate Yearly Income: Enter 1\nCalculate Yearly Expenses: Enter 2\nCalculate time to earn certain dollar amount: Enter 3\nMake monthly summary table: Enter 4\nQuit: Enter 5\n")

    if (inputChoice == "1"):

      choice = input("Enter 1 for hourly wage or 2 for estimated weekly income:\n")

      if (choice == "1"):

        wageAmount = float(input("Enter your hourly wage: "))
        hoursPerWeek = float(input("Enter the average hours a week you work: "))
        print("Your estimated yearly income is " + str(wageAmount * hoursPerWeek * 52) + " dollars.")
     
      if (choice == "2"):

        weeklyIncome = float(input("Enter your estimated weekly income: "))
        print("Your estimated yearly income is " + str(weeklyIncome * 52) + " dollars.")
    
    if (inputChoice == "2"):

        housingCosts = float(input("Enter monthly rent/mortgage + utilities and insurance: "))
        transportation = float(input("Enter monthly transportation costs: "))
        food = float(input("Enter monthly food costs: "))
        medical = float(input("Enter monthly medical costs: "))
        entertainment = float(input("Enter monthly entertainment costs: "))
        otherExpenses = float(input("Enter any other monthly expenses: "))
        totalExpenses = (housingCosts + transportation + food + medical + entertainment + otherExpenses) * 12
        print("Your estimated yearly expenses are " + str(totalExpenses) + " dollars.")

    if (inputChoice == "3"):
    
        dollarAmount = float(input("Enter desired dollar amount: "))
        choice = input("Enter 1 for hourly wage or 2 for estimated weekly income:\n ")

        if (choice == "1"):

            wageAmount = float(input("Enter your hourly wage: "))
            hoursPerWeek = float(input("Enter the average hours a week you work: "))
            timeInWeeks = float(dollarAmount/(wageAmount * hoursPerWeek))
            print("It will take " + str(timeInWeeks) + " weeks to earn " + str(dollarAmount) + " dollars.")

        if (choice == "2"):

            weeklyIncome = float(input("Enter your estimated weekly income: "))
            timeInWeeks = float(dollarAmount / weeklyIncome)
            print("It will take " + str(timeInWeeks) + " weeks to earn " + str(dollarAmount) + " dollars.")
     

    if (inputChoice == "4"):

        monthlyIncome = float(input("Enter monthly income: "))
        housingCosts = float(input("Enter monthly rent/mortgage + utilities and insurance: "))
        transportation = float(input("Enter monthly transportation costs: "))
        food = float(input("Enter monthly food costs: "))
        medical = float(input("Enter monthly medical costs: "))
        entertainment = float(input("Enter monthly entertainment costs: "))
        otherExpenses = float(input("Enter any other monthly expenses: "))
        monthlyExpenses = housingCosts + transportation + food + medical + entertainment + otherExpenses
        difference = monthlyIncome - monthlyExpenses
        fileName = input("Enter the name of the file to create: \n")
        #Writing to file
        
        with open(fileName, "w") as f:
            f.write("<!DOCTYPE html>\n")
            f.write("<html>\n")
            f.write("<style>\n")
            f.write("table, th, td {\n")
            f.write("  border:1px solid black;\n")
            f.write("}\n")
            f.write("</style>\n")
            f.write("<body>\n")
            f.write("<h2>Monthly Financial Summary</h2>\n")
            f.write('<table style="width:100%">\n')
            f.write("  <tr>\n")
            f.write("    <<th>MonthlyIncome</th>\n")
            f.write("    <<th>Housing</th>\n")
            f.write("    <<th>Transportation</th>\n")
            f.write("    <<th>Food</th>\n")
            f.write("    <<th>Medical</th>\n")
            f.write("    <<th>Entertainment</th>\n")
            f.write("    <<th>OtherExpenses</th>\n")
            f.write("    <<th>MonthlyExpenses</th>\n")
            f.write("    <<th>Difference</th>\n")
            f.write("  </tr>\n")
            f.write("  <tr>\n") 
            f.write("    <td>" + str(monthlyIncome) + "</td>\n")
            f.write("    <td>" + str(housingCosts) + "</td>\n")
            f.write("    <td>" + str(transportation) + "</td>\n")
            f.write("    <td>" + str(food) + "</td>\n")
            f.write("    <td>" + str(medical) + "</td>\n")
            f.write("    <td>" + str(entertainment) + "</td>\n")
            f.write("    <td>" + str(otherExpenses) + "</td>\n")
            f.write("    <td>" + str(monthlyExpenses) + "</td>\n")
            f.write("    <td>" + str(difference) + "</td>\n")
            f.write("  </tr>\n")
            f.write("</table>\n")
            f.write("</body>\n")
            f.write("</html>\n")
  
        print("File has been written successfully!. Run as HTML program to see table.")
            
    if (inputChoice == "5"):

        print("Thanks for using MoneyBuddy!")
        running = False



