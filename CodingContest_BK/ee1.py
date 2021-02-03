''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    SampleTestCases = int(input())
    counter = 1
    while (counter <= SampleTestCases and SampleTestCases > 0):

        NoOfTeamMembers = int(input())
        GRevolution = " ".join(input().split()).strip().split(" ")[:NoOfTeamMembers]
        OpponentTeam = " ".join(input().split()).strip().split(" ")[:NoOfTeamMembers]

        calculation = []
        count = 0
        i = 0
        j = 0
        while (i < NoOfTeamMembers):

            while (j < len(GRevolution)):
                calculation.append(int(OpponentTeam[i]) - int(GRevolution[j]))
                j = j + 1

            try:

                m = max(k for k in calculation if k < 0)
                Indx = calculation.index(m)
                count = count + 1
                GRevolution.pop(Indx)
                calculation.clear()
            except:
                calculation.clear()

            i = i + 1
            j = 0

        print(count)
        counter = counter + 1


main()

