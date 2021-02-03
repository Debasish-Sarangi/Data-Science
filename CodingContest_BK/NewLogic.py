''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT

#import __pypy__


def main():
    SampleTestCases = int(input())
    counter = 1
    while (counter <= SampleTestCases and SampleTestCases > 0):

        NoOfTeamMembers = int(input().strip())
        GRevolutions =input().strip().split(" ")
        OpponentTeams = input().strip().split(" ")

        OpponentTeam = [int(numeric_string) for numeric_string in OpponentTeams]
        GRevolution = [int(numeric_string) for numeric_string in GRevolutions]

        GRevolution.sort(reverse=False)
        OpponentTeam.sort(reverse=False)

        count = 0
        cnt1=0
        cnt2=0

        while (cnt1 < NoOfTeamMembers and cnt2 < NoOfTeamMembers):
            try:
                if(GRevolution[cnt1]>OpponentTeam[cnt2]):
                    count=count+1
                    cnt1=cnt1+1
                    cnt2=cnt2+1
                else:
                    cnt1=cnt1+1
              
            except:
                pass

        counter = counter + 1
        print(count)



main()

