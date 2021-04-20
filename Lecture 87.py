import csv

def red_csv():
    with open('employee_birthday.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')

def Write_csv():
    
    with open('Member_BNK.csv', mode ='w') as Member_File:
        member_writer = csv.writer(Member_File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        member_writer.writerow(['Member', 'Member', 'Member', 'Member'])
        member_writer.writerow(['Noey', 'Pape', 'NamNeung','Molabill'])
        member_writer.writerow(['BNK', 'BNK', 'BNK', 'BNK'])

Write_csv()