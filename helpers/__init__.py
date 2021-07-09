from helpers import  alberoBinario

def pre_order(tree):

    print(tree)
    if (tree.sx):
        pre_order(tree.sx)
    if (tree.dx):
        pre_order(tree.dx)


if __name__ == "__main__":

    tree = alberoBinario.crea(3)
    pre_order(tree)