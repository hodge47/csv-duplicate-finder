import sys
import os
import os.path
import csv
import datetime

students_with_devices = []


def read_csv_file(input_file):
    with open(input_file) as file:
        reader = csv.reader(file, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
            else:
                students_with_devices.append((row[1], row[3]))
                line_count += 1

        print(f'Processed {line_count} lines in {input_file}...')


def check_for_dupes(student_list):
    set_of_students = []
    dupe_students = []
    for student in student_list:
        if student[0] in set_of_students and student[0] not in dupe_students:
            dupe_students.append(student[0])
        else:
            set_of_students.append(student[0])
    # Return the duplicate students
    return dupe_students


def show_dupe_students(dupe_list):
    print(f'\nStudents with multiple devices: {len(dupe_list)}')


def create_multiple_devices_file(duplicates_list):
    output_directory = "output"
    filename = f'{datetime.datetime.now().strftime("%b-%d-%Y_%I-%M-%S-%p")}'
    # Check for directory
    if not os.path.isdir(directory):
        os.mkdir(directory)
    # Make file
    path = f'{output_directory}/{filename}.csv'
    with open(path, mode='w') as newFile:
        student_writer = csv.writer(
            newFile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        student_writer.writerow(
            ["Student ID", "# Of Devices", "Device Serial Numbers"])
        for dupe in duplicates_list:
            devices = []
            for student in students_with_devices:
                if student[0] == dupe:
                    devices.append(student[1])
            student_writer.writerow(
                [f'{dupe}', f'{len(devices)}', f'{devices}'])


def main(output_directory, input_files):
    # Check directory exists
    if not os.path.exists(output_directory):
        print("That directory does not exist...")
        return
    # Check all files exist
    for file in input_files:
        filepath = f'{output_directory}/{file}'
        if not os.path.exists(filepath):
            print(f'{filepath} does not exist...')
            return
    # Read CSV files
    for file in input_files:
        filepath = f'{output_directory}/{file}'
        read_csv_file(filepath)

    print(f'\nThere are a total of {len(students_with_devices)} entries...')

    # Check for duplicates after all students are added to master list
    duplicate_students = check_for_dupes(students_with_devices)

    # Show all duplicate students
    show_dupe_students(duplicate_students)

    # Create file with students with multiple devices
    if len(duplicate_students) > 0:
        create_multiple_devices_file(duplicate_students)
    else:
        print("No files were created...")


if __name__ == "__main__":
    files = []
    directory = sys.argv[1]
    for i in range(2, len(sys.argv)):
        files.append(sys.argv[i])
    main(directory, files)
