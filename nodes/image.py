class ImageInfo:
    """
    Node for getting width, height, and batch size from an Image
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }
    
    RETURN_TYPES = ("INT", "INT", "INT")
    RETURN_NAMES = ("width", "height", "batch_size")
    
    FUNCTION = "get_info"
    CATEGORY = "DebugPadawan/Image"
    
    def get_info(self, image):
        """
        Extract dimensions from a ComfyUI image tensor
        ComfyUI images are formatted as [batch_size, height, width, channels]
        """
        batch_size = image.shape[0]
        height = image.shape[1]
        width = image.shape[2]
        
        return (width, height, batch_size)

NODE_CLASS_MAPPINGS = {
    "DebugPadawan_ImageInfo": ImageInfo,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_ImageInfo": "Image Info",
}
