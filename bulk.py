import json

for x in range(5000): # <--- edit range/total json file
    with open(f'./metadata/{x}.json', 'r+') as f: # <--- or change to another path
        data = json.load(f)
        data['image'] = f"https://gateway/ipfs/CID/{x}.png" # <--- add `image` value.
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
