import flet as ft

class Page1Fields:
    # 送信元
    address_field = ft.TextField(hint_text="送信元")
    # 送信元の所属組織
    organize_field = ft.TextField(hint_text="送信元の所属組織")
    # 送信元が所属する部署
    department_field = ft.TextField(hint_text="送信元の所属部署")
    # 送信元の上司
    supervisor_field = ft.TextField(hint_text="送信元の上司")

    def __init__(self):
        pass
    
    def install_field(self):
        return self.address_field, self.organize_field, self.department_field, self.supervisor_field
    
    def all_clear(self):
        self.address_field.value = ""
        self.organize_field.value = ""
        self.department_field.value = ""
        self.supervisor_field.value = ""

    def all_return(self):
        return self.get_address()+" "+self.get_organize()+" "+self.get_department()+" "+self.get_supervisor()

    def get_address(self):
        return self.address_field.value
    
    def get_organize(self):
        return self.organize_field.value

    def get_department(self):
        return self.department_field.value
    
    def get_supervisor(self):
        return self.supervisor_field.value

    def set_address(self, add):
        self.address_field.value = add
    
    def set_organize(self, org):
        self.organize_field.value = org
    
    def set_department(self, dep):
        self.department_field.value = dep
    
    def set_supervisor(self, sup):
        self.supervisor_field.value = sup  

class Page2Fields:
    # 宛先
    dst_field = ft.TextField(hint_text="宛先")
    # CC
    cc_field = ft.TextField(multiline=True, hint_text="CC")
    # BCC
    bcc_field = ft.TextField(multiline=True, hint_text="BCC")
    # 差出人
    src_field = ft.TextField(hint_text="送信元")
    # 件名
    subject_field = ft.TextField(multiline=True, hint_text="件名")
    #本文
    mail_field = ft.TextField(multiline=True, hint_text="メール本文")

    def __init__(self):
        pass
    
    def install_field(self):
        return self.dst_field, self.cc_field, self.bcc_field, self.src_field, self.subject_field, self.mail_field
    
    def all_clear(self):
        self.dst_field.value = ""
        self.cc_field.value = ""
        self.bcc_field.value = ""
        self.src_field.value = ""
        self.subject_field.value = ""
        self.mail_field.value = ""
    
    def all_return(self):
        return self.get_dst()+" "+self.get_cc()+" "+self.get_bcc()+" "+self.get_src()+" "+self.get_subject()+" "+self.get_mail()

    def get_dst(self):
        return self.dst_field.value
    
    def get_cc(self):
        return self.cc_field.value

    def get_bcc(self):
        return self.bcc_field.value
    
    def get_src(self):
        return self.src_field.value
    
    def get_subject(self):
        return self.subject_field.value
    
    def get_mail(self):
        return self.mail_field.value

    def set_dst(self, dst):
        self.dst_field.value = dst
    
    def set_cc(self, cc):
        self.cc_field.value = cc
    
    def set_bcc(self, bcc):
        self.bcc_field.value = bcc

    def set_src(self, src):
        self.src_field.value = src
    
    def set_subject(self, sub):
        self.subject_field.value = sub
    
    def set_mail(self, mail):
        self.mail_field.value = mail

class Page3Fields:
    # 宛先
    dst_field = ft.TextField()
    # CC
    cc_field = ft.TextField(multiline=True)
    # BCC
    bcc_field = ft.TextField(multiline=True)
    # 差出人
    src_field = ft.TextField()
    # 件名
    subject_field = ft.TextField()
    #本文
    mail_field = ft.TextField(multiline=True)
    # GPTの返答
    gpt_field = ft.TextField(multiline=True)

    def __init__(self):
        pass

    def install_field(self):
        return self.dst_field, self.cc_field, self.bcc_field, self.src_field, self.subject_field, self.mail_field, self.gpt_field
    
    def all_return(self):
        return self.get_dst()+" "+self.get_cc()+" "+self.get_bcc()+" "+self.get_src()+" "+self.get_subject()+" "+self.get_mail()

    def get_dst(self):
        return self.dst_field.value
    
    def get_cc(self):
        return self.cc_field.value

    def get_bcc(self):
        return self.bcc_field.value
    
    def get_src(self):
        return self.src_field.value
    
    def get_subject(self):
        return self.subject_field.value
    
    def get_mail(self):
        return self.mail_field.value

    def get_gpt(self):
        return self.gpt_field.value

    def set_dst(self, dst):
        self.dst_field.value = dst
    
    def set_cc(self, cc):
        self.cc_field.value = cc
    
    def set_bcc(self, bcc):
        self.bcc_field.value = bcc
    
    def set_src(self, src):
        self.src_field.value = src

    def set_subject(self, sub):
        self.subject_field.value = sub
    
    def set_mail(self, mail):
        self.mail_field.value = mail
    
    def set_gpt(self, gpt):
        self.gpt_field.value = gpt
