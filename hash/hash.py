from PIL import Image
import imagehash

img1 = Image.open("../1.png")
img2 = Image.open("../2.png")

hash1 = imagehash.average_hash(img1)
hash2 = imagehash.average_hash(img2)
print("ahash")
print(hash1)
print(hash2)
print(hash1 - hash2, "\n")

hash1 = imagehash.phash(img1)
hash2 = imagehash.phash(img2)
print("phash")
print(hash1)
print(hash2)
print(hash1 - hash2, "\n")

hash1 = imagehash.dhash(img1, 8)
hash2 = imagehash.dhash(img2, 8)
print("dhash")
print(hash1)
print(hash2)
print(hash1 - hash2, "\n")
