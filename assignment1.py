from flask import Flask, request, jsonify

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

video_titles.sort()

def binary_search(video_titles, query):
    low, high = 0, len(video_titles) - 1
    while low <= high:
        mid = (low + high) // 2
        if video_titles[mid] == query:
            return mid
        elif video_titles[mid] < query:
            low = mid + 1
        else:
            high = mid - 1
    return -1


@app.route('/search', methods=['GET'])
def search_videos():
    query = request.args.get('title')
    if not query:
        return jsonify({"error": "Title query parameter is required"}), 400

    index = binary_search(video_titles, query)
    if index != -1:
        return jsonify({"title": video_titles[index]})
    else:
        return jsonify({"message": "Video not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
