
class AlberoBinario:
    def __init__(self, V, sx=None, dx=None):
        self.valore = V
        self.sx = sx
        self.dx = dx



################### DA QUI IN GIÙ SONO SOLO FUNZIONI NECESSARIE PER I TEST #####################



def fromLista(lista):
    '''Crea l'albero da una lista [valore, listafigli]
           In cui lista figli contiene alberi o e' la lista vuota. '''
    r=AlberoBinario(lista[0])
    if lista[1]!=None: r.sx= fromLista(lista[1])
    if lista[2]!=None: r.dx= fromLista(lista[2])
    return r

def crea(x):
    a='''genera un albero i cui nodi sono definiti calla classe AlberoBinario:
    
    class AlberoBinario:
        def __init__(self, V, sx=None, dx=None):
            self.valore = V
            self.sx = sx
            self.dx = dx
    
    '''
    print(a)
    if x==1:
        a='''genera albero:                          
     0                                             
    / \                                            
   5   6                                           
      /                                            
     3                                             
    / \                                            
   9   7                                           
                                                   
        '''
        lista1= [0,[5, None, None],[6,[3,[9, None, None],[7, None, None]],None]]
        tree1=fromLista(lista1)
        print(a)
        return tree1
    elif x==2:
        a='''genera albero:            
                    36                 
             _______|______            
            |              |           
            26             10          
         ___|___        ___|__         
        |       |      |      |        
        3       55     3     15        
       _|_     _|_    _|_    _|_       
      |   |   |   |  |   |  |   |      
      1   2   3   4  5   6  7   8      
                                       
    '''                                
        lista2=[36,
                 [26,
                    [3,[1,None,None],[2,None,None]],
                    [55,[3,None,None],[4,None,None]],
                 ], 
                 [10,
                    [3,[5,None,None],[6,None,None]],
                    [15,[7,None,None],[8,None,None]],
                 ]
                ]
        tree2=fromLista(lista2)
        print(a)
        return tree2
    elif x==3:
        a='''genera albero
                          76                            
            ______________|_______________              
           |                              |             
          12                              37            
    _______|_______              _________|_____        
   |               |            |               |       
   80             15           71              100     
 __|__          ___|____     __|__            __|___    
|     |         |       |   |     |          |      |   
5     19        47      96  92   67         23      121 
   ___|___    __|___         ____|______      \      \  
  |       |  |      |       |           |     81     44 
  181     28 94     29      70          8               
                                         \              
                                          30            
                                          _|_           
                                         |   |          
                                        46  21          
                                                        
    '''
        lista1=[76,
              [12,
                 [80,
                    [5,None,None],
                    [19,
                       [181,None,None],
                       [28,None,None],
                    ],
                  ],
                 [15,
                    [47,
                       [94,None,None],
                       [29,None,None],
                    ],
                    [96,None,None],
                  ],
              ],
              [37,
                 [71,
                   [92,None,None],
                   [67,
                      [70,None,None],
                      [8,None,
                         [30,
                           [46,None,None],
                           [21,None,None],
                          ],
                       ],
                   ],
                  ],
                 [100,
                     [23,None,
                        [81,None,None],
                      ],
                     [121,None,
                          [44,None,None],
                      ],
                 ],
               ],
        ]
        tree3=fromLista(lista1)
        print(a)
        return tree3
    if x==4:
        a='''genera albero:                          
             1     
            /\     
           2  3    
          / \      
        4    5     
       /    /      
      6    7       
     /     \       
     8      9      
    '''
        lista1= [1, [2, [4, [6, [8, None, None], None], None], [5, [7, None, [9, None, None]], None]], [3, None, None]]
        tree4=fromLista(lista1)
        print(a)
        return tree4
    if x==5:
        a='''genera albero:             
         5            
          \           
           1          
          /           
        5             
         \            
          1           
          /           
         5            
    '''
        lista1=[5,None,[1,[5,None,[1,[5,None,None],None]],None]]
        tree5=fromLista(lista1)
        print(a)
        return tree5

    else: 
        print('serve un numero tra 1 e 5')

