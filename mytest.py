# TASK 1 DATA PARSING

import json # The json module in Python is used to work with JSON data and it's a popular format for representing structured data.

# JSON data (JavaScript Object Notation), it is defined as a multiline string. It contains two main arrays: users and videos.
data = '''
{
    "users": [
        {"user_id": 1, "name": "Alice Johnson", "watch_history": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]},
        {"user_id": 2, "name": "Bob Smith", "watch_history": [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]},
        {"user_id": 3, "name": "Carol Williams", "watch_history": [145, 146, 147, 148, 149, 150, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]},
        {"user_id": 4, "name": "David Brown", "watch_history": [115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134]},
        {"user_id": 5, "name": "Emma Davis", "watch_history": [135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 101, 102, 103, 104, 105, 106, 107, 108]},
        {"user_id": 6, "name": "Frank Miller", "watch_history": [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]},
        {"user_id": 7, "name": "Grace Wilson", "watch_history": [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]},
        {"user_id": 8, "name": "Henry Moore", "watch_history": [149, 150, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118]},
        {"user_id": 9, "name": "Isla Taylor", "watch_history": [119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]},
        {"user_id": 10, "name": "Jack Anderson", "watch_history": [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 101, 102, 103, 104, 105, 106, 107, 108]},
        {"user_id": 11, "name": "Karen Thomas", "watch_history": [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]},
        {"user_id": 12, "name": "Leo Jackson", "watch_history": [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]},
        {"user_id": 13, "name": "Mia White", "watch_history": [149, 150, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118]},
        {"user_id": 14, "name": "Noah Harris", "watch_history": [119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]},
        {"user_id": 15, "name": "Olivia Martin", "watch_history": [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 101, 102, 103, 104, 105, 106, 107, 108]},
        {"user_id": 16, "name": "Paul Martinez", "watch_history": [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]},
        {"user_id": 17, "name": "Quinn Lee", "watch_history": [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]},
        {"user_id": 18, "name": "Ruby Perez", "watch_history": [149, 150, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118]},
        {"user_id": 19, "name": "Sam Roberts", "watch_history": [119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]},
        {"user_id": 20, "name": "Tina Clark", "watch_history": [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 101, 102, 103, 104, 105, 106, 107, 108]}
    ],
    "videos": [
        {"video_id": 101, "title": "Introduction to Python", "category": "Education", "tags": ["python", "programming", "tutorial"], "duration": "15:32"},
        {"video_id": 102, "title": "Advanced Python Techniques", "category": "Education", "tags": ["python", "programming", "advanced"], "duration": "22:45"},
        {"video_id": 103, "title": "Python for Data Science", "category": "Education", "tags": ["python", "data science", "tutorial"], "duration": "19:56"},
        {"video_id": 104, "title": "Machine Learning Basics", "category": "Education", "tags": ["machine learning", "AI", "tutorial"], "duration": "25:11"},
        {"video_id": 105, "title": "Neural Networks Explained", "category": "Education", "tags": ["neural networks", "AI", "tutorial"], "duration": "28:34"},
        {"video_id": 106, "title": "Introduction to JavaScript", "category": "Education", "tags": ["javascript", "programming", "tutorial"], "duration": "14:20"},
        {"video_id": 107, "title": "Advanced JavaScript Concepts", "category": "Education", "tags": ["javascript", "programming", "advanced"], "duration": "20:31"},
        {"video_id": 108, "title": "React.js Fundamentals", "category": "Education", "tags": ["react", "javascript", "web development"], "duration": "23:45"},
        {"video_id": 109, "title": "Node.js Basics", "category": "Education", "tags": ["node.js", "javascript", "backend"], "duration": "16:30"},
        {"video_id": 110, "title": "Building REST APIs with Node.js", "category": "Education", "tags": ["node.js", "javascript", "web development"], "duration": "24:05"},
        {"video_id": 111, "title": "HTML & CSS Crash Course", "category": "Education", "tags": ["html", "css", "web development"], "duration": "12:44"},
        {"video_id": 112, "title": "CSS Grid Layout", "category": "Education", "tags": ["css", "web development", "design"], "duration": "18:22"},
        {"video_id": 113, "title": "Flexbox in CSS", "category": "Education", "tags": ["css", "web development", "design"], "duration": "15:55"},
        {"video_id": 114, "title": "Getting Started with Git", "category": "Education", "tags": ["git", "version control", "tutorial"], "duration": "10:37"},
        {"video_id": 115, "title": "Advanced Git Workflows", "category": "Education", "tags": ["git", "version control", "advanced"], "duration": "17:21"},
        {"video_id": 116, "title": "Introduction to Docker", "category": "Education", "tags": ["docker", "containerization", "tutorial"], "duration": "19:48"},
        {"video_id": 117, "title": "Kubernetes for Beginners", "category": "Education", "tags": ["kubernetes", "containerization", "tutorial"], "duration": "21:11"},
        {"video_id": 118, "title": "DevOps Essentials", "category": "Education", "tags": ["devops", "ci/cd", "tutorial"], "duration": "22:19"},
        {"video_id": 119, "title": "Introduction to SQL", "category": "Education", "tags": ["sql", "database", "tutorial"], "duration": "13:50"},
        {"video_id": 120, "title": "Advanced SQL Queries", "category": "Education", "tags": ["sql", "database", "advanced"], "duration": "17:45"},
        {"video_id": 121, "title": "Basic Cooking Techniques", "category": "Lifestyle", "tags": ["cooking", "basics", "tutorial"], "duration": "11:32"},
        {"video_id": 122, "title": "Gourmet Cooking at Home", "category": "Lifestyle", "tags": ["cooking", "gourmet", "advanced"], "duration": "24:13"},
        {"video_id": 123, "title": "30-Minute Meals", "category": "Lifestyle", "tags": ["cooking", "quick meals", "tutorial"], "duration": "20:10"},
        {"video_id": 124, "title": "Healthy Eating Tips", "category": "Lifestyle", "tags": ["health", "cooking", "tutorial"], "duration": "13:22"},
        {"video_id": 125, "title": "Yoga for Beginners", "category": "Lifestyle", "tags": ["yoga", "fitness", "tutorial"], "duration": "18:45"},
        {"video_id": 126, "title": "Advanced Yoga Practices", "category": "Lifestyle", "tags": ["yoga", "fitness", "advanced"], "duration": "22:50"},
        {"video_id": 127, "title": "Meditation Basics", "category": "Lifestyle", "tags": ["meditation", "wellness", "tutorial"], "duration": "15:40"},
        {"video_id": 128, "title": "Stress Management Techniques", "category": "Lifestyle", "tags": ["stress management", "wellness", "tutorial"], "duration": "17:55"},
        {"video_id": 129, "title": "Home Workout Routines", "category": "Lifestyle", "tags": ["fitness", "workout", "tutorial"], "duration": "20:00"},
        {"video_id": 130, "title": "Weight Loss Tips", "category": "Lifestyle", "tags": ["weight loss", "fitness", "tutorial"], "duration": "18:15"},
        {"video_id": 131, "title": "Running Tips for Beginners", "category": "Lifestyle", "tags": ["running", "fitness", "tutorial"], "duration": "16:50"},
        {"video_id": 132, "title": "Strength Training Basics", "category": "Lifestyle", "tags": ["strength training", "fitness", "tutorial"], "duration": "19:30"},
        {"video_id": 133, "title": "Advanced Strength Training", "category": "Lifestyle", "tags": ["strength training", "fitness", "advanced"], "duration": "21:22"},
        {"video_id": 134, "title": "Introduction to Gardening", "category": "Lifestyle", "tags": ["gardening", "basics", "tutorial"], "duration": "14:55"},
        {"video_id": 135, "title": "Organic Gardening Tips", "category": "Lifestyle", "tags": ["gardening", "organic", "tutorial"], "duration": "17:40"},
        {"video_id": 136, "title": "DIY Home Decor", "category": "Lifestyle", "tags": ["home decor", "DIY", "tutorial"], "duration": "15:05"},
        {"video_id": 137, "title": "Minimalist Living Tips", "category": "Lifestyle", "tags": ["minimalism", "lifestyle", "tutorial"], "duration": "12:55"},
        {"video_id": 138, "title": "Sustainable Living", "category": "Lifestyle", "tags": ["sustainability", "lifestyle", "tutorial"], "duration": "18:05"},
        {"video_id": 139, "title": "Personal Finance 101", "category": "Lifestyle", "tags": ["finance", "personal finance", "tutorial"], "duration": "19:20"},
        {"video_id": 140, "title": "Investing for Beginners", "category": "Lifestyle", "tags": ["investing", "finance", "tutorial"], "duration": "22:10"},
        {"video_id": 141, "title": "Retirement Planning", "category": "Lifestyle", "tags": ["retirement", "finance", "tutorial"], "duration": "21:55"},
        {"video_id": 142, "title": "Budgeting Tips", "category": "Lifestyle", "tags": ["budgeting", "finance", "tutorial"], "duration": "16:45"},
        {"video_id": 143, "title": "Credit Score Management", "category": "Lifestyle", "tags": ["credit score", "finance", "tutorial"], "duration": "14:30"},
        {"video_id": 144, "title": "Debt Reduction Strategies", "category": "Lifestyle", "tags": ["debt", "finance", "tutorial"], "duration": "20:25"},
        {"video_id": 145, "title": "Mindfulness Meditation", "category": "Lifestyle", "tags": ["mindfulness", "meditation", "tutorial"], "duration": "17:10"},
        {"video_id": 146, "title": "Self-Care Practices", "category": "Lifestyle", "tags": ["self-care", "wellness", "tutorial"], "duration": "14:35"},
        {"video_id": 147, "title": "Travel on a Budget", "category": "Lifestyle", "tags": ["travel", "budget", "tutorial"], "duration": "21:25"},
        {"video_id": 148, "title": "Cultural Travel Guide", "category": "Lifestyle", "tags": ["travel", "culture", "tutorial"], "duration": "23:30"},
        {"video_id": 149, "title": "Pet Care Basics", "category": "Lifestyle", "tags": ["pet care", "basics", "tutorial"], "duration": "13:20"},
        {"video_id": 150, "title": "Training Your Dog", "category": "Lifestyle", "tags": ["dog training", "pet care", "tutorial"], "duration": "18:45"}
    ]
}
'''
# The json.loads() function is used to parse the JSON string and convert it into a Python dictionary. 
# This dictionary (data_dict) will contain two keys: users and videos.
# From the parsed dictionary, the users and videos arrays are extracted and stored in separate variables.

