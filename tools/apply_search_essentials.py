from __future__ import annotations

import base64
import hashlib
import io
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
ARCHIVE_SHA256 = '9a2db1ea6483493c90bfb8630ecb35081ecf59fd44ef116a415dcf7da16165a7'
ARCHIVE_B64 = 'UEsDBBQAAAAIANKs81wCm28V/QoAAFchAAAKAAAAYWJvdXQuaHRtbOVa3XLjthW+71Og9ExvVtSPd7O7VmRl/5JsMruJG2cnM+10OhAJkYhAggFAyWq6t73vY/QJep9H6ZP0OwApkbZsOcl2pp1OEps/wMHhOd/5zgc4s9+mOnHbSrDcFWo+o59M8TI7j0QZv7uM8EjwdD4rhOMsybmxwp1HtVvGT6PmackLcR6tpdhU2riIJbp0osSojUxdfp6KtUxE7G8GTJbSSa5im3Alziew4aRTYv58oWvHXvGVhsWXukyMcIJ9I2xtljyRZcb+yr7dyJK9xHxh2duvZqMws+tEKmxiZOWkLjt+vBHclMzlghlhZYpn8IAtdVLbAePWCmsLPGS8qozmCbxspjLreJlyk1qG36zKtdPMGV7aihtRJlu2ELnEm7v8lmHpjvPDfuSMXmhnO/7CorgaLLVSejMo+FUsC56JuDKCgjxV3GTCP7elrCrhpvHE367xbXo3LJ70l+G1y7XpLHOH0/2ZcL8QcaJVb/rJ5OFpevoEQ5UsVwitOo8SXupSIrURy41Ynke5c5WdjkaPx+OPnp4ViyJeCFENM+nyejGUepR6J2A8OBGbvRMjTpgYEiR7i3DlhCm5E2GRHVpr+59cVSaEqWB/ydd0O7TrLGJUPXhNKRrhwYOraxOt2yphcyFcOz08GSbWfrI+Px2fPh4/mZzFQGFApu1NRzqxVCkSd/3rlsiEHWZaZ0rwSsKgLn7eVMDbycTPY4nR1mojM1k2No6vNsInnH6y5IVU2/NXbx9cojKmmyx3zx6Nxx9/hP+QgY+fjMe/a8a85aXRlQhjmncfP8X7VNpK8e253fAquhG3Bo0VzTVuex7pbEph73KNWFgJSBwaSi/+TFD+eeDvL0dc05l/lK8OWvkf46ee77VRHZ8/XIl1iWYjHWp7muCTOmvZuii42WJsiF5TcgiHAtdQMEcqffC9RVDnP0bP/LwrF013TtoEDMaH2mTRIHqWGV7l0fSPGOpBNA3JvEAB02uZdmb+ys87ASyrYJfC98Hswp7H8/QeOBz0uuL0vxBtA3S8N2DxmiI1bYQH3AbFv9WpXEpBKSGijMdP4skZTbAX3Livl9H0xw+RsZOWPt4PIh/lD2V3UVtZIqLR+/eDPd5eGGiqxNTF4o20jj7HiYIuP1WCYt8DJz3/Au8xrNJw0mdxsgPAa12IxsKv9Tbq+nhw2dODuPtAy3fg/f5P+Gc2CrCdz0ZBgy50up3PIEMVYApaWMkqpk7VdreTgktQwCWeM0Czge1sxOe/8SpWmN1U+BuHRxGTKZhHV6CXVK7bETQZ1jCl5Ot4A8qIOksvgPq0XdbLteA340byWPEFNbC7yiCnrIHP1lnPZAyew+eQfnuhr86jMRuzx4/wb2M5lykKFu6amqZX3OUM3r+djNmjM3b6lE0e55Onb3Dx6Oz1ZPwHjBnRoGZosxQtEvMkIaT56Q/99EdP2OSpgo2P4jMYev2wO5+kDfytONSBdUaX2Tx8H96E25ktuFLzQ5+LMf4dfnsDyMhsUTuny51Loqxjp7OMmmyg9zCg+XBxhYmpSEl7KSuap5Qko5UlqSOpRcRIVtS62Sx2980OESbWpUKPeQtPdn4GH+YzmPUw6S7Tzuw96+b/IrwgAMnMtykPoeugObHC0A4Jsu+yufIBOjAyQxAFNcLPw8Vt40DcCZHO/CJc9MYdqr04q9EJmo78OV3fZnrJf4jmnz3//W3v0Qn4/kvYc9w2Q1uch7yHX7HHxc1COhHWIXik5z4zQrBPm1tvaoSA4ieKtWEGYXqlu9ixq72lpg/mIZoTldIKLCDjQMWNGmSEEb1N6w4zwS//k/jI4yYQ08xCiss96JvEx6QQwEZGM0+B/vI2NurNSXRFqqhqh4mtWBi9YUpCX0fH99QobuzvJ/NvOkKghQcjSPASOVzUUkEOGF2jt1PzxpDUNwSml/6BBeKHyMUEvszv7P42CA2RMszOharoaXdfT8SoN/hSy7AcfjmvNQxH5LCvJM3itOFhdS9pyKRhEHzCSFy0/g/Zt+QZiJ5WhQSSWYll0RfAJYoSs8lFyTpFwAq+ZUvpBu0bDEt8P/ZvYAKx919P0Qo+DLwU2uTcwUcBHRQ8+6EmAJNvNte1SqGMIK1WIh36kO8SBg0jEyVi0sAoGnKW7Im0Dro25MOLr2AeX7DY3imwfvone1eRdErZl7XassnZgJF08gs34GxweDcgm3f3AmJmoJX8wJtojObf5VvABFnw2RBXUBY2QO90/hoY6Ca94CvEgBXaIG8lMlvgQ5YSOEACEmnhESHtlJC2+37w3ffw1rIEZbvwKVqS8Mpwk3DAjYX4CLaB+PUhRtOqE1cbkr5cqhrLIbqs1C4gGiqHzC4gyIbs69qwql5gt7GvClFUObfyL8DsXjQPuigYsNQgVojPgDCnrV8Ea4OfFGIAa0oWEm5jPGoeC8N9LFpI77sjVOnS+wFAOMKmZWIN4m8rbpdS/yN/2KtkX2mI1cP5rFbXU4wdUbIiL/yJwfyVkWux4VuMxx09uaBv6NxqrSgDq/2jS6y04WoVtgN01TPwGVSBY/DFUF3TkB21WCeqZuCoVn3OvAOc4RahxJ5U2qMI3Q+8G56U3RtbnBafLxUhJiAx1Db2qDnxqizXmAF0wp4s7A6V7xB9xZAlv3Fh7Q7ALwEWQxDhnwoRCectyFWD4LCp8hvUrccjX2MsBwoHAZaeIdZaYg/mAWlzQkpd2rqiw1fyBhzRnCMNAO0VbfNIT+LO81muFQlhLARklWiSVHXgTdBqsmL+GMsyr2BgjJPbRaUEWW5YZ6PN6hr0diHdRbzSsnTUfhuG24nGC6FhLlT0XjpW8wu/Ln3yxtAhQElMja3lBr5Svew5okOu3bpB3QnUy0ps4WAamoJF7pIcGMwoBY3TO4+uu/Zy19YWHB2q693nbdWnVLfYqSLwcLdhlVihKKk6QgsKMFmijkFjaxF4wQrnwubOJ55WaInnmF8XNzbaXdfeoJpLaqghgV0AgXETgi+6QCAFD0havunAeEFhWktbt53myh1z5yuNuJcrwl3gKtKre38uQ8xhUy6kkm472IHb1tLx8NB7sZQl4siAGV9dFF/PwURxIFrQKBwKHa/Zn/s/TdAxAeMK+L3u6j155N5NLjpEF68hsJAP6iq+qTWutYRx6eCOJwlfsV5Y++L1zKWor/lKbhqSJ3kwS0J42mpQEQG9IZOOT0Yo6unxfrNwf0H/DfRwK9wCAZtrW9FQWNkN4Z82baFrujEajpG8YGXtsK7dnp2KauKIET/mdgvoPzH1n2NW2j51q6Ul9aWY+tI29o3oiEU/stEMorph9jDmRqT457Ol1u7aqUN4dFvPCm97Dat/6NCOuO0E4v/6TKE6vJPpoj3or/0eYqfniAhbHFOv9PJnsMcTrluJM+ipGo8hlBf2R5kXBtfPN4/INLvb9JNSu0flvfql1Xbxiyvs4mhV2UYMxk2QDhj5Lry5pYLa0LyE3uDlth+NoxT38lCub/JZ9w8P/c37kQOX0IOzex67+P3CgaOX285R+hH4oiAph95HuxERAuExftHv7arf+b10a5gKb2knA02EeASVekjKtY3ZSzp2caBNG/FDLY1HevdvA82+H3KWhEOzGbl5/nEXxS20c/7vlX7aT/9oDl3otGQL9o3awr5rsztkz5Vihk47LGWe9ufpzpM26if+cPcFR4xIR+mK/etvf+9yd/Bo99claxLg2V8Pv7/tT7SohiXN2Z9Rh9Ppkf//KP4NUEsDBBQAAAAIANKs81xeWuOsTw8AAEo0AAAfAAAAY29uY3JldGUtcmVzdXJmYWNpbmctZ3VpZGUuaHRtbOVb25LbxhF9z1dMoCq/mCCXK1mXFZfy6mY5Jdlryy5VJeVyDYEhOVoAA2EGy2UcVeUp76nKT+QL8u5P8ZfkdM8ABLjcXW0sqRKn4qxJYC493ae7T/fQk9+nJnHrUomly7PphP6KTBaLw0gV8fcvIzxSMp1OcuWkSJayssodRrWbx3ej8LSQuTqMTrValaZykUhM4VSBUSuduuVhqk51omL+MhC60E7LLLaJzNThGGs47TI1fSQL8cgUSaWcEg+V+FbZuprLRKUPxHcrjZeYp6x4ZnJlVoWqxBe1TpX4i3gsTwykaCZPRn7BrmypskmlS6dN0RHvSJSVTJyGJL0tlu0WC97CGZrjJauCWLpYiEQWqU6lU3aAlVQpK0k7DESCZU/w8IUuCmVJOHVWGkxUAzGHAuwSmjRQCsbkUpM4skiUwHrYoMxw6hwSipWsCtrI6kVhh311V2ZmnO2cRhepOhvMTZaZ1SCXZ7HO5ULFEIwsc5DJaqH4uS10WSp3EI/56ymOaNph8bi/jazd0lSdbba03doJcvZnuiUOEScm602/Mb65n+7fwdBMFyc4bXYYQY+mICtEYlmp+WG0dK60B6PR7b29z+7ey2d5PFOqHC60W9azoTajlIWIG6vEHauMdj2M2ZBDAndvZ5k5VRWwoN+5xX1tP7ooOiFs+k3n8pS+Du3pIhLknHhNxhzhwadnWxOtW2fKLpVyzXT/ZJhY++D0cH9v//benfG9WFkLC8D1bG86DI+tCpW47SPPYTM7XBizyJQsNRY0+fWmWgeHSHgefMJYayq90EVY4+rdRjjC/oO5zHW2Pnz84tOXsrAHq8XSfX5rb+/+Z/g/zHL/zt7eJ2HMC1lUplR+THh3/y7ep9rCrdaHdiXL6JzeAm5Lmlu59WFkFgek9g5uZYWTZGrnUKud+pFAfz036W9HMasz/7JweHRZQNy5+m8q/vVOVldZ50Qf2FvPb89uuUMAfm6HpTpTmYdyuTTO2NH49nj/5s29OyP/KubHcfN0+LpUiweIueYQc6BTaz+ReXk/sYdOF2tbLWb8fXU4xhEvlugAga0LpsxYJSi+CzP31lHpxqYBWVvhe6UdguNBIqu0s5St81xW6x85nfzojz+deHSFUCXLMgOmCAqjLP30tQXopj9Fn/MaZy46aLVkE+QIOTTVIhpEny8qWS6jgz9hKDvfQXQUnA4vddqZ9yHMe0O2mxHhQYQiCf5zNxz0SMfB/5yzDSJyrQ+rc1ISTnRczzKIqcjElK7ivTvx+F54+cKkeq7Pv9PFc2TrmvB3EKjqoGErBz+9D8DcmNUWKLA2ejuIyiDjB1mczPIEudmtv54f84l++hiIX6lZSbu9fTvY+NwrNWMRBh9Tgo8ENs7Rlzv1tUqN34CTX9vFtD1GpPx6/r78ABAg/kRuIGemdu/fv7roflghtidVnc+ea+voOE7l9PFJxgrqpR96/iXeYxh0rb2Nxy2MCB5hhV8rbdSVcee2+xv07qCUbc55H8Jc5Udvf+hK+/TomxAvNlGsp8VvamX5DD3/M1mHgMw2XgAfpDieJKp0Kj0q7CqE3IYS+CeDKFCJlzCC0zm4Vk8f2oqFgr/JLFvTPhbSV+A8q6UqBCpTuA+0zJ6QyRkNR60yy7zDpJCp0sb7Hr2jk2Ed6XhqEHQoXsjXphJWOefBMxBgDqdYdCB8vYHT4HVCy1iBoVLMpc5o15kEIcvlGud+U+tKdZ102Ifsef290lnWCxvWmVKoU1WtfaAQ88rkGOFq9vbrafQr00YU2AnuX0mEE8SsJc6PJxTfThUdJzenHLR4yxUJVZAQgippnBozKlMvlkPxiEfQfgOaFJTVCXAhTsmMjJJQbMN86fVml6YGWIARKDWpUcXSl7mB0qyifUgGKezaAvtX645OEZaUnbjMPJwZaLM4HRWbWUvSXk+F38kTBYUg0HvWT6ybkDOvoaMAHz5ywsR8M6gJ89QcYxypdEEhPa2AQHiZkFASvjvYxEcGy+vIYg11ArLAumSFENCQHUgfP+B/k5FPU9PJyLfzZiZdTycSEuCQoPUnuoypKm8q+RuE+Wj6Es9DtiL+PxnJ6e+4IQiVNVMRc2L/KBI6ReVgSpQEqT5tRtBkrIYphTyNV1By1Nl6hrOkzbbcxPJhBmfVMoZ3UrF+STnNRqQa5HTRWzJGnYLjUNXz0JwdRntiT9y+hX/CykudpqqAuFVN00vplgLSvxjviVv3xP5dMb69HN99jg+37j0b7/0RY0Y0KAwNW9EmMSEDuYOn3+Tpt+6I8d0Ma3wW38NCz25251MbB/KWssBfV5liMfXnwxv/dWJzRK7pruNiDL/Dv3kBWGQyq52DEzUiqaKOAeYFNRR8SeYHhIPDu6AelVKfKbMqPCUjVSaz1NbRVOLFMFbUiBk2u/xLi4gqNoiX0fQFJGnl9DJMJ1iWYdLdppnZe9a1/7F/QQDSCw4MDKFt0NywqqJmswVywydW0I6RCygRATOafuE/XDQOxXVCNGJ67D/0xl2VKoNq66ri4pm57pRz9UXbzeWbaIqcetF7DgDt6cQRvoahDfY9Fvy/YsbKeee6QWExp77n9GmF2P4kfOWlRlAy/sKBQ7RQVc+dZy2Hshf4+U7bRFMiTLSD8GjZ4YWjgBY/Ynox1WlR5aXkvxSxGFk+dE1C5m1R6VUWkxEQryrjuTh/xGidI49Wycds4dzd2wNCsnMNGilWpvI58cJejZgrlyw55mvq/Cz1YnlR1O2dPDHlmsJdM0yt1awyK5FhARdNL6laEL6mk+V4egV9A2bGWH9jvK0CB98LnFM2jIsJ2ArMtDlbnIFFZGKlZDUgHAvtiIQVxtEk1PcuwUPkaCJNUlc+//eYFd4hjBrPjao6ARFCRdZQj6H4bkkEkUsxRMMMarKghmAG7ZFb3qHOZA4tNqwAVRY4ud+RWdKQ1dKqM3SRYuqkUcwgikOEZS0uS2E//0u8rGdQCDfoQTXrkgqzVPyhxpfxvYGgwox3usDRF7DIpX4eRGG9daQ4aikO+34HPy1qGN7QPhZ5jgcFETAwTjC6DWmCxPSYFldp7Zt/0Hho+d1n40EAQAE7YaC0QR8xOUmm6BlAfzLsefQouDBO7dV6uVOHd+/kBosKNSYPPO8L8AIia7qyDrVAoi0W9eDfR+Blzto6IsPU8+0O0hr2BV/YJ1/YKk0AN0dZJxWG+HJbizQeRQAFGHMFlsfEES9SpnsNk2SnmcGRiIrQA3KpQNthb9QvKIiOOI4MyNGggJS8gm9d01Z4qkCwNVjpUoLTtz5JTjSAR+iMH7Yeml9U8dDaO2oeWp8MoItaNeVCXRB5JMbacFXyVughk2vvTN74/Gd5c/qSWhV0EuyPZDwHXD24ZAe6GDeps21UJEuVnFBNwddW05fh1IFd074caAmisNZkhDE8jvTFPo4IXFNNg2BclooqoWQz7IUuSBleY565t++OhDU46EZ1BiHLa69Rkxc8jH/cEHyusihKzsg69Cj1g0Z1Nr3AOc75hP9KVRTcxl7pGJuBl3vFM6QJwlrjE740bhLD/vQp1YVvQsll/VE8GGH7is8GIelCuHUM72gM202d58s6AixX3XNaoAH9oG18sXW40wUuS+GHiiOPLkQnk25hqT1Ne9gS+cERhdkEF8++v7QbH/OgfbBh5uX0yBfAba3WegNL1DgE2RCBmC5CglTZmp4DwsBLHtSzlRspTCYGbDFxQfxWtm0hyRhcc68k6YcrxJ6YxxQzsCy/RwmJtGZLgiGV0Uu6vmF5S0MgzkypWGTOr6FHkum5ooAD9+B+SLAUSNEVsnGRDXDIjKjiGnZsohiHt76Y1K0kLSIwQUyZYv3QX9gk9SZSkISQvWBHUb0OQmikpO+iN227jRxOXX0LQ52QYSXXA9JPRog/wUfaiZWGeA9zW6dKBF6gL9XzuSKO38QSX6PP5zoRgBvSYt62Y7vtWQSCgiLNOyk0NeBk5xvAUFlfemL0f1Yx8LUSyRrLUE/YIAo2TpMq7dtG4J7d/gp06doEw+2UpuUCBW+L+I6h6J3Tc7Qr4hxvDNwEmVfgGo3heh0kWCDBcTrqDlFmazdYKaZLzSbYtSdCDnmUIeX6bEJJmwgjVFABn0ZnUGNmDPftyB8oAxXMgh0xRFA3u4neZOKKIOHzpkf1eSV290Z9OUe+bXZ/BNdxqofT0o9ooU6skt838TIYDRpZcsiUnLd83Gn4qqccNjcGclEGVPJkQzwulc8TSE+6bSPnk1OZ1SRpGw9LUBsbWlesom63yppmAX7V6/RBr4lnMxI8ytNHT3t2g69jWF/KIa9ndIWwieQ5/SINpjloHUR8RRIgEkIkTtzU98B+FAW9J0DNOfKDN2a3q8rhFh7huQAhDTADnJCkTNUd3vSU5e7LneH18vhcvrkqg9MQ0Cd/9s4Ieq6prxPtzudNfdcm7cbLvrdqXhPAqbFp25aooGZfh3h18zgl4DCcYBLa75ty4Je//sOXcKmWiwJFlPW1rgUCNAVK0toFSZvP53lcisIKvght+V8iXF2ONgMh5m/xtiBorFHLOf1c+7agp7H/7duAK3XTuQ348so7gJ5i/ot6/Fun/CiZ+clZmZGGZm02bkLHt6B8IS35HmW48g7VAGoyKxCpKoqzrz3R3crSlcqo+RFvmrltO7HhZd2Ga+guwqGxDzdQWvrWw/3iXN+VCd2OpdruiGd8VywCghgTQdyx0HFDHq9YgyRfyewkpj+7j/cyDGEshGFXrMosNYZKqnVMXNXuWPYpM1kewyszp9297G5cdZIyBb7pZA5msXU75B9dmLz4ba/27F8ONSMuuin6v777KXvA3/mrEh9OEfZDeCWTcvlB7brGVWyob2yn5MHngDTic8CIDoyO0dREdKopyd87reNdfZyumLa9nCES+Q7O/XiHQ7+TKx9ve/Cv893reu2r847a8aVGNY9MDnuu+9q48ueoOxvs56MA/6omTDmiz6IB3BUXY8eUssTiHa/HvvYR/dwV2UV3W30NtESdOsWhBmKMH3dazOBWWb8BzXc0IXKFK4KtLvOmvRz67yHr+G6zOA7fbK3B6MC2XEuybD/7N/k9lCaBrJ6/hbosxM2Mc/wbep728z/DRRjdWa1RUUSNY192VzAUR8Tn6LbGkuXhSdz08JI0Wr/Bl/APmWgZQYTvl7/9vRvFvUTtL3f55st/Hr6+6D8bgDfMac7mtwT+VwQj/k+H/g1QSwECFAMUAAAACADSrPNcAptvFf0KAABXIQAACgAAAAAAAAAAAAAAgAEAAAAAYWJvdXQuaHRtbFBLAQIUAxQAAAAIANKs81xeWuOsTw8AAEo0AAAfAAAAAAAAAAAAAACAASULAABjb25jcmV0ZS1yZXN1cmZhY2luZy1ndWlkZS5odG1sUEsFBgAAAAACAAIAhQAAALEaAAAAAA=='
CSS_APPEND = '\n/* Search Essentials content enhancements */\n.article-meta{max-width:760px;margin:14px 0 0;color:rgba(255,255,255,.78);font-size:.78rem;font-weight:700;letter-spacing:.02em}\n.guide-callout{margin-top:34px;padding:20px 22px;border-left:5px solid var(--gold);border-radius:12px;background:var(--cream);color:var(--ink)}\n.guide-callout strong{color:var(--forest)}\n.guide-hero .service-page-copy,.about-hero .service-page-copy{padding-block:105px}\n.about-hero{min-height:560px;background:linear-gradient(135deg,#132d27,#0b211b)}\n.about-hero:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 80% 20%,rgba(209,164,81,.24),transparent 34%)}\n.about-hero .service-page-copy{position:relative;z-index:2}\n.about-hero h1{max-width:950px}\n@media(max-width:700px){.article-meta{font-size:.72rem}.guide-callout{padding:17px}.guide-hero .service-page-copy,.about-hero .service-page-copy{padding-block:75px}}\n'

