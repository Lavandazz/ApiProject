from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "article" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(150) NOT NULL,
    "description" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "role" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "role" VARCHAR(100) NOT NULL UNIQUE
);
COMMENT ON TABLE "role" IS 'Модель роли (Админ, Пользователь)';
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "surname" VARCHAR(70) NOT NULL,
    "patronymic" VARCHAR(70) NOT NULL,
    "email" VARCHAR(25) NOT NULL UNIQUE,
    "password" VARCHAR(100) NOT NULL,
    "is_active" BOOL NOT NULL DEFAULT True
);
COMMENT ON TABLE "user" IS 'Модель пользователя';
CREATE TABLE IF NOT EXISTS "userrole" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "role_id" INT NOT NULL REFERENCES "role" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "userrole" IS 'Связь пользователя и роли';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmm1v2joUgP9KlE+9Uu8EaRjVvgVKN+5amFq6TdudIpMYsJrYLHHWoon/PttJiPN6yW"
    "7YiMYXF47PSY6fmPPi5rvqEhs6/gvDo8hyoPpK+a5i4PIP2alzRQXrdTLBBRTMhZEKJKW5"
    "Tz1gUSZeAMeHTGRD3/LQmiKCmRQHjsOFxGKKCC8TUYDR1wCalCwhXUGPTXz+wsQI2/AZ+v"
    "HX9aO5QNCxU84im99byE26WQvZGNNrocjvNjct4gQuTpTXG7oieKeNMOXSJcTQAxTyy1Mv"
    "4O5z76KFxisKPU1UQhclGxsuQOBQabl7MrAI5vyYN75Y4JLf5W+tq/f1y4uX+iVTEZ7sJP"
    "1tuLxk7aGhIDCZqVsxDygINQTGhBtFNHxsaXTDFfCK2e0MMviY01l8MawqfrEgAZhsmoYI"
    "uuDZdCBe0hX72u11Kni9N+6Gb4y7M6b1F18NYRs53OCTaEoL5zjUBKLsWQ7lDD6XbMOMWV"
    "uAVvCbjT7OuNOu7391ZGxnt8ZHQdTdRDM308nrWF3CPLyZDjJ0LQ/y9ZuA5uFesRmKXFgM"
    "OG2Z4WtHpi/iD8dJW2VrsKfY2USxpYr++HZ0PzNu36UewZUxG/EZLYU/lp69zGz03UWUD+"
    "PZG4V/VT5NJyNBkPh06Yk7JnqzTyr3CQSUmJg8mcCWwmAsjcFseQBfPEqhiAvmwHp8Ap5t"
    "5maIRsp081Ou5mYlAIOleCwcLnczSmp3pDjZCXllpvPInmlO/Tfo6F2LjxdQjLoYe2Kc81"
    "G3FPGnIymJiYtL5UyYdyTD8FKXYrTPhWV3kbXUQ62+JNfEKK6ka3kXxPOX92GrHD+VDL+8"
    "ZIh/AftWDLF+M/nt4PTS5UJnr3KhU1EudES5UCPuJaQDH3p+HvUgMrt+ewcdUFI+RAHtgV"
    "0iDmrHl9y28V6JpXGSO2Ts50iKYr+QV8b+INZoLvZf/P9AuPj5AN7U3U9R+JdHYb4Xxeca"
    "kVi2aWM03qt3q2jd8p2bH9SGKJm0pWNLU+zvQ7FfTrGfo7gG1CN44yKrDsi01YllyBK6AD"
    "l1MO4M2viL1np78NN6pfz4VHYv+v4T8QqyStVOTGzauQ8bq1NllMg3WZGDvhWExwFhNSXA"
    "JVlatsvwnDPDQwHd7dSmj7UG0+lN6kxlMM6eWz3cDkYMsMDLlBCFSRr/qdqfd02n2v8QtX"
    "/Z2Y+Mq7oHqHcGpHWTMlpfJOV1gzW4Ep29lB3KFHYIR+LXqXf4LSc4Zi14ksV/EzyO+NIM"
    "xHTDVQ+aZPEnQculuzTDPMBr4kG0xG/hRnAcM48Atoqqh8xJzfHxK0tqTOyBp10Ik7cGWx"
    "5bFAwLhqFxPzSuRmpq5xUfuNam1r5SIEtNikLF1H7PP5MM6CFrVVRSRDOVBQVIdE5vThxZ"
    "KKtKot+g5xf+w7+8z5RM2tlmar39+vWqhj3XsfOfRg2IkXo7AR6kT2d3pBAXvB3xz/10Uv"
    "JmRGKSAfmA2QI/28ii54qDfPrlOLFWUOSrrn4JJfu+yXn61QZ+gUG9vr359LL9AZ5njJQ="
)
