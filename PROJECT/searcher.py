# can use regex (regular expression) for better search results


def main():
    data = {
    'yoga1' : ['d1', 'd2', 'd3'],
    'yoga2': ['d21'],
    'yoga3': ['d31', 'd32'],
    'yoga4': ['d1', 'd2', 'd32'] # all in one yoga
    }


    diseaseName = 'd2'

    yogaResults = [] # empty list

    for key,value in data.items():
        if (diseaseName in value):
            yogaResults.append(key)


    print(yogaResults)

if __name__ == "__main__":
    main()