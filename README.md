# Introduction

A demo of the DLT tool.

# Prerequisites

1. Docker compose
2. A REST client (to interact with the APIs)

# Architecture

There are 3 components:

1. ui
2. db
3. model

## The `ui` Component

This component initialises the `db` component. 

## The `db` Component

This is a postgresql database. There is a database named `demo`. Inside this database is a table named `message` that has the following entries:

| id | text          | sentiment | confidence |
|----|---------------|-----------|------------|
| 1  | I am so happy |           |            |
| 2  | I am so sad   |           |            |
| 3  | I am fine     |           |            |

## The `model` Component

This component has a `predict` endpoint that takes a `text` and returns the `sentiment` and `confidence`.

# API Documentation
See [api.http](api.http) for example API calls.