''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT

import __pypy__


def main():
    SampleTestCases = int(input())
    counter = 1
    while (counter <= SampleTestCases and SampleTestCases > 0):

        NoOfTeamMembers = int(input().strip())
        GRevolution = input().strip().split(" ")
        OpponentTeam = input().strip().split(" ")

        calculation = []
        count = 0

        for i in range(NoOfTeamMembers):
            try:
                for s in OpponentTeam:
                    calculation.append(int(GRevolution[i]) - int(s))
                m = min(k for k in calculation if k > 0)
                Indx = calculation.index(m)
                count = count + 1
                OpponentTeam.pop(Indx)
                calculation.clear()
            except:
                calculation.clear()

        counter = counter + 1
        print(count)



main()
