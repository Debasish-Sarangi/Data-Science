''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT

#import __pypy__


def main():
    testcases= int(input())
    counter = 1
    while (counter <= testcases and testcases > 0):
        Members = int(input().strip())
        GRev =input().strip().split(" ")
        Opp= input().strip().split(" ")
        OppTeam = [int(numeric_string) for numeric_string in Opp]
        GRevTeam = [int(numeric_string) for numeric_string in GRev]
        GRevTeam.sort(reverse=False)
        OppTeam.sort(reverse=False)
        count = 0
        count1=0
        count2=0
        while (count1 < Members and count2 < Members):
                if(GRevTeam[count1]>OppTeam[count2]):
                    count=count+1
                    count1=count1+1
                    count2=count2+1
                else:
                    count1=count1+1
        counter = counter + 1
        print(count)
main()

