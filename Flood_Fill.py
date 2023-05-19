from typing import List


# The idea here is to go recursively traverse through each direction, with escape clauses for out of range,
# already filled, or not the color we want to replace.
class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        # Define the color to replace
        color_to_replace = image[sr][sc]

        def recurse(x, y):
            # if out of range, escape
            if x >= len(image) or x < 0 or y >= len(image[0]) or y < 0:
                return

            # if it's already filled or not the color to replace, escape
            if image[x][y] == color or image[x][y] != color_to_replace:
                return

            # perform the replace operation
            if image[x][y] == color_to_replace:
                image[x][y] = color

            # all four dimensions
            recurse(x - 1, y)
            recurse(x + 1, y)
            recurse(x, y - 1)
            recurse(x, y + 1)

        recurse(sr, sc)
        return image