if not DIST.is_dir():
    raise RuntimeError("dist directory missing; run the site generator first")

archive_bytes = base64.b64decode(ARCHIVE_B64, validate=True)
if hashlib.sha256(archive_bytes).hexdigest() != ARCHIVE_SHA256:
    raise RuntimeError("Search Essentials patch archive checksum mismatch")
with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
    bad = archive.testzip()
    if bad:
        raise RuntimeError(f"Corrupt Search Essentials patch member: {bad}")
    archive.extractall(DIST)

h1_updates = {
    "index.html": ("<h1>Restore your concrete.<br><em>Upgrade your home.</em></h1>", "<h1>Residential concrete resurfacing in the Twin Cities.<br><em>Restore your concrete. Upgrade your home.</em></h1>"),
    "driveway-resurfacing.html": ("<h1>Renew a worn driveway without assuming it must be torn out.</h1>", "<h1>Driveway resurfacing in the Twin Cities for worn residential concrete.</h1>"),
    "patio-resurfacing.html": ("<h1>Turn an aging concrete patio into a more inviting outdoor space.</h1>", "<h1>Patio resurfacing in the Twin Cities for a more inviting outdoor space.</h1>"),
    "pool-deck-resurfacing.html": ("<h1>Refresh the concrete around your pool with appearance and footing in mind.</h1>", "<h1>Pool deck resurfacing in the Twin Cities with appearance and footing in mind.</h1>"),
    "sidewalk-walkway-resurfacing.html": ("<h1>Create a cleaner, more welcoming path through your property.</h1>", "<h1>Sidewalk and walkway resurfacing in the Twin Cities.</h1>"),
    "front-entry-steps-resurfacing.html": ("<h1>Improve the first impression of your home from the ground up.</h1>", "<h1>Front entry and concrete step resurfacing in the Twin Cities.</h1>"),
}

