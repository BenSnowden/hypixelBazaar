# hypixelBazaar

Unofficial library for interacting with the official [Hypixel Bazaar API](https://api.hypixel.net/#tag/SkyBlock/paths/~1skyblock~1bazaar/get).


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install hypixelBazaar.

```bash
pip install hypixelBazaar
```

## Usage
Instantiate the Bazaar class and use it to grab bazaar information.
```python
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

```
You do not have to worry about going over the limit of API requests. Hypixel updates the bazaar API every ~15 seconds, so the most recent request is cached until it is outdated.


## License
[MIT](https://choosealicense.com/licenses/mit/)
