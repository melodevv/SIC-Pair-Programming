class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return True if len(self.stack) == 0 else False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return None if self.is_empty() else self.stack.pop()


def html_matched(text):
    S = Stack()

    start = text.find("<")

    while start != -1:
        end = text.find(">", start + 1)
        if end == -1:
            return False
        tag = text[start + 1:end]

        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        start = text.find("<", end + 1)
    return S.is_empty()


def main():
    text = input("Input the string of HTML document: ")

    # Check if all HTML tags Match
    match_result = html_matched(text)

    print('Did all the html tags entered match?', 'No' if match_result == False else 'Yes')


main()
