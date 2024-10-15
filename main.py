from get_data_stats import total_salary


def main():

    filename = 'salary_list.txt'
    total, average = total_salary(filename)
    #checking if the file was empty
    if total == 0 and average == 0:
        print("No Salary Data Found")
    else:
        print(f"Total salary: ${total}, Average Salary: ${average}")


if __name__ == '__main__':
    main()


