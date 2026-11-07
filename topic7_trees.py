"""Тема 7. Максимум у BST/AVL + ієрархічна система коментарів."""


# ---------- Завдання 1 ----------
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root: Node | None, key) -> Node:
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def find_max(root: Node | None):
    """Найбільше значення у BST/AVL - крайній правий вузол. O(h)."""
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.key


# ---------- Завдання 2 ----------
class Comment:
    DELETED_TEXT = "Цей коментар було видалено."

    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author
        self.replies: list["Comment"] = []
        self.is_deleted = False

    def add_reply(self, reply: "Comment") -> None:
        self.replies.append(reply)

    def remove_reply(self) -> None:
        """Позначає коментар видаленим, але зберігає гілку відповідей."""
        self.text = self.DELETED_TEXT
        self.is_deleted = True

    def display(self, level: int = 0) -> None:
        indent = "    " * level
        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)


if __name__ == "__main__":
    root = None
    for k in [50, 30, 70, 20, 40, 60, 80, 75]:
        root = insert(root, k)
    print("Максимум у дереві:", find_max(root))  # 80
    print()

    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()
