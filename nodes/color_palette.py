import numpy as np
import torch
from typing import Tuple

class ColorPaletteExtractor:
    """
    Node for extracting the most dominant colors from an image.
    Uses quantization and frequency analysis for speed and accuracy.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "color_count": ("INT", {"default": 5, "min": 1, "max": 20}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING", "IMAGE")
    RETURN_NAMES = ("hex_list", "dominant_color", "palette_image")
    FUNCTION = "extract"
    CATEGORY = "DebugPadawan/Image"

    def extract(self, image: torch.Tensor, color_count: int) -> Tuple[str, str, torch.Tensor]:
        # Image is typically [B, H, W, C]
        # We'll take the first image in the batch for analysis
        img = image[0]
        c = img.shape[-1]
        
        # Rescale for performance using torch
        img_torch = img.permute(2, 0, 1).unsqueeze(0)  # [1, C, H, W]
        # Using a smaller size for faster processing
        img_small = torch.nn.functional.interpolate(img_torch, size=(64, 64), mode='area')
        img_np = img_small.squeeze(0).permute(1, 2, 0).cpu().numpy()
        
        # Flatten and scale to 0-255
        pixels = (img_np.reshape(-1, c) * 255.0).astype(np.int32)
        
        # Simple quantization (group colors together)
        # We group by 16 levels to reduce noise
        pixels = (pixels // 16) * 16
        
        # Map each pixel to a unique integer color representation (R << 16 | G << 8 | B)
        # This is much faster than string formatting for all pixels
        rgb_int = (pixels[:, 0] << 16) | (pixels[:, 1] << 8) | pixels[:, 2]
            
        # Count frequencies
        unique, counts = np.unique(rgb_int, return_counts=True)
        sorted_indices = np.argsort(-counts)
        
        top_colors = unique[sorted_indices[:color_count]]
        
        def int_to_hex(val):
             return f"#{val >> 16 & 0xFF:02x}{val >> 8 & 0xFF:02x}{val & 0xFF:02x}"
             
        top_hex = [int_to_hex(c) for c in top_colors]
        dominant = top_hex[0] if top_hex else "#000000"
        
        # Create a visual palette image
        p_h, p_w = 64, color_count * 64
        palette_img = np.zeros((p_h, p_w, 3), dtype=np.float32)
        
        for i, val in enumerate(top_colors):
            r = ((val >> 16) & 0xFF) / 255.0
            g = ((val >> 8) & 0xFF) / 255.0
            b = (val & 0xFF) / 255.0
            palette_img[:, i*64:(i+1)*64, 0] = r
            palette_img[:, i*64:(i+1)*64, 1] = g
            palette_img[:, i*64:(i+1)*64, 2] = b
            
        palette_tensor = torch.from_numpy(palette_img).unsqueeze(0)
        
        return (", ".join(top_hex), dominant, palette_tensor)

NODE_CLASS_MAPPINGS = {
    "DebugPadawan_ColorPalette": ColorPaletteExtractor,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugPadawan_ColorPalette": "Color Palette Extractor",
}
