class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def display(self, level=0):
        indent = "  " * level
        print(f'{indent}{self.author}: {self.text}'
              if not self.is_deleted else f'{indent}Reply was deleted')
        for reply in self.replies:
            reply.display(level + 1)

    def remove_reply(self):
        self.is_deleted = True


comment = Comment("Hello! Great book!", "Val")
reply1 = Comment("Liked it too", "Nik")
reply2 = Comment("Just wanted to leave a comment", "Charlie")
comment.add_reply(reply1)
comment.add_reply(reply2)
reply2.add_reply(Comment("Hi", "Anna"))
comment.add_reply(Comment("Hey", "Charlie"))
reply2.remove_reply()

comment.display()
