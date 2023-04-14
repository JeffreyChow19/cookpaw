from PyQt5 import QtGui

def getFont(type, size):
    # Set the path to the font file based on the type
    font_path = f"assets/fonts/poppins/Poppins-{type}.ttf"

    # Add the font to the application
    font_id = QtGui.QFontDatabase.addApplicationFont(font_path)

    # Get the font family name
    font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]

    # Create a QFont object using the font
    font = QtGui.QFont(font_family)

    # Set the font size
    font.setPointSize(size)
    if (type == "Bold"):
        font.setWeight(75)

    return font

# def getColor(color):
#     return 