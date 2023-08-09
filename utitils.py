def matrixFromListDict(listDict):
    # Get the keys
    keys = listDict[0].keys()
    # Create a list of lists
    listOfLists = []
    for dict in listDict:
        listOfLists.append([dict[key] for key in keys])
    # Convert the list of lists to a matrix
    return listOfLists


