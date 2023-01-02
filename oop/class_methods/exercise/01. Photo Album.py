from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = PhotoAlbum.m(self)

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label):
        for row, p in enumerate(self.photos):
            if len(p) < 4:
                p.append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(p)}"

        return f"No more free slots"

    def display(self):
        result = ""
        m = self.photos
        for r in m:
            for index in range(len(r)):
                if r[index] != "":
                    r[index] = "[]"

        for el in m:
            result += f"-----------" + "\n"
            result += f"{' '.join(el)}" + "\n"
        result += f"-----------" + "\n"
        return result.strip()

    def m(self):
        matrix = []
        for x in range(self.pages):
            matrix.append([] * 4)
        return matrix


# from math import ceil
#
#
# class PhotoAlbum:
#     PHOTOS_PER_PAGE = 4
#
#     def __init__(self, pages):
#         self.pages = pages
#         self.photos = self.__build_photos()
#
#     @classmethod
#     def from_photos_count(cls, photos_count):
#         pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE) # tova e 4
#         return cls(pages)
#
#     def add_photo(self, label):
#         for row_idx in range(len(self.photos)):
#             row = self.photos[row_idx]
#             if len(row) < PhotoAlbum.PHOTOS_PER_PAGE:
#                 self.photos[row_idx].append(label)
#                 return f'{label} photo added successfully on page {row_idx + 1} slot {len(self.photos[row_idx])}'
#         return 'No more free slots'
#
#     def display(self):
#         separator = '-' * 11
#         result = separator + '\n'
#         for row in self.photos:
#             result += ' '.join(['[]' for _ in row]) + '\n'
#             result += separator + '\n'
#
#         return result.strip()
#
#     def __build_photos(self):
#         result = []
#         for _ in range(self.pages):
#             result.append([])
#         return result
#
#
# album = PhotoAlbum(2)
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())