class HashCracker:
    @staticmethod
    def crack_hash(hashed_pwd, hash_func, file_path):
        result = ""
        wordlist = open(file_path, "r")
        for word in wordlist:
            if hashed_pwd == hash_func(word[:-1]):
                result = word[:-1]
                break

        wordlist.close()
        return result
