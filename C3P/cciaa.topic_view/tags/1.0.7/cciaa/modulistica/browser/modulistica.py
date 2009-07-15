# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

class ModulisticaView(BrowserView):
    """Vista dei file nella vista modulistica"""

    IMG_TAG = """<img src="%s" alt="%s" title="%s" />"""

    def getDocumentContentOf(self, doc_id):
        """Dato l'id, carica da questo folder una pagina"""
        context = self.context
        page = getattr(context, doc_id)
        body = '<a name="sezione-'+ doc_id +'"></a>' + page.getText()
        return body
    
    def generateImgTag(self, icon, alt="", title=""):
        """Dato un'icona ne genera un tag (X)HTML da usare
        per la modulistica
        """
        src = icon
        if not src:
            # Can happens for some valuesofo icon_visibility in site_properties
            return alt
        return self.IMG_TAG % (src, alt, title)
    
    def generateColumns(self,related_items,num_rel):
        """genera le colonne vuote della tabella
        """
        var= related_items - num_rel
        stringa = ""
        for i in range(0,var):
            stringa += "<td class=\"col3\"/>"
        return stringa
    
    def getProxiedContent(self, proxy_brain, valid_target_type='File'):
        """Dato un brain ottiene il relativo brain per l'oggetto proxato.
           Questo richiede esplicitamente l'uso di ATProxiedContent
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        proxyed = catalog(UID=proxy_brain.getProxyreference)
        if proxyed:
            return proxyed[0]
        return self.context
    
    def count_related_items(self,items):
        """ ritorna quanti elementi correlati ha un file, e se ne ha più di 2 ritorna oslo i primi 2"""
        max = 0
        for item in items:
            if item.portal_type=='File':
                if len(item.getRawRelatedItems) > max:
                    max = len(item.getRawRelatedItems)
            if max > 2:
                return 2
        return max
    
    def getTitles(self,items):
        """ crea l'header della tabella con i titoli impostati nel campo della cartella """
        stringa =""
        num_related = self.count_related_items(items)+2
        
        if self.context.getColumns():
            if len(self.context.getColumns()) > num_related:
                titles = self.context.getColumns()[:num_related]
            else:
                titles= self.context.getColumns()
        
            for title in titles:
                stringa += '<th class="nosort">' + title + "</th>" 
            if len(titles) < num_related :
                for i in range(num_related-len(titles)):
                    stringa += "<th>" "</th>"
        return """<tr class="heading-moduli">%s</tr>""" % stringa
