from flask import Flask, jsonify

def merge_sort(videos):
    if len(videos) <= 1:
        return videos

    mid = len(videos) // 2
    left_half = merge_sort(videos[:mid])
    right_half = merge_sort(videos[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0] <= right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))

    sorted_list.extend(left if left else right)
    return sorted_list

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

@app.route('/api/sorted-videos', methods=['GET'])
def get_sorted_videos():
    sorted_videos = merge_sort(video_titles.copy())
    return jsonify({"sorted_videos": sorted_videos})

if __name__ == '__main__':
    app.run(debug=True)
