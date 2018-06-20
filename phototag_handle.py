from PhotoTag_modul import *

# find tags that have at least 3 photos associated with them,多对多
query = (Tag.select().join(PhotoTag).join(Photo).
         group_by(Tag).having(fn.Count(Photo.id) > 1))
# for m in query:
#     print(m.name)

qur = (Tag.select(Tag, fn.Count(Photo.id).alias('count'))
         .join(PhotoTag)
         .join(Photo)
         .group_by(Tag)
         .having(fn.Count(Photo.id) > 1))
# for m in qur:
#     print(m.count)

#  retrieve scalar values by calling scalar(as_tuple=True), 直接取值
que=Tag.select(Tag.name,Tag.id).where(Tag.id == 1).scalar(as_tuple=True)
# print(que)

