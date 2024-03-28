# This is a sample Python script.
import json
import os


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def coco_to_yolo(coco_annotations, image_dir, output_dir, classes):
    with open(coco_annotations, 'r') as f:
        coco_data = json.load(f)

    for image_data in coco_data['images']:
        image_id = image_data['id']
        image_filename = image_data['file_name']
        image_width = image_data['width']
        image_height = image_data['height']

        yolo_annotation_lines = []

        for annotation in coco_data['annotations']:
            if annotation['image_id'] == image_id:
                category_id = annotation['category_id']
                class_label = classes[0]

                bbox = annotation['bbox']
                x, y, width, height = bbox

                # Convert COCO bbox to YOLO format
                x_center = x + width / 2
                y_center = y + height / 2
                x_center /= image_width
                y_center /= image_height
                width /= image_width
                height /= image_height

                yolo_annotation_lines.append(f"{classes.index(class_label)} {x_center} {y_center} {width} {height}")

        if yolo_annotation_lines:
            output_filename = os.path.join(output_dir, os.path.splitext(image_filename)[0] + '.txt')
            with open(output_filename, 'w') as f:
                f.write('\n'.join(yolo_annotation_lines))
            print(f"Created YOLO annotation file for {image_filename}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Annotation file for training data
    coco_annotations_file = 'coco/annotations/instances_train2017.json'

    # Directory containing training images
    image_directory = 'train2017'

    # Output directory for YOLO annotations
    output_directory = 'yolo_train'

    # Class names (update with your actual class names)
    class_names = ['person']

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Convert COCO annotations to YOLO format for training set
    coco_to_yolo(coco_annotations_file, image_directory, output_directory, class_names)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
