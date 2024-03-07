class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        starting_pixel = image[sr][sc]
        if starting_pixel == color: return image

        def replace_color(r, c):
            if image[r][c] == starting_pixel:
                image[r][c] = color
                if r > 0: replace_color(r - 1, c)
                if r < row - 1: replace_color(r + 1, c)
                if c > 0: replace_color(r, c - 1)
                if c < col - 1: replace_color(r, c + 1)

        replace_color(sr, sc)
        return image