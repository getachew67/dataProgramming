# 1664741

import cse163_utils  # noqa: F401
import numpy as np
import matplotlib.pyplot as plt


def invert_colors(image):
    """
    Returns a new color image whose colors have been inverted
    from the given color image(3-d numpy array)
    """
    x, y, z = image.shape
    img = np.zeros((x, y, z))
    img[:, :, 0] = 255 - image[:, :, 0]
    img[:, :, 1] = 255 - image[:, :, 1]
    img[:, :, 2] = 255 - image[:, :, 2]
    return img


def blur(gray_image, patch_size):
    """
    Returns a new image that has been blurred from the given gray image
    with the given patch size
    """
    kernel = np.ones((patch_size, patch_size)) * (1/(patch_size**2))
    height, width = gray_image.shape
    result = np.zeros((height - (patch_size - 1), width - (patch_size - 1)))
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            curr = gray_image[i:i+patch_size, j:j+patch_size]
            result[i, j] = np.sum(curr * kernel)
    return result.astype(np.uint8)


def template_match(image, template):
    """
    Returns a 2-d numpy array of the similarity between
    the given template(2-d numpy array) at each point in the given gray
    image(2-d numpy array).
    """
    height, width = image.shape
    x, y = template.shape
    avg = np.sum(template)/(x*y)
    template = template - avg
    result = np.zeros((height - (x - 1), width - (y - 1)))
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            curr = image[i:i+x, j:j+y]
            curr_avg = np.sum(curr)/(x*y)
            curr = curr - curr_avg
            result[i, j] = np.sum(curr * template)
    return result


def find_xy(result):
    """
    Given the result of template_match, finds the position (x, y) with
    the highest similarity.
    """
    ij = np.unravel_index(np.argmax(result), result.shape)
    return ij[::-1]


def plot_result(image, template, result):
    """
    Given an image, a template, and the result of
    template_match(image, template), makes a plot showing the result
    of the match.
    """
    x, y = find_xy(result)

    plt.figure(figsize=(8, 3))
    ax1 = plt.subplot(1, 3, 1)
    ax2 = plt.subplot(1, 3, 2)
    ax3 = plt.subplot(1, 3, 3, sharex=ax2, sharey=ax2)

    ax1.imshow(template, cmap=plt.cm.gray)
    ax1.set_axis_off()
    ax1.set_title('template')

    ax2.imshow(image, cmap=plt.cm.gray)
    ax2.set_axis_off()
    ax2.set_title('image')
    # highlight matched region
    template_height,  template_width = template.shape
    rect = plt.Rectangle((x, y), template_width, template_height,
                         edgecolor='r', facecolor='none')
    ax2.add_patch(rect)

    ax3.imshow(result)
    ax3.set_axis_off()
    ax3.set_title('`match_template`\nresult')
    # highlight matched region
    ax3.autoscale(False)
    ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none',
             markersize=10)
    plt.show()
