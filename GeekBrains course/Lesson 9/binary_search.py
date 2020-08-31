from binarytree import bst

def search(bin_search_tree, number, path=''):
    if bin_search_tree.value == number:
        return f'Number {number} found on the thats way: \nRoot{path}'
    if bin_search_tree.value>number and bin_search_tree.left!=None:
            return search(bin_search_tree.left, number, path=f'{path}\nStep in the left')
    if bin_search_tree.value<number and bin_search_tree.right!=None:
            return search(bin_search_tree.right, number, path=f'{path}\nStep in the right')
    return f'Number {number} not found in the tree'
bt = bst(height=5, is_perfect=False)
print(bt)
num = int(input('Type a number for a search: '))
print(search(bt,num))