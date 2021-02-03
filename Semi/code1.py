def main():
    NoOfPatientDoc = input().strip().split(" ")
    NoOfPatients = int(NoOfPatientDoc[0])
    NoOfDoctors = int(NoOfPatientDoc[1])

    counter = 1
    DocEfforts = []
    RowEach = []

    while (counter <= NoOfDoctors):
        data = input().strip().split(" ")[:NoOfPatients]
        DocEfforts = [int(numeric_string) for numeric_string in data]
        RowEach.append(DocEfforts)
        counter = counter + 1

    sumofEach = []
    l1 = []
    l2 = []

    for row in RowEach:
        # sumofEach.append(min(row))
        # print(RowEach.index(row))

        c_index = RowEach.index(row)
        l1.append(sum(row[c_index:]))
        l2.append(sum(row[:c_index]))
    import numpy as np
    print(min(np.add(l1, l2)))

main()