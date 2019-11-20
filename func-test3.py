def apple_price(apple_num):
    box = 0
    if apple_num % 5 == 0:
        box = apple_num//5
    else:
        box = apple_num//5+1
    print("苹果的总价格是：",apple_num*2+box)
    return apple_num*2+box


def pineapple_price(pineapple_num):
    print("菠萝的总价为：",pineapple_num*8+pineapple_num)
    return pineapple_num*8+pineapple_num


def watermelon_price(watermelon_num):
    print("西瓜的总价为：",watermelon_num*10+watermelon_num)
    return watermelon_num*10+watermelon_num


if __name__ == '__main__':
    apple_num = int(input("请输入购买苹果的数量："))
    pineapple_num = int(input("请输入购买菠萝的数量："))
    watermelon_num = int(input("请输入购买西瓜的数量："))
    apple_price(apple_num)
    pineapple_price(pineapple_num)
    watermelon_price(watermelon_num)