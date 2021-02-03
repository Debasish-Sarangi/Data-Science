''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    SampleTestCases = int(input())
    counter = 1
    while (counter <= SampleTestCases and SampleTestCases > 0):

        NoOfTeamMembers = int(input())
        GRevolx = input().strip()
        Opponentx = input().strip()
        GRevolution = GRevolx.split(" ")[:NoOfTeamMembers]
        OpponentTeam = Opponentx.split(" ")[:NoOfTeamMembers]
        GRevolution.sort(reverse=False)
        OpponentTeam.sort(reverse=False)

        calculation = 0

        i = 0

        if(len(GRevolution)==len(OpponentTeam)==NoOfTeamMembers)   :


            while (i < len(GRevolution)):

                Glen = len(GRevolution)
                Olen = len(OpponentTeam)
                if (Glen > 0 and Olen > 0):
                    j = 0
                    if (float(GRevolution[i]) - float(OpponentTeam[i]) > 0):
                        calculation = calculation + 1
                        GRevolution.pop(i)
                        OpponentTeam.pop(i)



                    elif (float(GRevolution[i]) - float(OpponentTeam[i]) <= 0):
                        while (j < Glen):
                            if (float(GRevolution[j]) - float(OpponentTeam[i]) > 0):
                                calculation = calculation + 1
                                GRevolution.pop(j)
                                OpponentTeam.pop(i)

                                j = 0
                                break
                            j = j + 1

                if (Glen == len(GRevolution)):
                    i = i + 1

                else:
                    i = 0
            
        print(calculation)
        counter = counter + 1
    raise SystemExit

main()