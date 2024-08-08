
Menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

d=0
i=3
try :

    while i>0:
        i-=1
        te=input('Item: ').title()
        if te in Menu :
            d+=float(Menu[te])
            print(f'Total: ${d:.2f}')
        else:
            continue

except EOFError:
    pass




