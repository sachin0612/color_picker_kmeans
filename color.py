import streamlit as st
from PIL import Image, ImageDraw
import numpy as np
from sklearn.cluster import KMeans
def main():
    st.title("Majority Color Picking From the Image using KMeans Clustering")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("")
        X=np.array(image).reshape(-1,3)
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(X) 
        y=create_color_palette(kmeans.cluster_centers_.astype(int))   
        st.title("Top 3 used colors are: ")
        st.image(y)


def create_color_palette(dominant_colors, palette_size=(300, 50)):
    # Create an image to display the colors
    palette = Image.new("RGB", palette_size)
    draw = ImageDraw.Draw(palette)

    # Calculate the width of each color swatch
    swatch_width = palette_size[0] // len(dominant_colors)

    # Draw each color as a rectangle on the palette
    for i, color in enumerate(dominant_colors):
        draw.rectangle([i * swatch_width, 0, (i + 1) * swatch_width, palette_size[1]], fill=tuple(color))

    return palette
if __name__ == "__main__":
    main()
