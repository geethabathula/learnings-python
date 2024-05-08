playlist = [{
    "title":"GeePlay",
    "author":"Geetha",
    "songs" :[{"songname":"Nuvvunte na jathaga",
             "singer":"Sidsriram",
             "rating":5
             },
            {"songname":"Em sandeham Ledhu",
             "singer":"Sunita",
             "rating":3.9
             },
            {"songname":"Buttabomma",
             "singer":"Arman Malik",
             "rating":2
             },
            ]
            }]
print(playlist)
for list1 in playlist:
    for song in list1["songs"]:
        print(song["rating"])
