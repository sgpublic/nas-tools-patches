import log
from app.sites.siteconf import SiteConf
from app.helper import SiteHelper
from lxml import etree

log.info(f"【Plugin】加载 SiteConf Patch！")

SiteConf()._SITE_CHECKIN_XPATH.append('//a[@id="k_misign_topb"]')
SiteConf()._SITE_CHECKIN_XPATH.append('//i[@id="k_misign_topb"]//a')

SiteConf()._SITE_LOGIN_XPATH["captcha"].append('//input[contains(@id, "seccodeverify_")]')

SiteConf()._SITE_LOGIN_XPATH["captcha_img"].append('//span[contains(@id, "vseccode_")]//img/@src')

SiteConf()._SITE_LOGIN_XPATH["submit"].append('//button[@name="loginsubmit"]')

SiteConf()._SITE_LOGIN_XPATH["error"].append('//div[@id="ntcwin"]//div[contains(@class, "pc_inner")]/text()')

_SiteHelper_is_logged_in = SiteHelper.is_logged_in


def SiteHelper_is_logged_in(html_text=None):
    if _SiteHelper_is_logged_in(html_text) is True:
        return True
    html = etree.HTML(html_text)
    # 是否存在登出和用户面板等链接
    xpaths = [
        '//div[@id="main_succeed" and not(contains(@style, "none"))]',
        '//a[@id="myitem"]',
    ]
    for xpath in xpaths:
        if html.xpath(xpath):
            return True
    return False


SiteHelper.is_logged_in = SiteHelper_is_logged_in
