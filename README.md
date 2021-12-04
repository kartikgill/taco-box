# Tiling and Corruption (TACo)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)  [![PyPI](https://img.shields.io/pypi/v/tsai?color=blue&label=pypi%20version)](https://pypi.org/project/taco-box/0.1.1/#description)  ![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg) 

`TACo` is a simple and effective data augmentation technique for the task of Optical Character Recognition (`OCR`) or Handwritten Text Recognition (`HTR`) (check reference).

And, `taco-box` is an implementation of `TACo` algorithm. This is currently under the Apache 2.0, Please feel free to use for your project. Enjoy!

## Installing
First, you need to have `python 3` installed in your system.

Next, you can Install `taco-box` with `pip` or your favorite PyPi package manager.

```bash
pip install taco-box
```

## Usage
Checkout this jupyter notebook on usage - [Notebook](https://github.com/kartikgill/taco-box/blob/main/tests/Taco_testing.ipynb)

Here is an example:

```python
from tacobox import Taco

# creating Taco object. (Note: parameters are at their default value.)
mytaco = Taco(cp_vertical=0.25,
                cp_horizontal=0.25,
                max_tw_vertical=100,
                min_tw_vertical=20,
                max_tw_horizontal=50,
                min_tw_horizontal=10
                )

# apply random vertical corruption
augmented_img = mytaco.apply_vertical_taco(input_img, corruption_type='random')
mytaco.visualize(augmented_img)
```

        -------Understanding Arguments--------
        :cp_vertical:        corruption probability of vertical tiles
        :cp_horizontal:      corruption probability for horizontal tiles
        :max_tw_vertical:    maximum possible tile width for vertical tiles in pixels
        :min_tw_vertical:    minimum tile width for vertical tiles in pixels
        :max_tw_horizontal:  maximum possible tile width for horizontal tiles in pixels
        :min_tw_horizontal:  minimum tile width for horizontal tiles in pixels

## Expected results
Below picture shows the variations of `TACo` augmentation algorithm from current implementation:-

<p align="center">
  <img src="https://github.com/kartikgill/taco-box/blob/main/images/taco_results.png" alt="Example Output"/ width=600>
</p>

## Contributing
This project is in very early stages of development. If there is an issue or feature request, feel free to open an issue. Additionally, a PR is always welcome.

## Reference
TACo algorithm is part of a research project on Handwritten Text Recognition. Link to the original paper will be posted soon!!
