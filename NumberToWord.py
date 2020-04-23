from math import ceil

letters = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
        "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]

twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

thousands = ["", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ",
             "septillion ", "octillion ", "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ",
             "quattuordecillion ", "quindecillion ", "sexdecillion ", "septendecillion ", "octodecillion ",
             "novemdecillion ", "vigintillion "]


def num2word(num):
    word = ''
    num = str(num)
    length = len(num)
    # ar is the number split into triples with the exception of the first units. ie. if the number is 1234567,
    # ar = ['1', '234', '567']
    ar = []
    # we split the number into sections of three, since that's how we determine size of numbers ourselves
    for i in range(ceil(length / 3)):
        # grab the last 3 digits of the number from the back and append them to ar, and strip
        # the number of those digits
        trisplit = num[-3:]
        ar.append(trisplit)
        num = num[:-3]
    # we have now ar = ['567', '234', '1'], so we reverse the array, to get the final result of
    # ar = ['1', '234', '567'], which will make it easier to count
    ar = ar[::-1]

    total_trips = len(ar)
    trip_count = 0
    # we treat each triple as it's own number, and append the thousands unit to it afterwards
    for trip in ar:
        trip_count += 1
        count = 0
        num_in_trip = len(trip)
        for digit in trip:
            count += 1
            # count the number of digits after the current digit in the triple to tell what unit to use (hundreds/ones)
            after_digits = num_in_trip - count
            if after_digits == 0:
                word += ones[int(digit)]
            elif after_digits == 1:
                # then we are in the twenties, but we need to check if the digit is 1, since ten to
                # nineteen don't follow rules which other twenties do
                if int(digit) == 1:
                    running_digits = trip[-2:]
                    word += ones[int(running_digits)]
                    break
                else:
                    word += twenties[int(digit)]
            elif after_digits == 2:
                # then we have a number either like '234' or '023', if we have '023' then we don't need to worry about
                # the hundreds unit, we can just ignore it and move to the next digit in the triple
                if digit != '0':
                    word += ones[int(digit)] + 'hundred '
        # we've gone through each digit in the triple, so now we can add the corresponding thousands unit, but only
        # if it's not '000'
        if trip != '000':
            word += thousands[total_trips - trip_count]
    return word


if __name__ == "__main__":
    print(num2word(0))
