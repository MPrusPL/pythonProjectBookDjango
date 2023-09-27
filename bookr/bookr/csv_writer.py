import csv

def write_csv(filename, header, data):
    try:
        with open(filename, 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            csv_writer.writeheader()
            csv_writer.writerows(data)
    except (IOError, OSError) as csv_file_error:
        print('Nie można zapisać. Wyjątek {}'.format(csv_file_error))

if __name__ == '__main__':
    header = ['name', 'age', 'gender']
    data = [['Richard', 32, 'M'], ['Mumzil', 21, 'F'], ['Melinda', 25, 'F']]
    filename = 'sample_output.csv'
    write_csv(filename, header, data)

