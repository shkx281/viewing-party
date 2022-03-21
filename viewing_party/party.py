# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None

    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # movie_watched = ""
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            movie_watched = user_data["watchlist"][i]
            del user_data["watchlist"][i]
            user_data["watched"].append(movie_watched)  
    return user_data

    # .haskey() does NOT work in python3 --> use key in list of dictionary

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum_rating = 0
    count = 0
    for i in range(len(user_data["watched"])):
        sum_rating += user_data["watched"][i]["rating"]
        count += 1
    if count == 0:
        return 0
    else:
        return sum_rating/count

def get_most_watched_genre(user_data):
    genre_list = []
    for i in range(len(user_data["watched"])):
        genre_list.append(user_data["watched"][i]["genre"])
    if len(genre_list) == 0:
        return None
    else:
        # To get the most frequent genre. I'm not sure if it accounts for ties.
        return max(set(genre_list), key=genre_list.count)
        # might be better to use Count from importing collections.. look at StackOverflow

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # Can I also create a set with a combination of the users and friends watched list?"
    friends_movie_lists = [d["watched"] for d in user_data["friends"]] 
    unique_watched_list = []

    for movie in user_data["watched"]:
        if not any(movie in d for d in friends_movie_lists):
            unique_watched_list.append(movie)
    return unique_watched_list      

def get_friends_unique_watched(user_data):
    friends_movie_lists = [d["watched"] for d in user_data["friends"]]
    flat_list = [movie for sublist in friends_movie_lists for movie in sublist]
    friends_unique_list = []
    for movie in flat_list:
        if movie not in user_data["watched"] and movie not in friends_unique_list:
            friends_unique_list.append(movie)
    return friends_unique_list


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friends_unique_list = get_friends_unique_watched(user_data)
    recommended_list = []
    for movie in friends_unique_list:
        if movie["host"] in user_data["subscriptions"]:
            recommended_list.append(movie)
    return recommended_list


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    friends_unique_list = get_friends_unique_watched(user_data)
    genre_list = []
    new_rec = []
    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])
    
    if len(genre_list) > 0:  
        max_genre = max(set(genre_list), key=genre_list.count) #howww?
        for movie in friends_unique_list:
            if movie["genre"] == max_genre:
                new_rec.append(movie)
    return new_rec