data_dict = json.loads(data)
users = data_dict['users']
videos = data_dict['videos']





# TASK 2 SIMILARITY CALCULATION

from collections import defaultdict # For creating dictionaries with default values.
from sklearn.feature_extraction.text import TfidfVectorizer # To convert a collection of raw documents to a matrix of TF-IDF features.
from sklearn.metrics.pairwise import cosine_similarity # To compute cosine similarity between samples.
import numpy as np # A library for numerical computations. 

# Create a dictionary to store video metadata
# Creates a dictionary video_metadata where each key is a video_id and the value is the corresponding video metadata.
video_metadata = {video['video_id']: video for video in videos}

def compute_similarity(videos):
    vectorizer = TfidfVectorizer() # Converts text data into TF-IDF(Term Frequency-Inverse Document Frequency) features.
    video_tags = [" ".join(video['tags']) for video in videos] # For each video, it joins the tags into a single string, creating a list of tag strings.
    tfidf_matrix = vectorizer.fit_transform(video_tags) # The fit_transform method converts the list of tag strings into a TF-IDF matrix.
    cosine_sim = cosine_similarity(tfidf_matrix) # The cosine_similarity function computes the cosine similarity between rows of the TF-IDF matrix, producing a similarity matrix.
    return cosine_sim

# Compute similarity matrix for all videos
similarity_matrix = compute_similarity(videos) # calls the compute_similarity function and stores the resulting similarity matrix in similarity_matrix.





