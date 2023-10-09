# python using-flet
import flet as ft

def main(page: ft.Page):
    
    # 情報入力画面における入力内容取得のためのTextFieldハンドラ
    # View内に ft.TextField を直接記述されると ハンドラ.value での取得が通じない
    page1_mes_field = ft.TextField(value="view1")

    # メール確認画面における入力内容書き換えのためのTextFieldハンドラ
    # View内に ft.TextField を直接記述されると ハンドラ.value での取得が通じない
    page2_mes_field = ft.TextField(value="view2")
    
    # 結果表示画面における入力内容書き換えのためのTextFieldハンドラ
    # View内に ft.TextField を直接記述されると ハンドラ.value での取得が通じない
    page3_mes_field = ft.TextField(value="view3")

    # 情報入力画面からメール確認画面への遷移における処理
    def send_input(e):
        print(page1_mes_field.value)
        # 入力された情報で情報確認ページに移動
        page2_mes_field.value = page1_mes_field.value
        page.go("/view2")
    
    # メール確認画面から結果表示画面への遷移における処理
    def send_mail(e):
        print(page2_mes_field.value)
        # TODO : chatGPTにリクエストを投げる
        page3_mes_field.value = page2_mes_field.value
        page.go("/view3")
    
    def main_screen(e):
        page1_mes_field.value = "view1"
        page.go("/view1")

    # 情報入力画面
    view1: ft.View = ft.View(
        "/view1",
         [
            ft.AppBar(title=ft.Text("view1"),
                      bgcolor=ft.colors.BLUE),
            page1_mes_field,
            ft.ElevatedButton(
                #"入力確認画面", on_click=lambda _: page.go("/view2")),
                "入力確認画面", on_click=send_input),
        ]
    )

    # メール確認画面 
    view2: ft.View = ft.View(
        "/view2", 
        [
            ft.AppBar(title=ft.Text("view2"),
                      bgcolor=ft.colors.RED),
            page2_mes_field,
            ft.ElevatedButton(
                "確定・送信", on_click=send_mail),
        ]
    )

    # 結果表示画面
    view3: ft.View = ft.View(
        "/view3", 
        [
            ft.AppBar(title=ft.Text("view3"),
                      bgcolor=ft.colors.RED),
            page3_mes_field,
            ft.ElevatedButton(
                "最初の画面", on_click=main_screen),
        ]
    )

    def route_change(handler):
        page.views.clear()
        if page.route != "/view3":
            page.views.append(view1)
            if page.route == "/view2":
                page.views.append(view2)
        else:
            page.views.append(view3)
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