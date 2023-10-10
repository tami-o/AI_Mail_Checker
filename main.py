# python using-flet
import flet as ft
import req_chatGPT


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
    page3_gpt_field = ft.TextField(value="view3")

    # ChatGPTリクエスト情報保存用のリスト
    person_info = []

    # 情報入力画面からメール確認画面への遷移における処理
    def save_input(e):
        print(page1_mes_field.value)
        # 入力された情報をChatGPTのリクエスト用リストに保存
        person_info.append(page1_mes_field)
        print(len(person_info))
        #page2_mes_field.value = page1_mes_field.value
        page.go("/view2")
    
    # メール確認画面から結果表示画面への遷移における処理
    def send_mail(e):
        print(page2_mes_field.value)
        # chatGPTにリクエストを投げる
        chatGPT_res = req_chatGPT.request_chatGPT(person_info)
        # 入力された情報とChatGPTの回答を持って結果表示画面に移動
        page3_mes_field.value = page2_mes_field.value
        page3_gpt_field.value = chatGPT_res
        page.go("/view3")
    
    def main_screen(e):
        page1_mes_field.value = "view1"
        page2_mes_field.value = "view2"
        page.go("/view1")

    # 情報入力画面
    view1: ft.View = ft.View(
        "/view1",
         [
            ft.AppBar(title=ft.Text("情報入力画面"),
                      bgcolor=ft.colors.BLUE),
            page1_mes_field,
            ft.ElevatedButton(
                "入力確認画面", on_click=save_input),
        ]
    )

    # メール確認画面 
    view2: ft.View = ft.View(
        "/view2", 
        [
            ft.AppBar(title=ft.Text("メール確認画面"),
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
            ft.AppBar(title=ft.Text("結果表示画面"),
                      bgcolor=ft.colors.RED),
            # 横並びに表示する為に Row の中に入れている
            ft.Row(
                [
                    page3_mes_field,
                    page3_gpt_field,
                ]
            ),
            ft.ElevatedButton(
                "情報入力画面に戻る", on_click=main_screen),
        ]
    )

    def route_change(handler):
        page.views.clear()
        if page.route != "/view3":
            page.views.append(view1)
            if page.route == "/view2":
                # view1 の上に view2 が乗っている状態なので pop すると view1 に戻ることが可能
                page.views.append(view2)
        else:
            # view3 つまり結果画面からview2に戻れないように独立させる
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
    # localhost:8888 で起動されている
    ft.app(target=main, port=8888, view=ft.WEB_BROWSER)