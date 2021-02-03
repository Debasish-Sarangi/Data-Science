''' Read input from STDIN. Print your output to STDOUT '''
#Use input() to read input from STDIN and use print to write your output to STDOUT

#import __pypy__

def main():
    Ingredients = int(input())
    RQty = input().split(" ")
    PQty = input().split(" ")
    l = 0
    calculation=int(PQty[0]) / int(RQty[0])
    while (l < Ingredients):
        j=int(PQty[l]) / int(RQty[l])

        if(j<calculation):
            calculation=j
        l = l + 1
    print(int(calculation))
main()