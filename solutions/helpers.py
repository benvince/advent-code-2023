def read_data(day:str) -> str:
    """Read puzzle data.

    Args:
        day (str): Day to receive data from 

    Returns:
        str: Data red from file.
    """

    with open(f"./data/day{day}.txt", "r") as f:
        data = f.read()
    
    return data

