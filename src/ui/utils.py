from PyQt5 import QtGui
import io
import os
import shutil
from PIL import Image, ImageCms


def getFont(font_weight, font_size):
    """Get font from assets"""
    # Set the path to the font file based on the type
    font_path = f"assets/fonts/poppins/Poppins-{font_weight}.ttf"

    # Add the font to the application
    font_id = QtGui.QFontDatabase.addApplicationFont(font_path)

    # Get the font family name
    font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]

    # Create a QFont object using the font
    font = QtGui.QFont(font_family)

    # Set the font size
    font.setPointSize(font_size)
    if (font_weight == "Bold"):
        font.setWeight(75)

    return font


def convert_icc_to_icc_srgb(image_path):
    """Convert PIL image to sRGB color space (if possible and if image is in other ICC profiles)"""
    img = Image.open(image_path)
    icc = img.info.get('icc_profile', '')
    if icc:
        io_handle = io.BytesIO(icc)     # virtual file
        src_profile = ImageCms.ImageCmsProfile(io_handle)
        dst_profile = ImageCms.createProfile('sRGB')
        img_conv = ImageCms.profileToProfile(img, src_profile, dst_profile)
        icc_conv = img_conv.info.get('icc_profile','')
        if icc != icc_conv:
            # ICC profile was changed, converted file is saved
            img_conv.save(image_path,
                        format = 'JPEG',
                        quality = 50,
                        icc_profile = icc_conv)


def save_image_to_assets(source_image_path, content_type="recipe"):
    """Copy and save an external image to assets folder; supported content_type are recipe and notes"""
    if content_type != "recipe" and content_type != "notes":
        content_type = "recipe"
        
    # copy source image to assets
    destination_path = f'assets/images/images_{content_type}/' + os.path.basename(source_image_path)
    shutil.copy(source_image_path, destination_path)

    # handle complex icc profiles in assets folder
    convert_icc_to_icc_srgb(destination_path)

    return destination_path
