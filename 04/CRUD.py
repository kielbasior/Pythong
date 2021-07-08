data_list = []
def menu():
    while True:
        print("1. Create new data\n2. Display data from database\n3. Update data\n4. Delete entry from database\n5. Count how many men and women are in the database")
        option = int(input("\nChoose an option: "))
        if option == 1:
            create()
        elif option == 2:
            read()
        elif option == 3:
            update()
        elif option == 4:
            delete()
        elif option == 5:
            people_per_gender()
        else:
            print("\nThere's no such an option")

def create():
    while True:
        option = int(input("1. Add data from file\n2. Add data from console\n3. Exit to menu \n\nChoose an option: "))
        if option == 1:
            file = open("data.txt", "r")
            line_count = 0
            for line in file:
                if line != "\n":
                    line_count += 1
            file.close()
            file = open("data.txt", "r")
            for x in range(line_count):
                line = file.readline().strip().split(";")
                for x in data_list:
                    if x[0] == line[0]:
                        print("The record of id: " + line[0] + " is already present in database.")
                        create()
                data_list.append(line)
            print(data_list)
        elif option == 2:
            inputdata = input("\nEnter your data separated with semicolons: ")
            line = inputdata.strip().split(";")
            data_list.append(line)
            print(data_list)
        elif option == 3:
            menu()

def read():
    for x in data_list:
        print(x)

def update():
    inputdata = input("\nEnter your data separated with semicolons: ")
    line = inputdata.strip().split(";")
    id = input("\nEnter id of record you want to update: ")
    for x in range(len(data_list)):
        if id in data_list[x][0]:
            data_list[x] = line
        elif x == len(data_list) and id not in data_list[x][0]:
            print("\n\nRecord of provided id hasn't been found.")
        else:
            print("Unexpected error. Try again")

def delete():
    id = input("Enter id of record you want to delete: ")
    for x in data_list:
        if id in x[0]:
            data_list.remove(x)
            print("\n\nThe record of id " + id + " has been deleted.")


def people_per_gender():
    woman = 0
    man = 0
    for x in data_list:
        if int(x[3][10]) % 2 == 0:
            woman += 1
        else:
            man += 1
    print("\n\nThe number of women in database: " + str(woman))
    print("The number of men in database: " + str(man))
