class ParserSettings:
    xpath_urls = [
        "//a/@href", "//audio/@src", "//button/@formaction", "//img/@src", "//link/@href", "//script/@src",
        "//video/@src", "//source/@src", "//track/@src", "//embed/@src", "//object/@data"
    ]
    xpath_headlines = [
        "//h1", "//h2", "//h3", "//h4", "//h5", "//h6"
    ]
