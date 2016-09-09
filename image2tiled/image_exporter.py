import math
from PIL import Image


class ImageExporter:
    def create(self, images, tiles_per_row):
        assert images, "Writing an empty array of images is invalid"
        width = images[0].width
        height = images[0].height
        num_columns = min(len(images), tiles_per_row)
        num_rows = int(math.ceil(len(images) / float(num_columns)))

        final_image = Image.new("RGBA", (num_columns * width, num_rows * height))

        current_row = 0
        current_column = 0
        for image in images:
            if current_column >= tiles_per_row:
                current_row += 1
                current_column = 0
            final_image.paste(image, (current_column * width, current_row * height,
                                       (current_column + 1) * width, (current_row + 1) * height))
            current_column += 1

        return final_image
