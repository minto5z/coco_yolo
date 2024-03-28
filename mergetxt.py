import os


def create_image_list(image_dir, output_file):
    with open(output_file, 'w') as f:
        for root, _, files in os.walk(image_dir):
            for file in files:
                if file.endswith('.jpg'):
                    image_path = os.path.join(root, file)
                    f.write(image_path + '\n')
    print(f"Created {output_file} with paths to all images.")

if __name__ == "__main__":
    image_directory = './datasets/coco/images/val2017'
    output_file = 'coco/val2017.txt'
    create_image_list(image_directory, output_file)