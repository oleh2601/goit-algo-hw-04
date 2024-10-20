
from get_data import load_data, clear_data

#calculating average salary and returning 0 if there is no data
def calculate_average_salary( salary_list: list[float] ) -> int:
    if not salary_list:
        return 0
    return sum(salary_list) / len(salary_list)

#calculating total salary and returning 0 if there is no data
def calculate_total_salary( salary_list: list[float]) -> int:
    if not salary_list:
        return 0   
    return sum(salary_list)

#reading and cleaning the data and returning a tuple 
#with total and average salary
def total_salary(filename: str) -> tuple:
        raw_data = load_data(filename)
        cleared_data = clear_data(raw_data)
        total = calculate_total_salary(cleared_data)
        average = calculate_average_salary(cleared_data)
        return (total, average)