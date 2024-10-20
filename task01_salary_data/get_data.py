import pathlib

#reading data from the file, printing message if it's empty and
#passing and empty list in that case
def load_data(filename: str) -> list[str]:
        with open(filename, 'r', encoding='utf-8') as file:
            list_of_salaries = file.readlines()
            if not list_of_salaries:
                print ('File is empty')
                return []
            return list_of_salaries 


#clearing the data and double checking if it's valid
def clear_data(salary_data: list[str]) -> list[float]:
    if not salary_data:
        return []
    output_list = []
    for salary in salary_data:
        try:
            #deleting whitespaces and splitting the line with coma and using only the second part
            output_list.append((float(salary.strip().split(',')[1]))) 
        except (ValueError, IndexError):
            print(f"Bad data found at line {salary.strip()}")
    return output_list