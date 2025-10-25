from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "blacklistedtoken" ALTER COLUMN "token" TYPE TEXT USING "token"::TEXT;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "blacklistedtoken" ALTER COLUMN "token" TYPE VARCHAR(200) USING "token"::VARCHAR(200);"""


MODELS_STATE = (
    "eJztmm1z2jgQgP+Kx5/SmVzHOKbQ+waEXHNN4CYh105fxiNsAZrYMrXlJkwn//0k2Ubya+"
    "0WEpjzFw+sdq3dx2K1WvxDdT0bOsHrgU+Q5UD1T+WHioHLPmSHThUVrNdigAkImHMjFUhK"
    "84D4wCJUvABOAKnIhoHlozVBHqZSHDoOE3oWVUR4KUQhRt9CaBJvCckK+nTg81cqRtiGjz"
    "BIvq7vzQWCjp1yFtlsbi43yWbNZZeYXHBFNtvctDwndLFQXm/IysNbbYQJky4hhj4gkN2e"
    "+CFzn3kXB5pEFHkqVCIXJRsbLkDoECncmgwsDzN+1JuAB7hks/yhd4ye0T97Y/SpCvdkK+"
    "k9ReGJ2CNDTmAyU5/4OCAg0uAYBTeCSPTY0uhGK+AXs9saZPBRp7P4ElhV/BKBACgWzY4I"
    "uuDRdCBekhX92ulqFbz+HdyM3g1uTqjWKxaNRxdytMAn8ZAejTGoAqLsWQ7lDD6WLMOM2b"
    "EAreA3G3+cMafdIPjmyNhOrgcfOVF3E49cTSd/JeoS5tHVdJiha/mQxW8Ckod7TkcIcmEx"
    "4LRlhq8dm75OPhwmbZXGYE+xs4lzSxX9y+vx7Wxw/U/qEZwPZmM2oqfwJ9KTN5mFvr2J8u"
    "Fy9k5hX5VP08mYE/QCsvT5jEJv9kllPoGQeCb2HkxgS2kwkSZgnlgCX9xLqYgJ5sC6fwC+"
    "beZGPN0r080PubqblQAMlvyxMLjMzXhTGzr0Ng4K6JOeefcQF218OZ3KHXAutMlW+2dbof"
    "ol1IyOxa5nkF8Nfu3y65xdDUuRBiLRgouMjrAzuIWhcUl0taU7RZ/7srEuTQpyqlo0qR7p"
    "9sS4Id3c4N6cvVWEa/EcnWiKOjNBaaKCIGORJgPJhfeWy/uyJDJeSC7HE+VCiVzqK9KwNF"
    "sUUOyF5HESomTcJFDZMXnq6Dmm14KayRPtomkXTa1F05bTz19OJ6m/bg24NWirP1H9HUiR"
    "cOMVn4i5vLIY8L2aZ+H6uTyVkOIso5xwc00ytKT8Y59yy84iaxlnw14uxWlSSkq58OrXN6"
    "EDcLxNhM+eCJNfQN22QqK/mzS4d3rpnoJWq6egVfQUNN5TaJD3BOkwgH6QRz2MzS7e30AH"
    "lPQY4oR2R2+RJLWD3XGENDkJ7zP3MyRFuZ/LK3N/mGjs8PD3+4lw8RuniB3N3mbhZ8/CbC"
    "3yzw0ysWxzjNm4VoO3or+bb+8GYWOIksmxFPZpir06FHvlFHs5imtAfA9vXGQ1AZm2allG"
    "LKELkNME49bgGH/RercGP71byo8NZddiEDx4fsGuUrUShc1xrsOd1akyShSYtMhB3wvS49"
    "CjNSXAJbu0bJfhOaeG+wK6Xam77n4Mp9OrVPdjeJltb9xdD8cUMMdLlRCBYhv/pdqfnZra"
    "2n8ftX9Z70fGVX0GaNYD0jtSP3chyusd1uCK3HYuaMoUnhAOxK/27PAiHRyzETzJ4ucEDy"
    "O/7AZi+sDVDJpk8X+Cltvu0gzzAC88H6Ilfg83nOMl9Qhgq6h6yHRqDo9f2aZGxT542KYw"
    "eWnQ8GhQMCoYRoPb0eB8rKZWXnHDtTG14ysFstSkLFRM7WX+TBpAH1mropIiHqksKIDQaV"
    "+vPLBUVrWJfod+UPhWYPk5UzI5zmOm3q13Xq86sOdO7Oyn0QBirH6cAPdyTqczEogLXqH8"
    "+3Y6KXl9UphkQN5hGuBnG1nkVGHvvH09TKwVFFnU1e8qZF9LOE2//8hu8OLvKjz9ByzD99"
    "o="
)
