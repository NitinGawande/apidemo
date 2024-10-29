class Util:

    @staticmethod
    def common_header_json():
        return {
            "Content-Type": "application/json"
        }

    @staticmethod
    def common_header_xml():
        return {
            "Content-Type": "application/xml"
        }

    @staticmethod
    def common_header_put_patch_delete_basic_auth():
        return {
            "Content-Type": "application/json",
            "Authorization": "YWRtaW46cGFzc3dvcmQxMjM="  # Base64 encoded "admin:password123"
        }

    @staticmethod
    def common_header_put_patch_delete_basic_cookie(token):
        return {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