for name, (old_h1, new_h1) in h1_updates.items():
    path = DIST / name
    text = path.read_text(encoding="utf-8")
    text = text.replace('<html lang="en">', '<html lang="en-US">', 1)
    text = text.replace(old_h1, new_h1, 1)
    text = text.replace(
        '<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">',
        '<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">\n  <meta name="author" content="Dakota Concrete Resurfacing">',
        1,
    )
    if name == "index.html":
        text = text.replace('<a href="#faq">FAQ</a>', '<a href="concrete-resurfacing-guide.html">Guide</a><a href="#faq">FAQ</a>', 1)
        text = text.replace(
            '<p>Resurfacing is a finish system installed over an existing slab. It can improve appearance and address surface-level wear, but it does not correct a failing base, major settlement or ongoing structural movement.</p>',
            '<p>Resurfacing is a finish system installed over an existing slab. It can improve appearance and address surface-level wear, but it does not correct a failing base, major settlement or ongoing structural movement.</p><a class="text-link" href="concrete-resurfacing-guide.html">Read the concrete resurfacing homeowner guide →</a>',
            1,
        )
    else:
        text = text.replace('<a href="index.html#faq">FAQ</a>', '<a href="concrete-resurfacing-guide.html">Guide</a><a href="index.html#faq">FAQ</a>', 1)
    text = text.replace('<h3>Company</h3>', '<h3>Company</h3><a href="concrete-resurfacing-guide.html">Concrete resurfacing guide</a><a href="about.html">About Dakota</a>', 1)
    path.write_text(text, encoding="utf-8")

