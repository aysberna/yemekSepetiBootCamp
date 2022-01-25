# 2022 - YemekSepeti Python Web Development BootCamp
# User model

from commons.common import RE

class User:
    def __init__(self,
        email            = RE.defaultNone,
        username         = RE.defaultNone,
        isimsoyisim      = RE.defaultNone,
        emailuserlk      = RE.defaultZero,
        usernamelk       = RE.defaultZero,
        dogumyil         = RE.defaultYear,
        dogumay          = RE.defaultMonth,
        dogumgun         = RE.defaultDay,
        ulke             = RE.defaultNone,
        ap               = RE.defaultAP):

        self.email       = email
        self.username    = username
        self.isimsoyisim = isimsoyisim
        self.emailuserlk = emailuserlk
        self.usernamelk  = usernamelk
        self.dogumyil    = dogumyil
        self.dogumay     = dogumay
        self.dogumgun    = dogumgun
        self.ulke        = ulke
        self.ap          = ap