import  requests

class GitHub:

    # def get_user_defunkt(self):
    #     r =  requests.get('https://api.github.com/users/defunkt')
    #     body = r.json()
    #     return body

    # def get_non_exist_user(self):
    #     r =  requests.get('https://api.github.com/users/olgaas')
    #     body = r.json()
    #     return body

# optimizing code of 2 similer function:

    def get_user (self, username):
         r =  requests.get(f'https://api.github.com/users/{username}')
    #     body = r.json()
    #     return body

    def search_repo(self, namerepo):
        r = requests.get(f'https://api.github.com/search/repositories',
        params= {"q": namerepo}
        )
        body = r.json()
        return body