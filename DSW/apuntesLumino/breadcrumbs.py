from dataclasses import dataclass

@dataclass
class BreadcrumbItem:
    title: str
    url: str
    active: bool

class Breadcrumbs:
    def __init__(self, add_home: bool = True):
        self.items = []
        if add_home:
            self.add('Home', '/')

    def add(self, title: str, url: str):
        if len(self.items) > 0:
            self.items[-1].active = False
        self.items.append(BreadcrumbItem(title, url, True))

    def __len__(self):
        return len(self.items)
    
    def __iter__(self):
        for item in self.items:
            yield item
    
    def __str__(self):
        buffer = []
        for item in self:
            buffer.append(f'{item.title} ({item.url}){" *" if item.active else ""}')
        return ' > '.join(buffer)
