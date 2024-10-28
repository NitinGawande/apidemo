class Util:

    def common_header_json(self):
        header={
            "Content-Type":"application/json"
        }
        return header

    def common_header_xml(self):
        header={
            "Content-Type":"application/xml"
        }
        return header

    def common_header_put_patch_delete_basic_auth(self):
        header={
            "Content-Type": "application/json",
            "Authorization":"YWRtaW46cGFzc3dvcmQxMjM="
        }

    def common_header_put_patch_delete_basic_cookie(self,token):
        header = {
            "Content-Type": "application/json",
            "Cookie":"token="+str(token)
        }