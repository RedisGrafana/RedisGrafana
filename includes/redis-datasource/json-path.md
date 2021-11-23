!!! note "JSONPath"

    RedisJSON decides which syntax to use depending on the first character of the path query. If the query starts with the character $ it is considered as a JSONPath query. Otherwise it is interpreted as a legacy path syntax.

    [Learn more in the documentation](https://oss.redis.com/redisjson/path/).
