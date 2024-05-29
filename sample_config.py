#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = "7337806154:AAHCaq6_zvgSVb56fsQa_68YLJY9RbtlP1Y"

    # Get from my.telegram.org
    APP_ID = int(20839691)

    # Get from my.telegram.org
    API_HASH = "d3811826548276448c7065125d3034a3"

    # Generate a user session string
    TG_USER_SESSION = "1BVtsOIABu1o4NTTLNOm76cUnkX9rk2KQ8iboPGS7fOKbmOdCJ9joAI48e5R6EU3P_5WD6jnFrrNqbEv2N8tu7blBCBzIlc9vzZPPVG_SRxVHJdUFpe0B18qrssYYUgnHPU6eukMd4py9OvJpkbkYesdtei7C3h0279l8zUxZHxsGacrxWwileNKz1PXdkmSvf7nQkuFmSw7zpnIF6RauCINiX3FkwGJ08zJ79uMcFirTDCaL7PXqrY3PJHCHMGl-PpZ8uctj77yviPz3E3tjX8_KWKP5GJrlz30_fSSrW61lK9yTeSfh43dbjwvyJ_30Paa50rbYSiHEXf6msLGMe_2gt0q-29w="

    # Database URI
    DB_URI = "-4065852557"


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
