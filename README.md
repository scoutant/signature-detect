# Simple photo signature watermark detection using PyTorch CRAFT text detector

![photo with signature](data/photologo-1-1.jpg)


## Text detection

![times square](data/times-square_text_detection.png)


## CRAFT detector

Paper _Character Region Awareness for Text Detection_, 2019, https://arxiv.org/abs/1904.01941

For Python we can use this PyTorch implementation : https://github.com/fcakyon/craft-text-detector

Installation cannot be simpler :

    pip install __craft-text-detector__

Instanciate the engine:

    craft = __Craft__(output_dir='output', crop_type="box")

And run the detection:

    result = craft.__detect_text__([ image])

The result holds a list of bounding boxes for the detected text regions 

## Telling signature text from text in the wild
You may come up with a more advanced solution. For the moment we can use a simple region-based decision.

We state that a signature most often is located in a corner. Or at top or bottom of the image. You may refer [Where do I place my watermark](https://photologo.co/where-do-i-place-my-watermark).

![detection](data/photologo-1-1_boundaries.png)

We can traverse the list of text bounding boxes. And if any of them happen to be completely inside the mask we consider it to be a signature...

<p align="center">
  <img src="data/lukeman-boundaries.jpg">
</p>


