import pathlib

def get_cats_info(path: str) -> list[dict]:
    raw_data = load_data(path)
    clean_data = clear_data(raw_data)
    list_cat_dic = []
    for cat_list in clean_data:
        cat_dic = {
            'ID': cat_list[0],
            'Name' : cat_list[1],
            'Age' : cat_list[2],
        }
        list_cat_dic.append(cat_dic)
    return list_cat_dic



def load_data(path: str) -> list[str]:
    with open(path, 'r', encoding='utf-8') as file:
        list_of_cats = file.readlines()
    list_of_cats = [arg.strip() for arg in list_of_cats]
    if list_of_cats == []:
        print("The file with cat data is empty")
        return []
    return list_of_cats

def clear_data(list_of_cats: list[str]) -> list[list]:
    if not list_of_cats:
        return []
    list_of_cat_args = []
    for arg in list_of_cats:
        try:
            cat_info = [item.strip() for item in arg.split(',')]
            if len(cat_info) != 3:
                raise ValueError("Expected ID, Cat's name and age")
            list_of_cat_args.append(cat_info)
        except (ValueError, IndexError) as e:
            print(f"Bad data found at line {arg.strip()} - {e}")
    return list_of_cat_args