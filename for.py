from mysql import Person, Pet
from datetime import date
# pet = Pet.select().where((Pet.owner_id==3) & (Pet.animal_type == 'cat'))
#
# for m in pet:
#     m.name = int(m.name) + 2
#     m.save()
#     print(m.name)
person = Person.select()
for m in person:
    # m.birthday = m.birthday + date(1960-10-6)
    # m.save()
    print(m.birthday)