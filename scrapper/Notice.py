class Notice:
    def __init__(self,head=None,url=None,is_new_notice=False):
        self.head = head
        self.url = url
        self.is_new_notice = is_new_notice

    def __str__(self):
        return f"{self.head} || {self.url}"