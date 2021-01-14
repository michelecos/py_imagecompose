# Py_imagecompose

## What is it?

It is a tool for patching a face into an other. We use OpenCV to match the orientation,
and the size of face features. The gamma of the two different images is also taken into
account. Colors are matched, to compensate for different color dominants.
Our algorythm can stretch to the point that a color image is transformed to black and white
for color matching.