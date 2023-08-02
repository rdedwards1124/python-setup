def hello():
    print("Hello user person!")

def pack(a,b,c):
    return [a, b, c]

def eat_lunch(alist):
    if not alist:
        print("My lunchbox is empty!")
    else:
        print("First I eat", alist[0])
        for food in alist[1:]:
            print("Next I eat", food)



hello()

result = pack("Lions", "Tigers", "Bears")
print(result)

eat_lunch(["grapes", "bananas", "apples", "watermelon"])
