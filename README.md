# BULK EDIT JSON FILE

This code is especially for nft creators after generating and having problems with json metadata with "image" or other json key

```py
import json

for x in range(5000): # <--- change (5000) to your total supply or your total json file
    with open(f"./path/to/metadata/{x}.json", 'r+') as f: # Don't change {x}!
        data = json.load(f)
        data['image'] = f"https://link/to/ipfs/{x}.png" # <--- add `id` value.
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
```
