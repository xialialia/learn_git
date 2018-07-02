from peewee模型.jointojoin import *
team_objs = User.select(Team, User, Teamprofile). \
            join(Team, on=(User.id == Team.user)). \
            join(Teamprofile,on=(Team.id == Teamprofile.user)).\
            where(Team.id > 1).order_by(Team.id)

for m in team_objs:
    print(m.Teamprofilr.address)