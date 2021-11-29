import matplotlib.pyplot as plt
import random
import numpy as np

class Taco:
    def __init__(self,
                cp_vertical=0.25,
                cp_horizontal=0.25,
                max_tw_vertical=100,
                min_tw_vertical=20,
                max_tw_horizontal=50,
                min_tw_horizontal=10
                ):
        """
        -: Creating Taco object and setting up parameters:-

        -------Arguments--------
        :cp_vertical:        corruption probability of vertical tiles
        :cp_horizontal:      corruption probability for horizontal tiles
        :max_tw_vertical:    maximum possible tile width for vertical tiles in pixels
        :min_tw_vertical:    minimum tile width for vertical tiles in pixels
        :max_tw_horizontal:  maximum possible tile width for horizontal tiles in pixels
        :min_tw_horizontal:  minimum tile width for horizontal tiles in pixels

        """
        self.corruption_probability_vertical = cp_vertical
        self.corruption_probability_horizontal = cp_horizontal
        self.max_tile_width_vertical = max_tw_vertical
        self.min_tile_width_vertical = min_tw_vertical
        self.max_tile_width_horizontal = max_tw_horizontal
        self.min_tile_width_horizontal = min_tw_horizontal

    def apply_vertical_taco(self, image, corruption_type='random'):
        """
        Only applies taco augmentations in vertical direction.
        Default corruption type is 'random', other supported types are [black, white, mean].

        -------Arguments-------
        :image:            A gray scaled input image that needs to be augmented.
        :corruption_type:  Type of corruption needs to be applied [one of- black, white, random or mean]

        -------Returns--------
        A TACO augmented image.

        """
        if len(image.shape) < 2 or len(image.shape) > 3:
            raise Exception("Input image with Invalid Shape!")

        if len(image.shape) == 3:
            raise Exception("Only Gray Scale Images are supported!")

        img_h, img_w = image.shape[0], image.shape[1]

        image = self._do_taco(image, img_h, img_w,
                                        self.min_tile_width_vertical,
                                        self.max_tile_width_vertical,
                                        orientation='vertical',
                                        corruption_type=corruption_type)

        return image

    def apply_horizontal_taco(self, image, corruption_type='random'):
        """
        Only applies taco augmentations in horizontal direction.
        Default corruption type is 'random', other supported types are [black, white, mean].

        -------Arguments-------
        :image:            A gray scaled input image that needs to be augmented.
        :corruption_type:  Type of corruption needs to be applied [one of- black, white, random or mean]

        -------Returns--------
        A TACO augmented image.

        """
        if len(image.shape) < 2 or len(image.shape) > 3:
            raise Exception("Input image with Invalid Shape!")

        if len(image.shape) == 3:
            raise Exception("Only Gray Scale Images are supported!")

        img_h, img_w = image.shape[0], image.shape[1]

        image = self._do_taco(image, img_h, img_w,
                                        self.min_tile_width_horizontal,
                                        self.max_tile_width_horizontal,
                                        orientation='horizontal',
                                        corruption_type=corruption_type)

        return image

    def apply_taco(self, image, corruption_type='random'):
        """
        Applies taco augmentations in both directions (vertical and horizontal).
        Default corruption type is 'random', other supported types are [black, white, mean].

        -------Arguments-------
        :image:            A gray scaled input image that needs to be augmented.
        :corruption_type:  Type of corruption needs to be applied [one of- black, white, random or mean]

        -------Returns--------
        A TACO augmented image.

        """
        image = self.apply_vertical_taco(image, corruption_type)
        image = self.apply_horizontal_taco(image, corruption_type)

        return image

    def visualize(self, image, title='example_image'):
        """
        A function to display images with given title.
        """
        plt.figure(figsize=(5, 2))
        plt.imshow(image, cmap='gray')
        plt.title(title)
        plt.tight_layout()
        plt.show()

    def _do_taco(self, image, img_h, img_w, min_tw, max_tw, orientation, corruption_type):
        """
        apply taco algorithm on image and return augmented image.
        """
        if orientation =='vertical':
            tiles = []
            start = 0
            tile_width = random.randint(min_tw, max_tw)
            while start < (img_w - 1):
                tile = image[:,start:start+min(img_w-start-1,tile_width)]
                if random.random() <= self.corruption_probability_vertical:
                    tile = self._corrupted_tile(tile, corruption_type)
                tiles.append(tile)
                start = start + tile_width
            augmented_image = np.hstack(tiles)
        else:
            tiles = []
            start = 0
            tile_width = random.randint(min_tw, max_tw)
            while start < (img_h - 1):
                tile = image[start:start+min(img_h-start-1,tile_width), :]
                if random.random() <= self.corruption_probability_vertical:
                    tile = self._corrupted_tile(tile, corruption_type)
                tiles.append(tile)
                start = start + tile_width
            augmented_image = np.vstack(tiles)
        return augmented_image

    def _corrupted_tile(self, tile, corruption_type):
        """
        Return a corrupted tile with given shape and corruption type.
        """
        tile_shape = tile.shape
        if corruption_type == 'random':
            corrupted_tile = np.random.random(tile_shape)*255
        if corruption_type == 'white':
            corrupted_tile = np.ones(tile_shape)*255
        if corruption_type == 'black':
            corrupted_tile = np.zeros(tile_shape)
        if corruption_type == 'mean':
            corrupted_tile = np.ones(tile_shape)*np.mean(tile)
        return corrupted_tile
