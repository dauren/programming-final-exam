with open('in.csv', 'r') as file:
    lines = file.readlines()
    max_region = None
    max_price = 0
    for line in lines[1:]: #skip 1st line because header row
        cols = line.split(";")
        region = cols[0]
        #continue your code
    print(max_region)
