import os
from PIL import Image, ImageOps


class FakeSegmenter:
    """
    Simple class to represent a MRI segmentation model.

    Args:
        use_gpu: bool to indicate if GPU will be used.
    """

    def __init__(self, use_gpu: bool = False) -> None:
        self.use_gpu = use_gpu

    def _is_image(self, filename: str) -> bool:
        """Filter files by selected extensions."""
        lower = filename.lower()
        extensions = (
            '.png',
            '.jpg',
            '.jpeg',
            '.tif',
            '.tiff',
            '.bmp',
        )

        return lower.endswith(extensions)

    def segment(self, input_dir: str, output_dir: str) -> None:
        """Fake function to simulate a image segmentation."""
        os.makedirs(name=output_dir, exist_ok=True)

        if not os.path.isdir(input_dir):
            raise FileNotFoundError('Input path does not exist.')

        for fname in sorted(os.listdir(input_dir)):  # Iterate over each image.
            if not self._is_image(filename=fname):
                continue

            in_path = os.path.join(input_dir, fname)
            out_path = os.path.join(output_dir, fname)

            try:
                img = Image.open(in_path).convert('L')  # Grayscale.
                inverted = ImageOps.invert(img)
                mask = inverted.point(lambda p: 255 if p > 128 else 0) # type: ignore
                mask.save(out_path)
            except Exception as e:
                print(f'[WARN] Fail to process {in_path}: {e}')
