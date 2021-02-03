    SampleTestCases= int(input())
    counter=1
    while (counter <= SampleTestCases):

        NoOfTeamMembers = int(input())
        GRevolution  = input().split(" ")
        OpponentTeam = input().split(" ")
        GRevolution.sort(reverse=False)
        OpponentTeam.sort(reverse=False)

        calculation = 0

        i = 0

        while (i < len(GRevolution)):

            Glen=len(GRevolution)
            Olen=len(OpponentTeam)
            if(Glen>0 and Olen>0 ):
                j=0
                if(int(GRevolution[i])-int(OpponentTeam[i])>0):
                    calculation=calculation+1
                    GRevolution.pop(i)
                    OpponentTeam.pop(i)



                elif(int(GRevolution[i])-int(OpponentTeam[i])<=0):
                    while (j < Glen) :
                        if (int(GRevolution[j]) - int(OpponentTeam[i] )> 0):
                            calculation = calculation + 1
                            GRevolution.pop(j)
                            OpponentTeam.pop(i)

                            j=0
                            break
                        j=j+1

            if(Glen==len(GRevolution)):
                i=i+1

            else:
                i=0

        print(calculation)
    counter=counter+1

