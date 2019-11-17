
def overlay(base_image, adding_image, top, left):
    """
    Overlay image
    Args
        base_image (numpy-array): input base image
        adding_image (numpy-array): input adding image
        top (int): start y axis of adding image
        left (int): start x axis of adding image
    Return
        image (numpy): original image
    """
    height, width = adding_image.shape[:2]
    base_image[top:height + top, left:width+left] = adding_image

    return base_image
