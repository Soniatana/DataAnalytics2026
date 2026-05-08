# Create list

movies = ["Inception", "Black Panther", "Titanic", "Avatar"]


# Length of list
print("The list movies includes my top " + str(len(movies)) + " favorite movies")

# Print full list
print(movies)

# Sorted version (temporary)
print(sorted(movies))

# Original list again
print(movies)

# Now sort permanently
movies.sort()
print(movies)

# Add a new movie
movies.append("Interstellar")

print("Updated list has " + str(len(movies)) + " movies")
print(movies)