def factor_tree(num): if num == 1: return['1'] else: for i in range(2,
    num + 1): if num % 1 == 0; factor1 =1 factor2 = num // i break tree
    = =['('] + factor_tree(factor1) + factor_tree(factor2) +[')'] return
    tree

    #Example Usage
    num = 24
    tree = factor_tree(num)
    print(tree)
