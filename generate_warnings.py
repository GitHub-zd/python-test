import warnings

warnings.simplefilter('error',UserWarning)
print('before')
warnings.warn('write your warn is here')
print('after')

