import json
from datetime import datetime, timedelta

def read_file() -> list:
    """Read a .json file

    Returns:
        dict: Read JSON
    """
    f = open("products.json", "r")
    data = json.load(f)
    f.close()
    return data

def apply_filter(data: list,  filter_function: callable) -> list:
    """Apply callback filter function to a list

    Args:
        data (list): List where a filter would be applied
        filter_function (callable): Filter function to apply

    Returns:
        list: Filtered list
    """
    result: list = list(filter(filter_function, data))
    return result

def sort_by_key(data: list, key, reverse=True) -> list:
    """Sort a list of objects by a key property

    Args:
        data (list): List to be sorted
        key (_type_): Key property where the sort algorithm would be applied
        reverse (bool, optional): Indicator wether the list should be asc or desc. Defaults to True.

    Returns:
        list: Sorted list by a key
    """
    data.sort(key=key, reverse=reverse)
    return data

def calculate_top_average_rating(data: list, limit: int=-1) -> float:
    """Calculate top average rating of products with a given limit

    Args:
        data (list): List to iterate
        limit (int, optional): Amount of items to iterate. If its -1 then limit should never be applied. Defaults to -1.

    Returns:
        float: Average rating of top items
    """
    acum_rating: int = 0
    iterated_items: int = 0
    for item in data:
        acum_rating += item["rating"]
        iterated_items += 1
        if iterated_items == limit:
            break
    if iterated_items == 0: # Avoid zero division if list is empty.
        return 0
    return acum_rating / iterated_items


if __name__ == "__main__":
    # First read the file
    products: list = read_file()


    # Create 3 months difference date and lambda function to apply filter
    filter_date: datetime = datetime.now() - timedelta(weeks=12)
    filter_lambda_function = lambda x: datetime.strptime(x['updated_at'], "%Y-%m-%d") > filter_date
    products: list = apply_filter(products, filter_lambda_function)

    # Sort by price
    products = sort_by_key(products, key=lambda x: x["price"])

    # Calculate top average
    average_rating: float = calculate_top_average_rating(products, 10)
    print("%.2f" % average_rating)


    