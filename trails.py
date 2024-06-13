users_data = {
    "user1": {
        "username": "alice123",
        "tweets": [
            "Excited about the new project launch!",
            "Loving the sunny weather today."
        ],
        "activity": {
            "likes": 120,
            "dislikes": 5
        }
    },
    "user2": {
        "username": "bob_the_builder",
        "tweets": [
            "Building a new deck for the backyard.",
            "Finished the new bookshelf!"
        ],
        "activity": {
            "likes": 95,
            "dislikes": 3
        }
    },
    "user3": {
        "username": "charlie_chef",
        "tweets": [
            "Tried a new pasta recipe today.",
            "Can't wait to bake the new cake!"
        ],
        "activity": {
            "likes": 150,
            "dislikes": 10
        }
    },
    "user4": {
        "username": "diana_artist",
        "tweets": [
            "Working on a new painting.",
            "Art gallery visit was inspiring."
        ],
        "activity": {
            "likes": 200,
            "dislikes": 8
        }
    },
    "user5": {
        "username": "eric_traveler",
        "tweets": [
            "Visited the mountains last weekend.",
            "Planning a trip to Europe next month."
        ],
        "activity": {
            "likes": 180,
            "dislikes": 12
        }
    },
    "user6": {
        "username": "fiona_writer",
        "tweets": [
            "Working on the second chapter of my book.",
            "Got an idea for a new story!"
        ],
        "activity": {
            "likes": 130,
            "dislikes": 7
        }
    },
    "user7": {
        "username": "george_gamer",
        "tweets": [
            "Just won my first game in the new league!",
            "Streaming tonight at 8 PM, join me!"
        ],
        "activity": {
            "likes": 210,
            "dislikes": 15
        }
    },
    "user8": {
        "username": "hannah_health",
        "tweets": [
            "Morning yoga session was amazing.",
            "Sharing my favorite smoothie recipe today!"
        ],
        "activity": {
            "likes": 175,
            "dislikes": 4
        }
    }
}
l = [user["username"] for user in users_data.values()]
