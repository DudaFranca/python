movies = {
    'Inception': {
        'genres': ['sci-fi', 'action'],
        'rating': 8.8
    },
    'The Matrix': {
        'genres': ['sci-fi', 'action'],
        'rating': 8.7
    },
    'The Hangover': {
        'genres': ['comedy'],
        'rating': 7.7
    },
    'Toy Story': {
        'genres': ['animation', 'comedy'],
        'rating': 8.3
    },
    'Die Hard': {
        'genres': ['action'],
        'rating': 8.2
    },
    'Interstellar': {
        'genres': ['sci-fi', 'drama'],
        'rating': 8.6
    }
}

users_ratings = {
    'Alice': {
        'Inception': 5,
        'The Matrix': 5,
        'Interstellar': 4
    },
    'Bob': {
        'Inception': 5,
        'Die Hard': 5,
        'The Hangover': 3
    },
    'Charlie': {
        'Toy Story': 5,
        'The Hangover': 4,
        'Inception': 3
    }
}

# Coletar avaliações do usuário
# Mostra os filmes disponíveis
print("Filmes disponíveis:")
for i, movie_name in enumerate(movies.keys(), 1):
    print(f"{i}. {movie_name}")

# Pede para avaliar alguns filmes
my_ratings = {}

print("\nEvaluate some movies you have watched (or type 0 to skip):")

for movie_name in movies.keys():
    rating = input(f"What rating do you give to '{movie_name}'? (0-5, or 0 to skip): ")

    if rating != '0':
        my_ratings[movie_name] = int(rating)

print(f"\nYour ratings: {my_ratings}")

# Encontrar usuário mais similar
# Calcula similaridade com cada usuário
best_match = None
best_score = 0

for user_name, user_ratings in users_ratings.items():
    score = 0
    for movie, my_rating in my_ratings.items():
        if movie in user_ratings:
            if user_ratings[movie] == my_rating:
                score += 1

    if score > best_score:
        best_score = score
        best_match = user_name

# Recomendar filmes que o usuário similar gostou

print(f"\nBased on your movies, we recommend:")

recommendations = []

# Pega os filmes que o best_match avaliou
for movie_name, rating in users_ratings[best_match].items():
    # Verifica se VOCÊ ainda não viu esse filme
    if movie_name not in my_ratings:
        recommendations.append({
            'name': movie_name,
            'rating': rating,
            'movie_rating': movies[movie_name]['rating']
        })

# Ordena por nota do usuário similar
recommendations.sort(key=lambda x: x['rating'], reverse=True)

# Mostra as recomendações
if len(recommendations) == 0:
    print("You have watched all the movies that this user has seen!")
else:
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec['name']} (user's rating: {rec['rating']}, IMDb: {rec['movie_rating']})")

