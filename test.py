import requests


t = {'normal': 0.319, 'psoriasis': 0.029, 'pruritus nodular': 0.019, 'couperose': 0.002, 'ineffective': 0.349, 'lichen': 0.021, 'herpes': 0.257, 'eczema': 0.004}

result = dict(sorted(t.items(), key=lambda kv: kv[1]))

print(result)