# TASK 3: RECOMMENDATION ALGORITHM

# Print the User Data
print(users[0])  # Print the first user's data to verify the structure and contents of the users list.


# Modify the Recommendation Function

# define the recommend_video function
def recommend_videos(user, similarity_matrix, video_metadata, n_recommendations=5): 
    # Check if 'watched' key exists
    if 'watched' not in user:
        print(f"User {user['user_id']} doesn't have a 'watched' key.")
        return []
    
    # Check if 'liked' key exists
    if 'liked' not in user:
        print(f"User {user['user_id']} doesn't have a 'liked' key.")
        return []
    
    watched_videos = user['watched']
    liked_videos = user['liked']
    
    # Aggregate watched and liked videos
    all_watched_liked = watched_videos + liked_videos
    
    # Find the indices in the videos list that correspond to the video IDs in the aggregated list.
    indices = [i for i, video in enumerate(videos) if video['video_id'] in all_watched_liked]
    
    # Compute the average similarity scores for all videos or Calculates similarity scores for all videos based on the similarity matrix.)
    similarity_scores = np.mean(similarity_matrix[indices], axis=0)
    
    # Sort the videos based on similarity scores and filters out already watched/liked videos in descending order)
    sorted_indices = np.argsort(similarity_scores)[::-1]
    
    # Get the top N recommendations excluding already watched/liked videos
    recommendations = []
    for idx in sorted_indices:
        video_id = videos[idx]['video_id']
        if video_id not in all_watched_liked:
            recommendations.append(video_metadata[video_id])
        if len(recommendations) >= n_recommendations:
            break
    
    return recommendations


# This section tests the recommend_videos function with the first user's data and prints the recommendations.

# Test the recommendation function
recommendations = recommend_videos(users[0], similarity_matrix, video_metadata)

# Print recommendations for the first user
for rec in recommendations:
    print(f"Title: {rec['title']}, Category: {rec['category']}, Duration: {rec['duration']}")


# Check the User Data Structure 

# This section defines a list of user data, each with user_id, name, watched, and liked keys.
# This updated structure is necessary for the 'recommend_videos' function to work correctly.
users = [
    {"user_id": 1, "name": "Alice", "watched": [101, 102, 103], "liked": [104, 105]},
    {"user_id": 2, "name": "Bob", "watched": [106, 107, 108], "liked": [109, 110]},
    {"user_id": 3, "name": "Charlie", "watched": [111, 112, 113], "liked": [114, 115]}
]





