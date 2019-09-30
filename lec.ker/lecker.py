import web

urls = (
    "/",
    "view",
    "/add",
    "add",
    "/delete",
    "delete",
    "/edit/([0-9]*)",
    "edit",
    "/search/(\S*)",
    "search",
)


class view:
    def GET(self):
        bookmarks = list(web.select("bookmarks", order="created desc"))
        for b in bookmarks:
            b.tags = b.tags.split()
        web.render("view.html")


class add:
    def POST(self):
        i = web.input()
        web.debug(type(i.tags))
        n = web.insert("bookmarks", title=i.title, url=i.url, tags=i.tags)
        web.seeother("./#t" + str(n))


class delete:
    def GET(self):
        bookmarks = web.select("bookmarks", order="title")
        web.render("delete.html")

    def POST(self):
        i = web.input()
        web.debug(i)
        for item in i:
            web.delete("bookmarks", "id = " + item)
        web.seeother("./#")


class edit:
    def GET(self, id):
        try:
            bookmark = web.select("bookmarks", where="id = " + id)[0]
            web.render("edit.html")
        except IndexError:
            print("This bookmark doesn't exist.")

    def POST(self, id):
        i = web.input()
        web.update("bookmarks", "id = " + id, title=i.title, url=i.url, tags=i.tags)
        web.seeother("../")


class search:
    def GET(self, tag):
        bookmarks = []
        bs = list(web.select("bookmarks", order="created desc"))
        for b in bs:
            b.tags = b.tags.split()
            if tag in b.tags:
                bookmarks.append(b)
        empty = len(bookmarks) == 0
        web.render("search.html")

    def POST(self, tag):
        i = web.input()
        tags = i.tags.split()
        bookmarks = []
        bs = list(web.select("bookmarks", order="created desc"))
        for b in bs:
            b.tags = b.tags.split()
            if every(lambda t: t in b.tags, tags):
                bookmarks.append(b)
        empty = len(bookmarks) == 0
        web.render("search.html")


def every(f, lst):
    for x in lst:
        if not f(x):
            return False
    return True


web.internalerror = web.debugerror
web.db_parameters = dict(dbn="mysql", user="root", pw="", db="lecker")
if __name__ == "__main__":
    web.run(urls, web.reloader)
