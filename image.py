import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from collections import Counter
import os
import webcolors
from PIL import Image
import io
def rgb_to_hex(rgb_color):
    hex_color = "#"
    for channel in rgb_color:
        hex_color += f"{int(channel):02x}"
    return hex_color
def get_color_name(rgb_color):
    try:
        color_name = webcolors.rgb_to_name(rgb_color)
    except ValueError:
        min_distance = float('inf')
        closest_color = None
        for name, rgb in webcolors.CSS3_HEX_TO_NAMES.items():
            css_rgb = webcolors.hex_to_rgb(name)
            distance = sum((a - b) ** 2 for a, b in zip(rgb_color, css_rgb))
            if distance < min_distance:
                min_distance = distance
                closest_color = webcolors.CSS3_HEX_TO_NAMES[name]
        color_name = closest_color
    return color_name
def process_image(image_path, num_colors=5):
    if isinstance(image_path, bytes):
        image = cv2.imdecode(np.frombuffer(image_path, np.uint8), cv2.IMREAD_COLOR)
    else:
        image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    height, width = image.shape[:2]
    max_dim = 500
    scale = max_dim / max(height, width)
    resized_image = cv2.resize(image, (int(width * scale), int(height * scale)), interpolation=cv2.INTER_AREA)
    pixel_list = resized_image.reshape((-1, 3))
    kmeans = KMeans(n_clusters=num_colors, n_init=10)
    kmeans.fit(pixel_list)
    counts = Counter(kmeans.labels_)
    total_pixels = sum(counts.values())
    sorted_colors = sorted([(count, color) for color, count in zip(kmeans.cluster_centers_, counts.values())], 
                          key=lambda x: x[0], reverse=True)
    results = []
    for count, color in sorted_colors:
        percentage = (count / total_pixels) * 100
        hex_color = rgb_to_hex(color)
        color_name = get_color_name(tuple(map(int, color)))
        results.append({
            'rgb': tuple(map(int, color)),
            'hex': hex_color,
            'name': color_name,
            'percentage': round(percentage, 2)
        }) 
    return results
def display_results(results):
    print("\nDominant Colors in the Image:")
    print("-" * 40)
    for idx, color in enumerate(results, 1):
        print(f"{idx}. Color: {color['name']}")
        print(f"   RGB: {color['rgb']}")
        print(f"   HEX: {color['hex']}")
        print(f"   Percentage: {color['percentage']}%")
        print("-" * 40)
def plot_colors(results):
    colors = [color['hex'] for color in results]
    percentages = [color['percentage'] for color in results]
    labels = [f"{color['name']}\n{color['percentage']}%" for color in results]  
    plt.figure(figsize=(8, 6))
    plt.pie(percentages, labels=labels, colors=colors, startangle=90)
    plt.axis('equal')
    plt.title('Dominant Colors Distribution')
    plt.show()
def main():
    print("Image Dominant Color Detector")
    print("=" * 30)    
    while True:
        print("\nOptions:")
        print("1. Upload an image file")
        print("2. Enter image path")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '3':
            print("Exiting program...")
            break   
        if choice in ('1', '2'):
            try:
                if choice == '1':
                    print("\nPlease upload an image file:")
                    file_path = input("Drag and drop your image file here or enter the path: ").strip('"')
                else:
                    file_path = input("\nEnter the path to your image file: ").strip('"')
                if not os.path.exists(file_path):
                    print("Error: File not found. Please try again.")
                    continue
                with open(file_path, 'rb') as f:
                    image_bytes = f.read()
                results = process_image(image_bytes)
                display_results(results)
                plot_colors(results)  
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                continue
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