# TASK 4: TOP-N RECOMMENDATIONS

# Define the Function
# Here's the function to get the top N recommended video IDs for a given user ID:

# 4A.

# Define the get_top_n_recommendations function
def get_top_n_recommendations(user_id, users, similarity_matrix, video_metadata, n_recommendations=5):
    # Find the user data based on user_id.
    user = next((u for u in users if u['user_id'] == user_id), None)
    if user is None:
        print(f"User with ID {user_id} not found.")
        return []
    
    # Calls the recommend_videos function to get recommendations.
    recommendations = recommend_videos(user, similarity_matrix, video_metadata, n_recommendations)
    
    # Extracts and returns the video IDs from the recommendations.
    recommended_video_ids = [rec['video_id'] for rec in recommendations]
    
    return recommended_video_ids


# 4B.

# Adjust the Recommendation Function

# Function recommend_videos or define the recommend_videos function

# Ensures that the user has both watched and liked keys.
# Aggregates the watched and liked videos.
# Computes similarity scores, sorts them, and filters out already watched/liked videos.
# Returns the top N recommended videos.

def recommend_videos(user, similarity_matrix, video_metadata, n_recommendations=5):
    # Check if 'watched' key exists
    if 'watched' not in user:
        print(f"User {user['user_id']} does not have a 'watched' key.")
        return []
    
    # Check if 'liked' key exists
    if 'liked' not in user:
        print(f"User {user['user_id']} does not have a 'liked' key.")
        return []
    
    watched_videos = user['watched']
    liked_videos = user['liked']
    
    # Aggregate watched and liked videos
    all_watched_liked = watched_videos + liked_videos
    
    # Get the indices of these videos
    indices = [i for i, video in enumerate(videos) if video['video_id'] in all_watched_liked]
    
    # Compute the average similarity scores for all videos
    similarity_scores = np.mean(similarity_matrix[indices], axis=0)
    
    # Sort the videos based on similarity scores
    sorted_indices = np.argsort(similarity_scores)[::-1]
    
    # Get the top N recommendations excluding already watched/liked videos
    recommendations = []
    for idx in sorted_indices:
        video_id = videos[idx]['video_id']
        if video_id not in all_watched_liked:
            recommendations.append(video_metadata[video_id])
        if len(recommendations) >= n_recommendations:
            break
    
    return recommendations


# 4C

# Sample Data: Defined sample users and video metadata.

# Sample user data
users = [
    {"user_id": 1, "name": "Alice", "watched": [101, 102, 103], "liked": [104, 105]},
    {"user_id": 2, "name": "Bob", "watched": [106, 107, 108], "liked": [109, 110]},
    {"user_id": 3, "name": "Charlie", "watched": [111, 112, 113], "liked": [114, 115]}
]

# Sample video metadata
video_metadata = {
    101: {"video_id": 101, "title": "Video A", "category": "Education", "duration": 10},
    102: {"video_id": 102, "title": "Video B", "category": "Entertainment", "duration": 15},
    103: {"video_id": 103, "title": "Video C", "category": "Education", "duration": 12},
    104: {"video_id": 104, "title": "Video D", "category": "Music", "duration": 20},
    105: {"video_id": 105, "title": "Video E", "category": "Music", "duration": 25},
    106: {"video_id": 106, "title": "Video F", "category": "Sports", "duration": 30},
    107: {"video_id": 107, "title": "Video G", "category": "Entertainment", "duration": 35},
    108: {"video_id": 108, "title": "Video H", "category": "Education", "duration": 40},
    109: {"video_id": 109, "title": "Video I", "category": "Education", "duration": 45},
    110: {"video_id": 110, "title": "Video J", "category": "Music", "duration": 50},
    111: {"video_id": 111, "title": "Video K", "category": "Music", "duration": 55},
    112: {"video_id": 112, "title": "Video L", "category": "Sports", "duration": 60},
    113: {"video_id": 113, "title": "Video M", "category": "Entertainment", "duration": 65},
    114: {"video_id": 114, "title": "Video N", "category": "Education", "duration": 70},
    115: {"video_id": 115, "title": "Video O", "category": "Music", "duration": 75}
}

# Created a random similarity matrix for demonstration.
similarity_matrix = np.random.rand(len(video_metadata), len(video_metadata))

# Test for user_id 1
# Ran the function and printed the top N recommendations for user ID 1
top_n_recommendations = get_top_n_recommendations(1, users, similarity_matrix, video_metadata, n_recommendations=5)

print("Top N Recommendations for User ID 1:")
for video_id in top_n_recommendations:
    print(f"Video ID: {video_id}, Title: {video_metadata[video_id]['title']}")
