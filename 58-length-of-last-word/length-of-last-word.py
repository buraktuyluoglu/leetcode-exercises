class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimmed_string = s.strip()  
        ters_string = trimmed_string[::-1]
        bosluk_index = ters_string.find(' ')
        if bosluk_index != -1:
            ilk_kelime_tersten = ters_string[:bosluk_index]
            harf_sayisi = len(ilk_kelime_tersten)
            return harf_sayisi
        else:
            harf_sayisi = len(ters_string)
            return harf_sayisi