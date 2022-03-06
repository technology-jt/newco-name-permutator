import itertools
import pandas as pd
from datetime import datetime


words = ['access',
         'intra',
         'inter',
         'scope',
         'scape',
         'nft',
         '5g',
         'face',
         'novel',
         'low',
         'node',
         'glimpse',
         'vista',
         'merge',
         'mem',
         'uni',
         'self',
         'view',
         'based',
         'double',
         'doable',
         'defy',
         'net',
         'hood',
         'open',
         'image',
         'identity',
         'person',
         'sym',
         'sim',
         'symbiotic',
         'supple',
         'supply',
         'additive',
         'trans',
         'cross',
         'vertex',
         'join',
         'lattice',
         'spot',
         'plus',
         'perk',
         'chain',
         'bit',
         'speak',
         'remote',
         'addr',
         'verack',
         'inventory',
         'invent',
         'data',
         'merk',
         'hash',
         'genesis',
         'hex',
         'private',
         'public',
         'core',
         'off',
         'on',
         'cold',
         'hot',
         'fork',
         'gas',
         'mine',
         'stake',
         'peer',
         'script',
         'shard',
         'shill',
         'side',
         'safe',
         'space',
         'dyn',
         'io',
         'ai',
         'id',
         'import',
         'dim',
         'image',
         'pic',
         'wallet',
         'transaction',
         'wall',
         'dev',
         'atom',
         'see',
         'trade',
         'share',
         'collect',
         'buy',
         'sell',
         'inspo',
         'web',
         'star',
         'lag',
         'new',
         'co',
         'flex',
         'digi',
         'digital',
         'evol',
         'auto',
         'social',
         'digitize',
         'data',
         'zone',
         'core',
         'grove']

vowel_check = lambda x: 1 if x in ["a","i","e","o","u","y","A","E","I","O","U","y"] else 0
_fdate = datetime.now().strftime(format="%y%m%d")
_fseconds = datetime.now().strftime(format="%H_%M_%S")

custom_names = []
domains = []
name_one = []
name_two =[]
syllables = []

for r in itertools.permutations(words, 2):
    name = (r[0] + " " + r[1])
    domain = (r[0] + r[1] + ".io")
    syllable = sum(list(map(vowel_check, name)))
    name_one.append(r[0])
    name_two.append(r[1])
    domains.append(domain)
    custom_names.append(name)
    syllables.append(syllable)

data = {
    'newco name': custom_names,
    'newco webname': domains,
    'pos1': name_one,
    'pos2': name_two,
    'syllables': syllables
}

df = pd.DataFrame(data)

print(f'number of words: {len(words)}')
print(f'number of names: {len(custom_names)}')
print(df)

df.to_pickle(f"./pickle_runs/{_fdate}_{_fseconds}_names.pkl")

