class Item(object):

    def __init__(self):
        self.clear()

    def clear(self):
        self.janCode = ""
        self.salesPrice = ""
        self.salesPriceNotes = []
        self.shopName = ""
        self.linkUrl = ""
        self.itemName = ""
        self.itemDesc = ""

    def addSalesPriceNotes(self, value):
        self.salesPriceNotes.append(value)

    def getItemInfo(self):
        fields = [("JANR[h", self.janCode),
                  ("€iΌ", self.itemName),
                  ("ΜΏi", self.salesPrice),
                  ("VbvΌ", self.shopName),
                  ("NURL", self.linkUrl),
                  ("€iΰΎ", self.itemDesc)]
        for note in self.salesPriceNotes:
            fields.append(("Ώiυl", note))
        itemInfo = []
        for key, value in fields:
            if not value:
                continue
            itemInfo.append((key, value))
        return itemInfo
