# 📱 Social Media Feed Story (30 lines)

# 1️⃣ Users
alice = {"name": "Alice", "followers": 150}
bob   = {"name": "Bob", "followers": 200}
charlie = {"name": "Charlie", "followers": 100}

# 2️⃣ Posts as dicts
post1 = {
    "user": alice,
    "content": "Just baked some cookies!",
    "likes": 0,
    "comments": []
}

post2 = {
    "user": bob,
    "content": "Check out my new painting!",
    "likes": 0,
    "comments": []
}

# 3️⃣ Feed as a list of posts
feed = [post1, post2]

# 4️⃣ Charlie likes Alice's post
post1["likes"] += 1

# 5️⃣ Charlie comments on Bob's post
post2["comments"].append({
    "user": charlie,
    "comment": "Wow, amazing colors!"
})

# 6️⃣ Bob makes a new post
post3 = {
    "user": bob,
    "content": "Sunset at the beach 🌅",
    "likes": 0,
    "comments": []
}
feed.append(post3)

# 7️⃣ Alice likes Bob's new post
post3["likes"] += 1

# 8️⃣ Charlie comments on Alice's post
post1["comments"].append({
    "user": charlie,
    "comment": "Save me some cookies! 😋"
})

# 9️⃣ Another comment added to Bob's first post
post2["comments"].append({
    "user": alice,
    "comment": "Incredible work, Bob!"
})

# 🔟 Feed snapshot
print("Social Media Feed:")
for post in feed:
    print(f"{post['user']['name']} posted: {post['content']}")
    print(f"Likes: {post['likes']}, Comments: {len(post['comments'])}")
    for c in post["comments"]:
        print(f" - {c['user']['name']} said: {c['comment']}")
    print()