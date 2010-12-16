# coding=utf-8
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.app.rotterdam import Rotterdam

# Layers just inherit from IBrowserRequest.
class IGSGreenLayer(IBrowserRequest):
    '''GroupServer Green Layer'''
# Skins inherit from a bunch of layers. In this case the green layer
# and the core Zope Rotterdam layer.
class IGSGreenSkin(IGSGreenLayer, Rotterdam):
    '''GroupServer Green Skin'''

