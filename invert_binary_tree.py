def invertTree():

    root = ''

    if not root:
        print('none')
        exit()

    tmp = root.left
    root.left = root.right
    root.right = tmp

    invertTree(root.left)
    invertTree(root.right)
    print(root)

