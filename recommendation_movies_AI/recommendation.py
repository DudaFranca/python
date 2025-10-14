movies = {
    'Inception': ['sci-fi', 'action'],
    'The Matrix': ['sci-fi', 'action'],
    'The Hangover': ['comedy'],
    'Toy Story': ['animation', 'comedy'],
    'Die Hard': ['action'],
    'Interstellar': ['sci-fi', 'drama']

}

print("Available Movies: action, sci-fi, comedy, drama, animation")
user_genre = input("What genre do you like? ") # Pega a categoria que o usuário gosta

recommendations = []

for movie_name, movie_genres in movies.items(): # Pega o nome e o gênero dos filmes listados
    if user_genre in movie_genres: # Compara se o gênerio digitado tem na lista
        recommendations.append(movie_name) # Adiciona as recomendações

if len(recommendations) == 0: # Se não existir recomendações
    print("Sorry, no movies found!")
else:
    print(f"Recommended {user_genre} movies:")
    for i in range(len(recommendations)): # Analisa as recomendações e lista os filmes que estão lá
        print(f"{i+1}. {recommendations[i]}")

print(f"You chose: {user_genre}")