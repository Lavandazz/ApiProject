from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "name" VARCHAR(50) NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP COLUMN "name";"""


MODELS_STATE = (
    "eJztmm1zmzgQgP8Kw6d0JtfBBNfufbMd55prYt8kzrXTl2FkkG0mILkgmng6+e8nCbDEa6"
    "HFiT3nLwxe7aLdB2Wl3fBD9bAN3eD1wCeO5UL1T+WHioDHbrJDp4oK1msxwAQEzLmRCiSl"
    "eUB8YBEqXgA3gFRkw8DynTVxMKJSFLouE2KLKjpoKUQhcr6F0CR4CckK+nTg81cqdpANH2"
    "GQ/FzfmwsHunbKWcdmc3O5STZrLrtE5IIrstnmpoXd0ENCeb0hK4y22g4iTLqECPqAQPZ4"
    "4ofMfeZdHGgSUeSpUIlclGxsuAChS6RwazKwMGL8qDcBD3DJZvlD7xg9o3/2xuhTFe7JVt"
    "J7isITsUeGnMBkpj7xcUBApMExCm7EIdFrS6MbrYBfzG5rkMFHnc7iS2BV8UsEAqBYNC0R"
    "9MCj6UK0JCv6s9PVKnj9O7gZvRvcnFCtVywaTBdytMAn8ZAejTGoAqLsWQ7lDD6WLMOM2a"
    "EAreA3G3+cMae9IPjmythOrgcfOVFvE49cTSd/JeoS5tHVdJiha/mQxW8Ckod7TkeI48Fi"
    "wGnLDF87Nn2d3OwnbZXGYE+Ru4lzSxX9y+vx7Wxw/U/qFZwPZmM2oqfwJ9KTN5mFvn2I8u"
    "Fy9k5hP5VP08mYE8QBWfp8RqE3+6Qyn0BIsInwgwlsKQ0m0gTME0vgi3spFTHBHFj3D8C3"
    "zdwI1nGZbn7I072sBCCw5K+FwWVuxpva0KWPcZ2AvukZvoeoaOPL6VTugHOhTbbaP9sK1S"
    "+hZnQsdj2D/Grwa5df5+xqWIo0EIkWXGR0hJ3BLQyNS6KrLT0puu/Lxro0KcipatGkeqTb"
    "E+OG9HCDe3P2VhGuxXN0oinqzASliQqCjEWaDCQX3lsu78uSyHghuRxPlAslcqmvSMPSbF"
    "FAsReSx0mIknGTQGXH5Kmj95heC2omTxwXzXHR1Fo0x+P08x+nk9Rf9wy4NTie/sTpb08O"
    "CTe4uCLm8srDgI9r1sL1c3kqIcVZRjnh5ppkaEn5xz7llp1F1jLOhr1citOklJRy4dWvb0"
    "J74PgxET57Ikz+Auq2FRL9dtLgzumlewparZ6CVtFT0HhPoUHeE6TDAPpBHvUwNrt4fwNd"
    "UNJjiBPaHX1EktT2dscR0qQS3mXuZ0iKcj+XV+b+MNFosfj7/US4+I0qoqXZj1n42bMwW4"
    "v8vkEmlm0OMRvXavBW9Hfz7d2mBNul99wd8vb5BWHjRSiZHCbFXh2KvXKKvRzFNSA+RhvP"
    "sZqATFsdWUYsoQcctwnGrcEhZkS9W4Of3i3lx4ayazEIHrBfsCtXrURhc5jrsLVzvozSCU"
    "x6SHS+F6THIaZncoBKTjmyXYbnnBruCuh2pbbdPRpOp1ep7tHwMtseursejilgjpcqOQSK"
    "Y9Av1U6s6jzWTruoncp6ZzKu6hqqWQ9N70j98IUoT1qsYRS5bV/Q1CqssPbEr2Pt9SIdML"
    "MRPMni5wT3I7+0AzFdsDaDJln8n6Dltrs0wzzAC+xDZ4neww3neEk9AsgqOj1kOl37x69s"
    "U6NiHzxsU5i8NGh4NCgYHRhGg9vR4HysplZeccO6MbXDOwpkqUlZqJjay/wzbgB9x1oVHS"
    "nikcoDBRA6x89T9yyVVW2i36EfFH5VWV5nSiaHWWbq3Xr1elXBnqvY2Z9GA4ix+mEC3Emd"
    "TmckEBV8gvr37XRS8vmpMMmAvEM0wM+2Y5FThX0z+HU/sVZQZFFXf+uR/azjNP39KHvAi3"
    "/r8fQftu9dRA=="
)
