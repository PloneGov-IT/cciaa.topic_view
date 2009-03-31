from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName


class TopicView(BrowserView):
    """Vista dei cercatori"""
    
    def getDescr(self, doc_id):
        """restituisce la descrizione dell'oggetto"""
        context = self.context
#        import pdb;pdb.set_trace()
        page = getattr(context, doc_id)
        
        return page.Description()
