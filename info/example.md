**Example:**

```python
from battle import commander
unit_client = commander.Client()

def search_and_destroy(data=None, *args, **kawargs):
    enemy = unit_client.ask_nearest_enemy()
    unit_client.attack_item(enemy['id'])
    unit_client.subscribe_the_item_is_dead(enemy['id'], search_and_destroy)

search_and_destroy()
```
