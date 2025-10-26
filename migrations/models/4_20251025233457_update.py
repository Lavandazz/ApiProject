from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "article" ADD "author_id" INT NOT NULL;
        ALTER TABLE "article" ADD CONSTRAINT "fk_article_user_8c489e15" FOREIGN KEY ("author_id") REFERENCES "user" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "article" DROP CONSTRAINT IF EXISTS "fk_article_user_8c489e15";
        ALTER TABLE "article" DROP COLUMN "author_id";"""


MODELS_STATE = (
    "eJztmltz2joQgP+Kh6d0JqdjHFPoeYOEnHKaQCchbaeX8QhbgCe2RG25CdPJfz+SfJF8LW"
    "5MAie8eGC1a60+i/Xuol8tF1vQ8V/3PWKbDmz9rfxqIeCyD9mhY6UFVisxwAQEzLhRC0hK"
    "M594wCRUPAeOD6nIgr7p2StiY8SUvwWq3jbZ9QTyq86vHX6dsatuKvzLXCjpbX7VuERlE1"
    "nYpDPZaNHgPQNk/wigQfACkiX06J2/fqdiG1nwHvrx19WtMbehY6Vw2Ra7AZcbZL3ishEi"
    "51yRuTszTOwELhLKqzVZYpRo24gw6QIi6AEC2e2JFzCAKHCcCHXMNPRUqIQuSjYWnIPAYY"
    "+BWeeeQiyUIEYiEyP2BKk3Pl/ggs3yl9bWu3rv5I3eoyrck0TSfQiXJ9YeGnIC42nrgY8D"
    "AkINjlFwIzYJN04a3ekSeMXsEoMMPup0Fl8Mq4pfLBAAxbZtiKAL7g0HogVZ0q/tjlrB62"
    "P/6vRd/+qIar1iq8H0pxT+xMbRkBaOMagCouxZDuUU3pdsw4zZvgCt4Dcdfp4yp13f/+HI"
    "2I4u+585UXcdjVxMxv/E6hLm04vJIEPX9CBbvwFIHu4ZHSG2C4sBpy0zfK3I9HX8YTdpt+"
    "garAly1lFsqaI/uhxeT/uXH1KP4Kw/HbIRLYU/lh69yWz05CbKp9H0ncK+Kl8m4yEniH2y"
    "8PiMQm/6pcV8AgHBBsJ3BrCkMBhLYzCpB0sHl9gzaoXulM3vI/iOPMMGgjh7881vC2N4yC"
    "QP8Rx70F6g93DNWY6oTwCZRcE7SjZufLjbMUdIxRbzwF2SD6S3B10gXRYk4Rutf33aPxu2"
    "OMgZMG/vgGcZKaJsBGs4I0l080Ou5mYlAIEFJ8DWwbyO0A4cehvH9inUKb6FqCjXy+lUJn"
    "0zoU0S7QazP10SzRWRsEXJG7fQ1TB541dLulP4uScba9KkIKeqhpNqoW5XjOvSzXXuzclb"
    "RbgWzRGlkpvMFMq1R+Sw/3My31DJKiORKhPJre8tl/dkiZT5Rz7HM2XXEvrUU6RhabZwRZ"
    "EXksupQqJXY6V5x+SpwweZ3gyHKuV5qpQ4wG2aWicGh6RaJNW5FOJ5XoVXuLjVweWVrzwP"
    "N97kSAWkKMooR9xclQxNKf5Yx9yyPc9aRtGwmwtxqhSSUi68+vO30A44fgiETx4I41/Apt"
    "2aWL+ZMLh1eulWjbpRq0ataNWovFVTI+4J0gGthfw86kFkdv7+CjqgpHUjlVNxUNvZN06u"
    "pHrYZuznFWZB7I8rz/LYH8Qa22lw/2EgnDfTCn/M7Ico/ORRmO1F/rlGJJZt9jEab9Q3r2"
    "ib57vmdQk2S++p/3honp8f1N6Eksl+UuxuQrFbTrGbo7gCxMNo7dpmHZBpqwPLkCV0ge3U"
    "wZgY7GNE1Dob8NM6pfzYUHYv+v4d9greylU7Udjs5z5sLM+XUdq+QZNE+2dBeBxgmpMDVJ"
    "LlyHYZnjNquC2gyU5tuns0mEwuUt2jwSjbHrq5HAwpYI6XKtnhHyYlfzttUjtF51EeWT5J"
    "R192bwuXVk/yJmTV96GG3EYNWdZDlHFV15L1eolaW/pfYC7KtAZrOUX++6KguVdYae6IX4"
    "ca9Fk6gfWOTkgWL+nghByQ2Q+/HjTJ4iVBqzhtEjfiXvxZE2lrFJ80yaYCDVDbv1QgS02K"
    "Qrt0PqcPPdtcFqUU0UhlQgGEzu/SiXKgh5fok79Ef0LPLzy0W15vSyb7WW5rnc36FlWNi1"
    "zngv00akCM1PcT4Fb6FXRGAlHBCed/ryfjktPNwiQD8gbRBX61bJMcK+yE4PfdxFpBka26"
    "+sxL9njLcfp4MrvBs595efgPPCdW2g=="
)