styles = DIST / "styles.css"
css = styles.read_text(encoding="utf-8")
if "/* Search Essentials content enhancements */" not in css:
    styles.write_text(css + CSS_APPEND, encoding="utf-8")

base = "https://600589mbm-beep.github.io/dakota-concrete-resurfacing/"
entries = [
    ("", "weekly", "1.0"),
    ("concrete-resurfacing-guide.html", "monthly", "0.9"),
    ("driveway-resurfacing.html", "monthly", "0.8"),
    ("patio-resurfacing.html", "monthly", "0.8"),
    ("pool-deck-resurfacing.html", "monthly", "0.8"),
    ("sidewalk-walkway-resurfacing.html", "monthly", "0.8"),
    ("front-entry-steps-resurfacing.html", "monthly", "0.8"),
    ("about.html", "yearly", "0.5"),
]
urls = []
for rel, frequency, priority in entries:
    urls.append(f"  <url>\n    <loc>{base}{rel}</loc>\n    <lastmod>2026-07-19</lastmod>\n    <changefreq>{frequency}</changefreq>\n    <priority>{priority}</priority>\n  </url>")
(DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")

required = ["about.html", "concrete-resurfacing-guide.html", "sitemap.xml"]
missing = [name for name in required if not (DIST / name).is_file()]
if missing:
    raise RuntimeError(f"Search Essentials patch missing: {', '.join(missing)}")
print("Applied Google Search Essentials enhancements")