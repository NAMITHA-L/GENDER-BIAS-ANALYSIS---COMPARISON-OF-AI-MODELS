from collections import Counter
import matplotlib.pyplot as plt

def draw_bias_bar_chart(tags):
    if not tags:
        print("⚠️ No bias tags found. Skipping chart generation.")
        return  # Prevent crash if list is empty

    # Count occurrences of each bias type
    tag_counts = Counter(tags)
    tags, counts = zip(*sorted(tag_counts.items(), key=lambda x: x[1], reverse=True))  # Sort by count descending

    # Generate horizontal bar chart
    plt.figure(figsize=(10, 6))
    bars = plt.barh(tags, counts, color='salmon')
    plt.xlabel("Number of Biased Mentions")
    plt.title("Gender Bias Types Detected in Movie Plot")

    # Add count labels on bars
    for bar in bars:
        plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, str(int(bar.get_width())), va='center')

    plt.tight_layout()
    plt.savefig("bias_distribution.png")
    plt.close()
