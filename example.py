from hypixelBazaar import Bazaar

baz = Bazaar()
product_list = baz.get_product_list()

for p in product_list:
    print(baz.get_buy_price(p))
    print(baz.get_sell_price(p))
    print(baz.get_product_id(p))
    print(baz.get_sell_volume(p))
    print(baz.get_buy_volume(p))
    print(baz.get_buy_moving_week(p))
    print(baz.get_sell_moving_week(p))
    print(baz.get_buy_order_count(p))
    print(baz.get_sell_order_count(p))
