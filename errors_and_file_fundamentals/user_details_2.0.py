# %%
import csv # import csv package

# with open('user_details.csv', 'r') as csv_file: # opens the user details csv file in reading mode 'r'.
#     csv_read = csv.reader(csv_file, delimiter=',') # creates a variable that represents reading the file, with the data seperated by ','.
#     with open('new_details.csv', 'w', newline='') as csv_new_file: # creates a new csv file with name parsed in in write mode 'w'.
#         csv_write = csv.writer(csv_new_file, delimiter=',') # creates a variable that represents the ability to write to the file.
#         for lines in csv_read: # for loop that iterates through each row in the file, where 'lines' represents each row of information.
#             username = lines[4].split('@')[0] # cleaning the email column, splitting at '@' to get everything in front of it.
#             row = [lines[1], lines[2], username] # combines the individual columns into a list.
#             csv_write.writerow(row) # writes each row to the new file.

class CSV_Cleaner:
    def __init__(self) -> None:
        pass

    def open_file(self, file1):
        with open(file1, 'r') as csv_file:
            csv_r = csv.reader(csv_file, delimiter=',')
            details = []
            for lines in csv_r:
                details.append(lines)
            return details

    def write_file(self, file1, file2='untitled.csv'):
        new_data = self.add_info(file1)
        with open(file2, 'w', newline='') as csv_write:
            csv_w = csv.writer(csv_write)
            csv_w.writerows(new_data)

    def add_info(self, file1):
        reader = self.open_file(file1)
        rows = []
        for items in reader: # for loop that iterates through each row in the file, where 'lines' represents each row of information.
            username = items[4].split('@')[0] # cleaning the email column, splitting at '@' to get everything in front of it.
            row = [items[1], items[2], username] # combines the individual columns into a list.
            rows.append(row)
        return rows

clean1 = CSV_Cleaner()
clean1.write_file('user_details.csv')
# %%
