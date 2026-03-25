import torch
from typing import Tuple

class ImageInfo:
    """
    Node for getting width, height, and batch size from an Image.
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
    
    def get_info(self, image: torch.Tensor) -> Tuple[int, int, int]:
        # ComfyUI image tensor format: [B, H, W, C]
        batch_size = image.shape[0] if len(image.shape) > 0 else 0
        height = image.shape[1] if len(image.shape) > 1 else 0
        width = image.shape[2] if len(image.shape) > 2 else 0
        
        return (width, height, batch_size)

class ImageBatchSlicer:
    """
    Slices a batch of images to extract a specific range or single image.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "index": ("INT", {"default": 0, "min": 0, "max": 1000}),
                "count": ("INT", {"default": 1, "min": 1, "max": 1000}),
            }
        }
    
    RETURN_TYPES = ("IMAGE", "INT")
    RETURN_NAMES = ("sliced_images", "count")
    FUNCTION = "slice_batch"
    CATEGORY = "DebugPadawan/Image"

    def slice_batch(self, images: torch.Tensor, index: int, count: int) -> Tuple[torch.Tensor, int]:
        num_images = images.shape[0]
        start_idx = min(index, num_images - 1)
        end_idx = min(start_idx + count, num_images)
        
        sliced = images[start_idx:end_idx]
        return (sliced, sliced.shape[0])

NODE_CLASS_MAPPINGS = {
    "DebugPadawan_ImageInfo": ImageInfo,
    "DebugPadawan_ImageBatchSlicer": ImageBatchSlicer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_ImageInfo": "Image Dimensions Info",
    "DebugPadawan_ImageBatchSlicer": "Image Batch Slicer",
}
