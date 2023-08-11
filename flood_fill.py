image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2

def flood_fill(image, sr, sc, newColor):
    originalColor = image[sr][sc]
    if originalColor == newColor:
        print(image)

    def dfs(row, col):
        # If outside the bounds of the image, or not the original color, return
        if (row < 0
            or row >= len(image)
            or col < 0
            or col >= len(image[0])
            or image[row][col] != originalColor):
            exit()

    # Change the color of this pixel
        image[row][col] = newColor

    # Call DFS on all neighbors (up, down, left, right)
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    dfs(sr, sc)
    print(image)
