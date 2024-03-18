class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        len_img = len(image)
        odd = True if len_img & 1 else False

        for img in range(len_img):
            l, r = 0, len_img -1
            while l<r:
                image[img][l], image[img][r] = abs(image[img][r]-1), abs(image[img][l]-1)
                l += 1
                r -= 1
            if odd: image[img][l] = abs(image[img][l]-1)

        return image


'''
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        len_img = len(image)
        for img in image:
            l, r = 0, len_img -1
            while l<=r:
                # if they are different (1,0 or 0,1), they do not change
                if img[l] == img[r]:
                    img[l], img[r] = img[l]^1, img[r]^1
                    # Bitwise XOR --> 0^1 = 1, 1^1 =0
                l += 1
                r -= 1
        return image
'''