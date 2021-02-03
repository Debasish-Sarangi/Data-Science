''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    
    SampleTestCases = int(input())
    counter = 1
    while (counter <= SampleTestCases and SampleTestCases > 0):

        NoOfTeamMembers = int(input())
        GRevolution = input().strip().split(" ")[:NoOfTeamMembers]
        OpponentTeam = input().strip().split(" ")[:NoOfTeamMembers]
        #GRevolution.sort(reverse=False)
        #OpponentTeam.sort(reverse=False)
        opLen=len(OpponentTeam)
        calculation = []
        count = 0
        i = 0
        j = 0
        while (i < NoOfTeamMembers):

            while (j < opLen ):
                calculation.append(float(GRevolution[i]) - float(OpponentTeam[j]))
                j = j + 1

            try:
                
                m = min(k for k in calculation if k > 0)
                Indx = calculation.index(m)
                count = count + 1
                OpponentTeam.pop(Indx)
                opLen=opLen-1
                calculation.clear()
            except:
                calculation.clear()

            i = i + 1
            j = 0

        print(count)
        counter = counter + 1
        GRevolution.clear()
        OpponentTeam.clear()
        calculation.clear()

main()

