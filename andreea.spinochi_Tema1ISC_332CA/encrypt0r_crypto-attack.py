#!/usr/bin/env python3

import base64
import json
import gmpy2


def str_to_number(text):
    """ Encodes a text to a long number representation (big endian). """
    return int.from_bytes(text.encode("ASCII"), 'big')

def number_to_str(num):
    """ Decodes a text to a long number representation (big endian). """
    num = int(num)
    return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big').decode('ASCII')

def encrypt(pub_k, msg_num):
    """ We only managed to steal this function... """
    cipher_num = gmpy2.powmod(msg_num, pub_k["e"], pub_k["n"])
    # note: gmpy's to_binary uses a custom format (little endian + special GMPY header)!
    cipher_b64 = base64.b64encode(gmpy2.to_binary(cipher_num))
    return cipher_b64

def decrypt(priv_k, cipher):
    """ We don't have the privary key, anyway :( """
    # you'll never get it!
    pass


if __name__ == "__main__":
    # example public key
    pub_k = {"e": 17, "n": 1221540932698357538969048008476734604937734436157953593060163}
    # generate a message
    message = "Test Message 1234"
    # note: encrypt requires a number
    msg_num = str_to_number(message)
    # test the reverse
    print("Message:", number_to_str(msg_num))
    # encrypt the message
    cipher = encrypt(pub_k, msg_num)
    print("Ciphertext:", cipher)
    # encode the message to the server's format
    # todo...
    var1 = gmpy2.powmod(2, 137993, 14038279245896146096352238237947274508254687636255158417144897911727934487744385077705712111134624993618848955529376008832604802536168339876112122812013919594093192039411809495689491609900254868476863398795866127816171778596800854831341780809239436921127930912701471446174266656880972789223833639117113881853434689178851766113335941223396641036509929993801012448995763764175383258065045017914018231669863635002603493587843122019544234901489406896938205245558713010882665861557135545491800697560099038115186750412300416588433008758692955795905539726035511888851259755193413583776486939560319518061785352397561748891531)
    var2 = 1363659222958754023523014263707659123024685870954600043395437572713881082985428616965834243954806845493618594846064919267271571256456504418195474933675729562864171238505460741994204845581335406237630191040032539262040407582035880089348516650923262838763324524556219173707464566125998489455663479212178964930395344387246963975989693285096769168620460518501020665913526269731917595422123881368689000376987423044578001659229561319018372355490896593109451421470724428332218540460400876757773490512013393189648715377171257718967995457286290929134277191659067069913087318141101642664068842757159555058665014174354304276986
    var3 = var1 * var2
    final = base64.b64encode(gmpy2.to_binary(var3))
    final = final.decode("utf-8")
    print()
    print(final)
    
    num = b'\xa6\xe0\xca\xd2\xe6\xd0\x8c\xd8\xc2\xce\xf6\xd2\xb2\xd6h\xee\xb2n\xec\xa6\xb2\x8c\xae\xac\xda\xc6\xda\xa0b\xce\xec\xd8\xaa\x8c\xe4\xea\xc8\xd8\x90f\xe6\xf0\x8a\xfa'
    result = int.from_bytes(num, "big")
    res = result//2
    print(number_to_str(int(res)))
