import csv

class Person:
    def __init__(self, name: str, score):
        self.name = name
        self.score = score
        self.money = 0

if __name__ == "__main__":
    total_money = 5000
    people = []
    no_bonus = []
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
                if(int(row[1]) > 2):
                    people.append(Person(row[0], int(row[1])))
                else:
                    no_bonus.append(Person(row[0], int(row[1])))
            row_num += 1
    
    print("These are the people who will get a bonus:")
    for x in people:
        print(x.name)
    
    print("\nThese are the people who will not get a bonus:")
    for x in no_bonus:
        print(x.name)