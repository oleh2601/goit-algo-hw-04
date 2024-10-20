from get_data_stats import total_salary

def main():

    filename = 'task01_salary_data/salary_list.txt'    
    total, average = total_salary(filename)

    if total == 0 and average == 0:
        print("No Salary Data Found")
    else:
        print(f"Total salary: ${total:.2f}, Average Salary: ${average:.2f}")

if __name__ == "__main__":
    main()

