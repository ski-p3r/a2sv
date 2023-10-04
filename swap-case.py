def swap_case(s):
    d=''
    for i in s:
        try:
            if i.islower():
                d+=i.upper()
            else:
                d+=i.lower()
        except:
            d+=i
    return d

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)