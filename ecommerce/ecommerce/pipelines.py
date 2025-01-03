from sqlalchemy.orm import sessionmaker
from ecommerce.items import Product, engine

class EcommercePipeline:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)
    
    def clean_string(self, text):
        if not isinstance(text, str):
            return text
        return ' '.join(text.strip().split())
    
    def clean_price(self, price):
        if isinstance(price, str):
            return self.clean_string(price)
        return price
    
    def clean_url(self, url):
        if isinstance(url, str):
            return url.strip()
        return url

    def process_item(self, item, spider):
        clean_item = {
            'name': self.clean_string(item.get('name')),
            'price': self.clean_price(item.get('price')),
            'url': self.clean_url(item.get('url')),
            'image_url': self.clean_url(item.get('image_url'))
        }
          
        session = self.Session()
        product = Product(
            name=clean_item['name'],
            price=clean_item['price'] or None,
            url=clean_item['url'],
            image_url=clean_item['image_url'] or None,
            )
        session.add(product)
        session.commit()
        session.close()
        
        return clean_item