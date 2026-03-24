import numpy as np
import torch

class ColorPaletteExtractor:
    """
    Node for extracting the most dominant colors from an image
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

    def extract(self, image, color_count):
        # Image is typically [B, H, W, C]
        # We'll take the first image in the batch
        img = image[0]
        h, w, c = img.shape
        
        # Rescale for performance using torch
        img_torch = img.permute(2, 0, 1).unsqueeze(0)  # [1, C, H, W]
        img_small = torch.nn.functional.interpolate(img_torch, size=(128, 128), mode='area')
        img_np = img_small.squeeze(0).permute(1, 2, 0).numpy()
        
        # Flatten and scale to 0-255
        pixels = img_np.reshape(-1, c) * 255.0
        
        # Simple quantization
        pixels = (pixels / 16).astype(int) * 16
        
        # Convert to hex strings
        hex_colors = []
        for p in pixels:
            r, g, b = p
            hex_colors.append(f'#{r:02x}{g:02x}{b:02x}')
            
        # Count frequencies
        unique, counts = np.unique(hex_colors, return_counts=True)
        sorted_indices = np.argsort(-counts)
        
        top_hex = unique[sorted_indices[:color_count]]
        dominant = top_hex[0] if len(top_hex) > 0 else "#000000"
        
        # Create a palette image
        palette_h = 64
        palette_w = color_count * 64
        palette_img = np.zeros((palette_h, palette_w, 3), dtype=np.float32)
        
        for i, hex_color in enumerate(top_hex):
            r = int(hex_color[1:3], 16) / 255.0
            g = int(hex_color[3:5], 16) / 255.0
            b = int(hex_color[5:7], 16) / 255.0
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
