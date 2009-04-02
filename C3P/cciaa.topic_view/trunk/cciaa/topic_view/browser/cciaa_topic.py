from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName


class TopicView(BrowserView):
    """Vista dei cercatori"""
    IMG_TAG = u"""<img src="%s" alt="%s" title="%s" />"""
    
    def getDescr(self, doc_id):
        """restituisce la descrizione dell'oggetto"""
        context = self.context
        page = getattr(context, doc_id)
        return page.Description()
    
    def generateImgTag(self, icon, alt="", title=""):
        """Dato un'icona caricata dal tramite @@plone.getIcon ne genera un tag (X)HTML da usare
        per la modulistica
        """
        src = icon.url
        return self.IMG_TAG % (src, alt, title)