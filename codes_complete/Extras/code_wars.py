# Created on 01 November 2018
# @author vinimmelo
# Code Wars challenges
# Site => https://www.codewars.com

def remove_duplicity(text):
    #return number of duplicity text
    counter = 0
    text_list = list(text.lower())
    new_list = text_list[:]
    for i in text:
        if (new_list.count(i) > 1):
            new_list.remove(i)
    for x in new_list:
        if(text_list.count(x) > 1):
            counter += 1
    return counter


def filter_list(l):
    # return a new list with the strings filtered out
    return [x for x in l if type(x) is not str]


def descending_order(num):
    #return numbers in descending order
    new_list = sorted([int(x) for x in list(str(num))], reverse=True)
    return ''.join(map(str, new_list))


def digital_root(n):
    #recursive sum of all the digits in a single number.
    if n >= 10:
        x = n //10
        y = digital_root(x) + n % 10
        if(y >= 10):
            return digital_root(y)
        else:
            return y
    else:
        return n


def validate_pin(pin):
    #Accept pins with 4 or 6 digits (only numbers)
    try:
        return (len(pin) == 4 or len(pin) == 6) and int(pin) >= 0 and pin.isdigit()
    except:
        return False


def bool_to_word(bool):
    return "Yes" if bool else "No"


def number(bus_stops):
    sum = 0
    subtrain = 0
    for x in bus_stops:
        sum += x[0]
        subtrain +=x[1]
    return sum - subtrain




if __name__ == '__main__':
    print(number([[10,0],[3,5],[5,8]]))
    print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
