import DmozItem

class ExtItems(DmozItem):
     name = scrapy.Field(DmozItem.fields['name'], serializer=my_serializer)
