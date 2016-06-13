from skimage import data, io, segmentation, color
from skimage.future import graph
from matplotlib import pyplot as plt
import os


filename = 'leggies.jpg'
# filename = os.path.join(data_dir, "./data/source/template_match_chrome.png")
# filename = "template_match_chrome.png"
img = io.imread(filename)
# img = data.coffee()
# img = io.imread('http://scikit-image.org/_static/img/logo.png')

labels1 = segmentation.slic(img, compactness=30, n_segments=400)
out1 = color.label2rgb(labels1, img, kind='avg')

g = graph.rag_mean_color(img, labels1)
labels2 = graph.cut_threshold(labels1, g, 29)
out2 = color.label2rgb(labels2, img, kind='avg')

plt.figure()
io.imshow(out1)
plt.figure()
io.imshow(out2)
io.show()
