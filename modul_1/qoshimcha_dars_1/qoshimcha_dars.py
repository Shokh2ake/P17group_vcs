# nums = [8, 1, 2, 2, 3]
# re = []
# for i in nums:
#     c = 0
#     for j in nums:
#         if i > j:
#             c += 1
#     re.append(c)
# print(re)


# from string import ascii_lowercase
#
# sentence = "thequickbrownfoxjumpsoverthelazydog"
#
# for i in ascii_lowercase:
#     if not i in ascii_lowercase:
#         print(False)
#         break
# else:
#     print(True)

# from string import ascii_lowercase
# belgilar = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# words = ["gin","zen","gig","msg"]
# d = {}
#
# for i in range(len(ascii_lowercase)):
#     d[ascii_lowercase[i]] = belgilar[i]
# tmp = []
# for i in words:
#     t = ""
#     for j in i:
#         t += d[j]
#     tmp.append(t)
# print(len(set(tmp)))

# mat = [[0, 0, 0], [0, 1, 1]]
#
# re = [0, float("-inf")]
# for k, v in enumerate(mat):
#     if re[1] < (s:= sum(v)):
#         re[1] = s
#         re[0] = 0
# print(re)


# image = [[1, 1, 0],
#          [1, 0, 1],
#          [0, 0, 0]]
# fro i in range(len(image))

class Solution(object):
    def projectionArea(self, grid):

        xy = sum([len([i for i in g if i != 0]) for g in grid])
        zx = sum([max(g) for g in grid])
        yz = sum([max(g) for g in list(zip(*grid))])

        print(xy + yz + zx)
