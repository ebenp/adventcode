if __name__ == '__main__':
    with open('input1.txt', "r") as myfile:
        # strip new lines just in case
        data=myfile.read().replace('\n', '')

    count = 0

    for i in data:
        
        if i =="(":
            count += 1
        else:
            count -= 1
    print count
