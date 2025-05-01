from base import db,Puppy

my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

all_Puppies = Puppy.query.all()
print(all_Puppies)
puppy_one = Puppy.query.get(1)
print(puppy_one)

first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

second_puppy = Puppy.query.get(1)
print(f'Successfully deleted puppy {second_puppy.name}')
db.session.delete(second_puppy)

print(Puppy.query.all())
