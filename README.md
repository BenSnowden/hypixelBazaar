# hypixelBazaar

Unofficial library for interacting with the official Hypixel bazaar API.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install hypixelBazaar.

```bash
pip install hypixelBazaar
```

## Usage

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



## License
[MIT](https://choosealicense.com/licenses/mit/)
