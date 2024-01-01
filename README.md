# References
* [query_sets](https://docs.djangoproject.com/en/5.0/ref/models/querysets/)
* [database functions](https://docs.djangoproject.com/en/5.0/ref/models/database-functions/)

#  Errors

## mysqlclient
https://github.com/PyMySQL/mysqlclient/issues/584

mac os global environment run:

`brew install pkg-config`

in your virtualenv or other environment ->
```
export MYSQLCLIENT_LDFLAGS=$(pkg-config --libs mysqlclient)
export MYSQLCLIENT_CFLAGS=$(pkg-config --cflags mysqlclient)
pip install mysqlclient
```

