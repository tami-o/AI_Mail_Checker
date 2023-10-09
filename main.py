# python using-flet
import flet as ft

def main(page: ft.Page):

    # 情報入力画面
    view1: ft.View = ft.View(
        "/view1",
         [
            ft.AppBar(title=ft.Text("view1"),
                      bgcolor=ft.colors.BLUE),
            ft.TextField(value="view1"),
            ft.ElevatedButton(
                "入力確認画面", on_click=lambda _: page.go("/view2")),
        ]
    )

    # メール確認画面git 
    view2: ft.View = ft.View(
        "/view2", 
        [
            ft.AppBar(title=ft.Text("view2"),
                      bgcolor=ft.colors.RED),
            ft.TextField(value="view2"),
            ft.ElevatedButton(
                "確定・送信", on_click=lambda _: page.go("/view3")),
        ]
    )

    # 結果表示画面
    view3: ft.View = ft.View(
        "/view3", 
        [
            ft.AppBar(title=ft.Text("view3"),
                      bgcolor=ft.colors.RED),
            ft.TextField(value="view3"),
            ft.ElevatedButton(
                "最初の画面", on_click=lambda _: page.go("/view1")),
        ]
    )

    def route_change(handler):
        page.views.clear()
        if page.route != "/view3":
            page.views.append(view1)
            if page.route == "/view2":
                page.views.append(view2)
        else:
            pass
        page.update()

    def view_pop(handler):
        page.views.pop()
        page.go("/back")


    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.title = "Navigation and routing"
    page.views.clear()
    page.go("/view1")


if __name__ == "__main__":
    ft.app(target=main, port=8888, view=ft.WEB_BROWSER)