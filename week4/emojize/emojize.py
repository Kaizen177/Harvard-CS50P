

from emoji import emojize
emoji=input()

try:
    print(f'Output: {emojize(emoji, language='alias')}')
except:pass
