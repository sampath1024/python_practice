#CRUD application
#Create
#Read
#Update
#Delete

db=[
    {"name":"sampath","rank":"consultant"},
    {"name":"sravanthi","rank":"manager"}
]
def add_user(name,rank):
    db.append({"name": name,"rank":rank})

def get_users():
    [print(u) for u in db]

def update_rank(name,newrank):
    for u in db:
        if u["name"]== name:
            u["rank"] = newrank
def nuke_user(name):
    global db
    db = [u for u in db if u["name"] != name ]

add_user("Ravi","Intern")
update_rank("Alice","CTO")
nuke_user("Bob")
print(db)

