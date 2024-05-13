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
    cv2.namedWindow("Image Slideshow", cv2.WINDOW_NORMAL)
    #cv2.resizeWindow("Image Slideshow", 400, 300)

    while True:  # Loop indefinitely
        for image_file in image_files:
            # Read the image
            print(f"image file = {image_file}")
            image_path = os.path.join(directory, image_file)
            try:
                image = cv2.imread(image_path)

                if image is None:
                    print(f"Error: Unable to read image '{image_path}'")
                    continue

                # Display the image
                cv2.imshow("My Aurora Forecast", image)
                cv2.waitKey(50)  # Display each image for 1 second

            except Exception as e:
                print(f"Error: {e}")

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
                break

    # Close the window
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Directory containing JPG files
    directory =  "./downloaded_files/"
    play_images(directory)
