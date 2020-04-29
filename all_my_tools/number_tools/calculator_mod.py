"""
Calculator module
"""

def add(a, b):
    """
    return a + b
    """
    return a + b

def sub(a, b): 
    """
    return a - b
    """
    return a - b

if __name__ == '__main__':
    print("exécution du programme de test du module 'calculator' ")
    assert add(1,2)==3, "la fonction add() bug "
    assert sub(1,2)==-1, "la fonction sub() bug"