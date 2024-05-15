import os
import cv2

def play_images(directory):
    # Get a list of all JPG files in the directory
    image_files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
    # Sort the files to ensure consistent order
    image_files.sort()

    if not image_files:
        print("No JPG files found in the directory.")
        return

    # Create a window to display the images
    cv2.namedWindow("My Solar Wind Forecast", cv2.WINDOW_NORMAL)

    # Callback function for the trackbar
    def on_trackbar(val):
        nonlocal idx
        idx = val
        user_interacted = True  # Ensure user interaction is acknowledged

        # Display the image corresponding to the new index
        image_file = image_files[idx]
        image_path = os.path.join(directory, image_file)
        print(f"Displaying image {idx + 1}/{len(image_files)}: {image_file}")

        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Unable to read image '{image_path}'")
            return

        # Display the image
        cv2.imshow("My Solar Wind Forecast", image)

    # Initial setup for playback control
    idx = 0  # Start from the first image
    delay = 50  # Delay in ms between frames
    paused = False

    # Add a trackbar to the window
    cv2.createTrackbar('Frame', 'My Solar Wind Forecast', 0, len(image_files) - 1, on_trackbar)

    while True:
        if not paused:
            idx = (idx + 1) % len(image_files)

        image_file = image_files[idx]
        image_path = os.path.join(directory, image_file)
        print(f"Displaying image {idx + 1}/{len(image_files)}: {image_file}")

        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Unable to read image '{image_path}'")
            continue

        # Display the image
        cv2.imshow("My Solar Wind Forecast", image)
        
        # Set the trackbar position to current index
        cv2.setTrackbarPos('Frame', 'My Solar Wind Forecast', idx)

        key = cv2.waitKey(delay) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('p'):  # Press 'p' to pause or resume
            paused = not paused

    # Close the window when done
    cv2.destroyAllWindows()

if __name__ == "__main__":
    directory = "./downloaded_enlil_files/"  # Specify your directory
    play_images(directory)
