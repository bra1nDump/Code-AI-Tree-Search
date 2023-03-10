import json

def avg(xs):
    return sum(xs) / len(xs)

batch_stats = []
for i in range(0,1000):
    try:
        with open(f"../generate/results/{i}.json", "r") as f:
            data = json.loads(f.read())
            batch_stats.append(data["rewards"][0])
    except Exception:
        pass
print({'avg': avg(batch_stats), 'size': len(batch_stats), 'sum': sum(batch_stats), 'zero': len(list(filter(lambda x: x == 0, batch_stats)))})