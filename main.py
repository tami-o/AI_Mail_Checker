# python using-flet
import flet as ft
import req_chatGPT
import info_class


def main(page: ft.Page):

    # Page1 情報入力画面表示処理
    page1_fields = info_class.Page1Fields()
    add_f_p1, org_f_p1, dep_f_p1, sup_f_p1 = page1_fields.install_field()

    # Page2 メール入力画面表示処理
    page2_fields = info_class.Page2Fields()
    dst_f_p2, cc_f_p2, bcc_f_p2, src_f_p2, sub_f_p2, mail_f_p2 = page2_fields.install_field()
    
    # Page3 結果表示画面表示処理
    page3_fields = info_class.Page3Fields()
    dst_f_p3, cc_f_p3, bcc_f_p3, src_f_p3, sub_f_p3, mail_f_p3, gpt_f_p3 = page3_fields.install_field()    

    # ChatGPTリクエスト情報保存用のリスト
    request_info = {}

    # Page1(情報入力画面)からPage2(メール入力画面)への遷移における処理
    def save_input(e):
        print(page1_fields.get_address())
        # 入力された情報をChatGPTのリクエスト用リストに保存
        request_info['role_system'] = page1_fields.all_return()
        page.go("/view2")
    
    # Page2(メール入力画面)からPage3(結果表示画面)への遷移における処理
    def send_mail(e):
        print(page2_fields.get_dst())
        # 入力された情報をChatGPTのリクエスト用リストに保存
        request_info['role_user'] = page2_fields.all_return()
        # chatGPTにリクエストを投げる
        chatGPT_res = req_chatGPT.request_chatGPT(request_info)
        # 入力された情報とChatGPTの回答を持って結果表示画面に移動
        page3_fields.set_dst(page2_fields.get_dst())
        page3_fields.set_cc(page2_fields.get_cc())
        page3_fields.set_bcc(page2_fields.get_bcc())
        page3_fields.set_src(page2_fields.get_src())
        page3_fields.set_subject(page2_fields.get_subject())
        page3_fields.set_mail(page2_fields.get_mail())
        page3_fields.set_gpt(chatGPT_res)
        page.go("/view3")
    
    # Page3(結果表示画面)からPage1((情報入力画面)への遷移における初期化処理
    def main_screen(e):
        page1_fields.all_clear()
        page2_fields.all_clear()
        page.go("/view1")

    # 情報入力画面
    view1: ft.View = ft.View(
        "/view1",
         [
            ft.AppBar(title=ft.Text("情報入力画面"),
                      bgcolor=ft.colors.BLUE),
            add_f_p1,
            org_f_p1,
            dep_f_p1,
            sup_f_p1,
            ft.ElevatedButton(
                "メール入力画面", on_click=save_input),
        ]
    )

    # メール確認画面 
    view2: ft.View = ft.View(
        "/view2", 
        [
            ft.AppBar(title=ft.Text("メール入力画面"),
                      bgcolor=ft.colors.RED),
            dst_f_p2,
            cc_f_p2,
            bcc_f_p2,
            src_f_p2,
            sub_f_p2,
            mail_f_p2,
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
                    dst_f_p3,
                    gpt_f_p3
                ]
            ),
            cc_f_p3,
            bcc_f_p3,
            src_f_p3,
            sub_f_p3,
            mail_f_p3,
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