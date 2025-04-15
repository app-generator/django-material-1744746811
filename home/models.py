# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Stocks(models.Model):

    #__Stocks_FIELDS__
    year = models.IntegerField(null=True, blank=True)
    company = models.TextField(max_length=255, null=True, blank=True)
    term = models.IntegerField(null=True, blank=True)
    donenvarliklar = models.IntegerField(null=True, blank=True)
    nakitvenakitbenzeri = models.IntegerField(null=True, blank=True)
    finansalyatirimlar = models.IntegerField(null=True, blank=True)
    ticarialacaklar = models.IntegerField(null=True, blank=True)
    finanssektorufaaliyetlerindenalacaklar = models.IntegerField(null=True, blank=True)
    digeralacaklar = models.IntegerField(null=True, blank=True)
    musterisozlesmesindendoganalacaklar = models.IntegerField(null=True, blank=True)
    stoklar = models.IntegerField(null=True, blank=True)
    canlivariklar = models.IntegerField(null=True, blank=True)
    digerdonenvarliklar = models.IntegerField(null=True, blank=True)
    satisamaciyladuranvarliklar = models.IntegerField(null=True, blank=True)
    duranvarliklar = models.IntegerField(null=True, blank=True)
    dticarialacaklar = models.IntegerField(null=True, blank=True)
    dfinanssektorualacaklar = models.IntegerField(null=True, blank=True)
    ddigeralacaklar = models.IntegerField(null=True, blank=True)
    dmusterisozlesmesindendoganalacaklar = models.IntegerField(null=True, blank=True)
    dfinansalyatirimlar = models.IntegerField(null=True, blank=True)
    dozkaynakyontemiyledegerlenenyatirimlar = models.IntegerField(null=True, blank=True)
    dcanlivarliklar = models.IntegerField(null=True, blank=True)
    dyatirimamaclıgayrimenkuller = models.IntegerField(null=True, blank=True)
    dstoklar = models.IntegerField(null=True, blank=True)
    dkullanımhakkivarliklari = models.IntegerField(null=True, blank=True)
    dmaddiduranvarliklar = models.IntegerField(null=True, blank=True)
    dserefiye = models.IntegerField(null=True, blank=True)
    dmaddiolmayanduranvarliklar = models.IntegerField(null=True, blank=True)
    dertelenmisvergivarligi = models.IntegerField(null=True, blank=True)
    digerduranvarliklar = models.IntegerField(null=True, blank=True)
    toplamvarliklar = models.IntegerField(null=True, blank=True)
    kaynaklar = models.IntegerField(null=True, blank=True)
    kisavadeliyukumlulukler = models.IntegerField(null=True, blank=True)
    finansalborclar = models.IntegerField(null=True, blank=True)
    digerfinansalyukumlulukler = models.IntegerField(null=True, blank=True)
    ticariborclar = models.IntegerField(null=True, blank=True)
    digerborclar = models.IntegerField(null=True, blank=True)
    musterisozdoganyuk = models.IntegerField(null=True, blank=True)
    finanssektoruborclar = models.IntegerField(null=True, blank=True)
    devlettesvikveyardimlari = models.IntegerField(null=True, blank=True)
    ertelenmisgelirler = models.IntegerField(null=True, blank=True)
    donemkariveriyuk = models.IntegerField(null=True, blank=True)
    borckarsiliklari = models.IntegerField(null=True, blank=True)
    digerkisavadeliyuk = models.IntegerField(null=True, blank=True)
    satisamacliduranvarlikyuk = models.IntegerField(null=True, blank=True)
    uzunvadeliyuk = models.IntegerField(null=True, blank=True)
    ufinansalborclar = models.IntegerField(null=True, blank=True)
    udigerfinansalyukler = models.IntegerField(null=True, blank=True)
    uticariborclar = models.IntegerField(null=True, blank=True)
    udigerborclar = models.IntegerField(null=True, blank=True)
    umusterisozdogyuk = models.IntegerField(null=True, blank=True)
    ufinanssektoruborclar = models.IntegerField(null=True, blank=True)
    udevlettesvikyardimlari = models.IntegerField(null=True, blank=True)
    uertelenmisgelirler = models.IntegerField(null=True, blank=True)
    uzunvadelikarsiliklar = models.IntegerField(null=True, blank=True)
    calisanlarasaglananfaydakarsi = models.IntegerField(null=True, blank=True)
    ertelenmisvergiyuk = models.IntegerField(null=True, blank=True)
    digeruzunvadeliyuk = models.IntegerField(null=True, blank=True)
    ozkaynaklar = models.IntegerField(null=True, blank=True)
    anaortakligaaitozkaynaklar = models.IntegerField(null=True, blank=True)
    odenmissermaye = models.IntegerField(null=True, blank=True)
    karsilikliistiraksermayesiduzeltmesi = models.IntegerField(null=True, blank=True)
    hissesenediihracprimleri = models.IntegerField(null=True, blank=True)
    degerartisfonlari = models.IntegerField(null=True, blank=True)
    yabanciparacevrimfarklari = models.IntegerField(null=True, blank=True)
    kardanayrilankisitlanmisyedekler = models.IntegerField(null=True, blank=True)
    gecmisyillarkarzarar = models.IntegerField(null=True, blank=True)
    donemnetkarzarar = models.IntegerField(null=True, blank=True)
    digerozsermayekalemleri = models.IntegerField(null=True, blank=True)
    azinlikpaylari = models.IntegerField(null=True, blank=True)
    toplamkaynaklar = models.IntegerField(null=True, blank=True)
    surdurulenfaaliyetler = models.IntegerField(null=True, blank=True)
    satisgelirleri = models.IntegerField(null=True, blank=True)
    satislarinmaliyeti = models.IntegerField(null=True, blank=True)
    ticarifaaliyetlerdendigerkarzarar = models.IntegerField(null=True, blank=True)
    ticarifaaliyetlerdenbrutkarzarar = models.IntegerField(null=True, blank=True)
    fupkdigergelirler = models.IntegerField(null=True, blank=True)
    fupkdigergiderler = models.IntegerField(null=True, blank=True)
    finanssekdigerkarzarar = models.IntegerField(null=True, blank=True)
    finanssekbrutkarzarar = models.IntegerField(null=True, blank=True)
    digergelirgiderler = models.IntegerField(null=True, blank=True)
    brutkarzarar = models.IntegerField(null=True, blank=True)
    pazarlamasatisdagitimgiderleri = models.IntegerField(null=True, blank=True)
    genelyonetimgiderleri = models.IntegerField(null=True, blank=True)
    arastirmagelistirmegiderleri = models.IntegerField(null=True, blank=True)
    digerfaaliyetgelirleri = models.IntegerField(null=True, blank=True)
    digerfaaliyetgiderleri = models.IntegerField(null=True, blank=True)
    faaliyetkaridigergelirgider = models.IntegerField(null=True, blank=True)
    faaliyetkarizarar = models.IntegerField(null=True, blank=True)
    netfaaliyetkarzarar = models.IntegerField(null=True, blank=True)
    yatirimfaaliyetlergelirler = models.IntegerField(null=True, blank=True)
    yatirimfaaliyetlergiderler = models.IntegerField(null=True, blank=True)
    degerlenenyatirimkarzararpay = models.IntegerField(null=True, blank=True)
    finansmanoncesikarzarar = models.IntegerField(null=True, blank=True)
    efdfinansalgelirler = models.IntegerField(null=True, blank=True)
    efdffinansalgiderler = models.IntegerField(null=True, blank=True)
    vergioncesigelirgiderler = models.IntegerField(null=True, blank=True)
    surdurulenfaaliyetlervergikarzarar = models.IntegerField(null=True, blank=True)
    durdurulanfaaliyetler = models.IntegerField(null=True, blank=True)
    durdurulanfaaliyetvergisonrakarzarar = models.IntegerField(null=True, blank=True)
    donemkarzarar = models.IntegerField(null=True, blank=True)
    donemkarzarardagilimi = models.IntegerField(null=True, blank=True)
    anaortakliklpaylari = models.IntegerField(null=True, blank=True)
    hissebasınakazanc = models.IntegerField(null=True, blank=True)
    seyretilmishissebasinakazanc = models.IntegerField(null=True, blank=True)
    surdurulenfaaliyethissebasinakazanc = models.IntegerField(null=True, blank=True)
    surdurulenfaaliyetseyretilmishissebasinakazanc = models.IntegerField(null=True, blank=True)
    amortismangiderleri = models.IntegerField(null=True, blank=True)
    kidemtazminati = models.IntegerField(null=True, blank=True)
    finansgiderleri = models.IntegerField(null=True, blank=True)
    surdurulenfaaliyetlervergigelirgideri = models.IntegerField(null=True, blank=True)
    yurticisatislar = models.IntegerField(null=True, blank=True)
    yurtdisisatislar = models.IntegerField(null=True, blank=True)
    netyabancıparapozisyonu = models.IntegerField(null=True, blank=True)
    parasalnetyabanciparavarlikpozisyonu = models.IntegerField(null=True, blank=True)
    netypp = models.IntegerField(null=True, blank=True)
    isletmefaaliyetkaynaklanannetnakit = models.IntegerField(null=True, blank=True)
    duzeltmeoncesikar = models.IntegerField(null=True, blank=True)
    duzeltmeler = models.IntegerField(null=True, blank=True)
    amortismanitfapaylari = models.IntegerField(null=True, blank=True)
    karsiliklardakidegisim = models.IntegerField(null=True, blank=True)
    digergelirgider = models.IntegerField(null=True, blank=True)
    isletmesermayesindedegisikleroncesikar = models.IntegerField(null=True, blank=True)
    isletmesermayesindekidegisikler = models.IntegerField(null=True, blank=True)
    esasfaaliyetileolusannakit = models.IntegerField(null=True, blank=True)
    digerisletmefaaliyetlerindennakit = models.IntegerField(null=True, blank=True)
    sabitsermayeyatirimlari = models.IntegerField(null=True, blank=True)
    digeryatirimfaaliyetlerindennakit = models.IntegerField(null=True, blank=True)
    sabitsermayeyatirimlar = models.IntegerField(null=True, blank=True)
    diğeryatirimfaaliyetlerindennakit = models.IntegerField(null=True, blank=True)
    yatirimfaaliyetlerindenkaynaklanannakit = models.IntegerField(null=True, blank=True)
    serbestnakitakim = models.IntegerField(null=True, blank=True)
    finansalboırclardakidegisim = models.IntegerField(null=True, blank=True)
    temettüodemeleri = models.IntegerField(null=True, blank=True)
    sermayeartirimi = models.IntegerField(null=True, blank=True)
    digerfinansmanfaaliyetlerindennakit = models.IntegerField(null=True, blank=True)
    finansmanfaaliyetlerindenkaynaklanannakit = models.IntegerField(null=True, blank=True)
    yabparacevfarketkoncnaknakbenznetartisazalis = models.IntegerField(null=True, blank=True)
    yabparacevrimfarknakitvenakitbenzüzerindekietkisi = models.IntegerField(null=True, blank=True)
    digernalitgirisicikisi = models.IntegerField(null=True, blank=True)
    nakitvebenzerindekidegisim = models.IntegerField(null=True, blank=True)
    digernakitvenakitbenzerlerindekiartis = models.IntegerField(null=True, blank=True)
    donembasinakitdegerler = models.IntegerField(null=True, blank=True)
    donemsonunakit = models.IntegerField(null=True, blank=True)

    #__Stocks_FIELDS__END

    class Meta:
        verbose_name        = _("Stocks")
        verbose_name_plural = _("Stocks")


class Company(models.Model):

    #__Company_FIELDS__
    year = models.IntegerField(null=True, blank=True)
    company = models.TextField(max_length=255, null=True, blank=True)
    term = models.IntegerField(null=True, blank=True)

    #__Company_FIELDS__END

    class Meta:
        verbose_name        = _("Company")
        verbose_name_plural = _("Company")



#__MODELS__END
