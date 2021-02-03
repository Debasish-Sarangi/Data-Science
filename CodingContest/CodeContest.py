NoOfIngredients = int(input("first line of input consists of the number of ingredients, N"))
QtyOfEachIngredientReq = input(
    "The second line of input consists of the N space-separated integers representing the quantity of each ingredient required to create a Powerpuff Girl.")
QtyOfEachIngredientPre = input(
    "The third line of input consists of the N space-separated integers representing the quantity of each ingredient present in the laboratory.")

QtyOfEachIngredientRequired = QtyOfEachIngredientReq.split(" ")
QtyOfEachIngredientPresent = QtyOfEachIngredientPre.split(" ")

calculation = []

i = 0
while (i < NoOfIngredients):
    calculation.append(int(QtyOfEachIngredientPresent[i]) / int(QtyOfEachIngredientRequired[i]))
    i = i + 1

int(min(calculation))
