import requests
import re

from bs4 import BeautifulSoup


def find_anime():
    main_url = "https://www.anime-planet.com/anime/"
    anime_to_find = input("Type full name of the anime:\n")
    anime_for_url = anime_to_find.strip().title().replace(" ", "-")
    search_url = main_url + anime_for_url
    req_answer = requests.get(search_url)

    global someSoup
    someSoup = BeautifulSoup(req_answer.content, 'html.parser')
    # print(search_url)

    if input("show request answer? yes/no:\n") == "yes":
        print(req_answer.status_code)

    if input("show the content of a response? yes/no\n") == "yes":
        print(req_answer.content)
        print(type(req_answer.content))

    if input("make content look pretty? yes/no\n") == "yes":
        print(someSoup.prettify())

    if input("what about children tags? yes/no\n") == "yes":
        print(type(someSoup.children))
        print(list(someSoup.children))

    get_details(someSoup)

    # html_content = list(someSoup.children)[3]
    # html_list = list(html_content.children)[3]
    # print(html_list)
    # for item in list(someSoup.children):
    #     print(type(item))
    # print(list(someSoup.children)[3])


def get_details(someSoup):
    some_data = someSoup.find("div", {"class": "pure-1 md-3-5"})
    episodes = someSoup.find("div", {"class": "pure-1 md-1-5"})
    episodes_number = re.sub("[^0-9]", "", episodes.find("span").getText())
    when_drawn = someSoup.find("span", {"class": "iconYear"})
    site_rating = someSoup.find("div", {"class": "avgRating"})
    tags_soup = someSoup.find("div", {"class": "tags"})
    anime_tags = tags_soup.find("ul").getText().replace(
        "\n\n\n\n", "\n").replace("\n", " ").strip()

    def print_good_line():
        if int(episodes_number) <= 12:
            print(
                "Here are {} episodes in this anime, maybe it has more seasons".format(
                    episodes_number),
            )
        else:
            print(
                "Here are {} episodes in this anime".format(episodes_number),
            )

    print("\nAbout the anime: \n", "\t", some_data.find("p").getText(), "\n")

    print_good_line()

    print("\nYears: ", when_drawn.getText())

    print("\nRating: ", site_rating.find("span").getText())

    print("\nTags:\n", anime_tags)


if __name__ == "__main__":
    find_anime()
