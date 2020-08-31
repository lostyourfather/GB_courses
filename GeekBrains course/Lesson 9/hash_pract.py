import hashlib

def is_eq_str(a: str, b: str, verbose=False) -> bool:
    assert len(a)>0 and len(b)>0, 'Strings can not be a space'

    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()
    
    if verbose:
        print(f'hash 1 = {ha}\nhash 2 = {hb}')

    return ha==hb



s_1 = input('Enter the first string: ')
s_2 = input('Enter the second string: ')

print('Strings is equals' if is_eq_str(s_1,s_2,True) else 'Strings is not equals')


def rabin_karp(s: str, subs: str) -> int:
    assert len(s)>0 and len(subs)>0, 'Strings can not be a space'
    assert len(s) >= len(subs), "Sub string can not be more leght than string"

    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():

            if s[i:i + len_sub] == subs:
                return i

    return -1


s_1 = input('Enter the string: ')
s_2 = input('Enter the sub string: ')

pos = rabin_karp(s_1, s_2)
print(f'Sub string found in {pos}' if pos!= -1 else 'Sub strings is not found')