from Models import app,db,Puppy,Owner,Toy


with app.app_context():
    db.drop_all()
    db.create_all()
    rufus = Puppy('Rufus')
    fido = Puppy('Fido')

    db.session.add_all([rufus,fido])
    db.session.commit()

    print(Puppy.query.all())

    rufus = Puppy.query.filter_by(name='Rufus').first()##first puppy

    jose = Owner('jose',rufus.id)
    toy1 = Toy('Chew Toy',rufus.id)
    toy2 = Toy('Ball Toy',rufus.id)

    db.session.add_all([jose,toy1,toy2])
    db.session.commit()

    rufus = Puppy.query.filter_by(name='Rufus').first()
    print(rufus)

    rufus.report_toys()