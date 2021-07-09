from helpers import alberoBinario

def pre_order_global(tree):
    val = 0
    pre_order(tree, val)

def pre_order(tree, val):

    val += 1
    print(tree.valore, val)
    if (tree.sx):
        pre_order(tree.sx, val)
    if (tree.dx):
        pre_order(tree.dx, val)


if __name__ == "__main__":

    tree = alberoBinario.crea(2)
    pre_order(tree)