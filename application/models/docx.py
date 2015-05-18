 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

'''




'''




class wordXML():
    
    
    def __init__(self, documentXML):
        self.XML = BeautifulSoup(documentXML)

    
    
    def getAllParagraphs(self):
        
        paragraphs = self.XML.findAll('w:p')
        
        return paragraphs
        
        
        
        
    def getAllRuns(self, theParagraph):    
        paragraph = theParagraph
        runs = paragraph.findAll('w:r')

        returnRun = ''

        for run in runs:
           returnRun += self.getInlineElements(run)

        return returnRun
    
    
    
    
    def readOutLoud(self):
        
        '''
            print Word document as HTML
        
        '''
        returnString = ''
        returnString = returnString + "<!DOCTYPE html><html><head><meta http-equiv='Content-type' content='text/html; charset=utf-8'><title></title></head><body>"
        
        for paragraph in self.getAllParagraphs():
            returnString = returnString + (self.createParagraph(paragraph))
            
        returnString = returnString + ("</body></html>")

        return returnString
        
         
        
        
        
        
        
    def createParagraph(self, theParagraph):
        
        if theParagraph.find('w:pstyle') != None:
            style = theParagraph.find('w:pstyle')
            style = style['w:val']
            
        else:
            style = 'none'
            
            
        nodeType = self.getParagraphNodeType(style)
        AllRuns = self.getAllRuns(theParagraph)
        
        if nodeType[:1] == 'p':
        
            returnString = "<{nodeName}>{Runs}</p>".format(nodeName=nodeType,Runs=AllRuns)
        else: 
            returnString = "<{nodeName}>{Runs}</{nodeName}>".format(nodeName=nodeType,Runs=AllRuns)
        
        return(returnString)
        
        
    def getParagraphNodeType(self, elementNode):

        blockNodeArray = dict(
                            Overskrift1='h1',
                            Overskrift2='h2',
                            Overskrift3='h3',
                            Overskrift4='h4',
                            Overskrift5='h5',
                            Overskrift6='h6',
                            Heading1='h1',
                            Heading2='h2',
                            Heading3='h3',
                            Heading4='h4',
                            Heading5='h5',
                            Heading6='h6'
                        )
        
        
        nodeName = []


        if elementNode in blockNodeArray and not(blockNodeArray[elementNode] is None):
            nodeName = blockNodeArray[elementNode]
    
        elif self.getClassFromNode(elementNode) != False:

            nodeName = "p class='{classString}'".format(classString=self.getClassFromNode(elementNode))
    
        else:
            nodeName = 'p'
    

        return nodeName
    
    
    
            
            
            
  


     
        
        
       
    def getInlineElements(self, theRow):
        returnRun = ''
        
        
        for row in theRow.children:
            
            if row.name == 'w:br':
                returnRun += '<br/>'
                
            elif row.name == 'w:t':
                returnRun += row.text.encode('utf-8', 'ignore')
            
            else:
                returnRun += ''
                

  
        
        if theRow.find('w:rpr') != None:
            nodes = theRow.find('w:rpr')
            
            nodeString = ''
            
            for node in nodes.children:
                theName = node.name
                theName = str(theName)[2:]
                
                nodeArry = self.getInlineNodeType(theName)
                returnRun = nodeArry[0] + returnRun + nodeArry[1]
                
        
        
        
        
        return returnRun
        
        
        
        
        
        
        
        
        
        
        

    def getInlineNodeType(self, elementNode):

        blockNodeArray = dict(
                            i='i',
                            b='b',
                            u='u',
                            strike='del'                    
                        )
        
        
        nodeName = ''


        if elementNode in blockNodeArray and not(blockNodeArray[elementNode] is None):
            nodeName = "<{node}>".format(node=blockNodeArray[elementNode])
            nodeEnd  = "</{node}>".format(node=blockNodeArray[elementNode])
            
            returnNode = [nodeName, nodeEnd]
            
        elif self.getClassFromNode(elementNode) != False:

            nodeName = "<span class='{classString}'>".format(classString=self.getClassFromNode(elementNode))
            nodeEnd  = "</span>"
            
            returnNode = [nodeName, nodeEnd]
            
        else:
            nodeName = ''
            nodeEnd  = ''
    
            returnNode = [nodeName, nodeEnd]

        return returnNode
    
    
    
    
    
    





    #getClassesFromNode
    def getClassFromNode(self, nodeType):

        classNodeArray = dict(
                        caps='caps',
                        shadow='shadow',
                        Opslag='entry',
                        Titel='title',
                        Pause='pause'
                        )

        if nodeType in classNodeArray and not(classNodeArray[nodeType] is None):

             return classNodeArray[nodeType]
        else:

            return False