from . import cairo as cairo, constants as constants
from .surfaces import SURFACE_TYPE_TO_CLASS as SURFACE_TYPE_TO_CLASS, Surface as Surface

class XCBSurface(Surface):
    def __init__(self, conn, drawable, visual, width, height) -> None: ...
    def set_size(self, width, height) -> None: ...
