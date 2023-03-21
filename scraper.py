from bs4 import BeautifulSoup
import requests
from github import Github

# Github credentials
filename = "test.txt"


def readGithub():
    return repository.get_contents(filename).decoded_content.decode()


def writeGithub(currentLast):
    contents = repository.get_contents(filename)
    repository.update_file(
        contents.path, "updated last scrape", currentLast, contents.sha
    )


# completes the link if it is a relative link
def linkChecker(linkStr):
    if linkStr.startswith("/tr"):
        linkStr = "https://oidb.hacettepe.edu.tr" + linkStr
        return linkStr

    else:
        return linkStr


def updateLastChecked(duyuruList):
    if len(duyuruList) == 0:
        return

    else:
        writeGithub(duyuruList[0].partition("\n")[0])


def scrape():
    duyuruList = []
    lastScraped = readGithub()
    page = requests.get("https://oidb.hacettepe.edu.tr/")
    soup = BeautifulSoup(page.text, "lxml")

    duyurular = soup.find_all("div", class_="duyuru")

    for duyuru in duyurular:
        duyuruBaslik = duyuru.find("a").text

        if lastScraped != duyuruBaslik:
            duyuruLink = linkChecker(duyuru.find("a").get("href"))
            duyuruTarih = duyuru.find("div", class_="duyuru_tarih").text
            duyuruList.append(
                f"{duyuruBaslik}\n\n{duyuruLink}\n\n{duyuruTarih[0:10]} - {duyuruTarih[11:16]}"
            )

        else:
            break

    updateLastChecked(duyuruList)

    return duyuruList
