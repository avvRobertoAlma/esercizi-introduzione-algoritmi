from helpers import alberoBinario

tree = alberoBinario.crea(3)


def trovaAltezzaMinimale(tree):

    if not tree:
        return None
    
    if not tree.sx and not tree.dx:
        # è una foglia
        return 0

    else:
        
        sx = None
        dx = None
        if (tree.sx):
            sx = 1 + trovaAltezzaMinimale(tree.sx)
        
        if (tree.dx):
            dx = 1 + trovaAltezzaMinimale(tree.dx)

        if sx and dx:
            return min(sx, dx)
        elif sx:
            return sx
        elif dx:
            return dx


print(trovaAltezzaMinimale(tree))
