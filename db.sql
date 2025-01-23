CREATE TABLE "users"(
    "id" bigserial NOT NULL,
    "chat_id" INTEGER NOT NULL,
    "name" VARCHAR(30) NULL,
    "surname" VARCHAR(30) NOT NULL,
    "age" INTEGER NULL
);
ALTER TABLE "users" ADD PRIMARY KEY("id");
