# PDI-MVRC
PDI - Marine Vision Restoration Challenge (MVRC). 


## To-do
[ ] - metrics

[ ] - first enhancement model

[ ] - first detection model

## Image Resizing with Padding

This project implements two methods to standardize image dimensions within a dataset using padding. One method adds mirrored borders (reflection), while the other uses black padding, allowing images to be resized to predefined dimensions without distortion.

1. **Padding with mirrored borders**  
   - Main function:
     - `pad_image_with_mirror`: Adds reflected borders to images, ensuring a smooth transition at the edges when resizing to larger dimensions.

2. **Padding with black borders**  
   - Main function:
     - `pad_image_with_black`: Adds black padding to images, creating uniform borders when resizing.

Both scripts use the following functions to process image directories:

- **`process_dataset`**:  
  Processes all images in a directory, applying the selected padding method (mirrored or black) and saving the adjusted images to an output directory.

- **`process_multiple_directories`**:  
  Traverses a directory structure, identifies image folders to be processed, and calls `process_dataset` to apply padding according to the dimensions defined for each folder.

These functions rely on the [`os`](https://docs.python.org/3/library/os.html), [`cv2`](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) (OpenCV), and [`tqdm`](https://tqdm.github.io) libraries for file manipulation, image processing, and progress visualization.
