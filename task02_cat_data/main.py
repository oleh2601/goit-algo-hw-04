
from get_cat_data import get_cats_info


def main():
    
    filename = 'task02_cat_data\cat_data.txt'
    cats_info = get_cats_info(filename)
    print(cats_info)


if __name__ == '__main__':
    main()


