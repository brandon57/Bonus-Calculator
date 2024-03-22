import csv

class Person:
    def __init__(self, name: str, score):
        self.name = name
        self.score = score
        self.money = 0

if __name__ == "__main__":
    total_money = 5000
    people = []
    row_num = 0
    file = ""
    while True:
        print("input the file name:")
        file = input()
        try:
            open(file)
            break
        except:
            print("Couldn't open file")
    
    with open(file) as csvfile:
        csv_file = csv.reader(csvfile, delimiter=',')
        for row in csv_file:
            if row_num != 0:
                people.append(Person(row[0], int(row[1])))
            row_num += 1
    
    for x in range(len(people)):
        print(people[x].name + ", " + str(people[x].score))