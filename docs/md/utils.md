# utils

utils for nsedt

<a id="utils.get_headers"></a>

#### get\_headers

```python
def get_headers()
```

**Arguments**:

  ---

**Returns**:

- `Json` - json containing nse header

<a id="utils.get_cookies"></a>

#### get\_cookies

```python
def get_cookies()
```

**Arguments**:

  ---

**Returns**:

- `Json` - json containing nse cookies

<a id="utils.fetch_url"></a>

#### fetch\_url

```python
def fetch_url(url, cookies, key=None, response_type="panda_df")
```

**Arguments**:

- `url` _str_ - URL to fetch
- `cookies` _str_ - NSE cokies
  key (str, Optional):

**Returns**:

  Pandas DataFrame: df containing url data

<a id="utils.data_format"></a>

# utils.data\_format

return data in specific format

<a id="utils.data_format.price"></a>

#### price

```python
def price(result)
```

**Arguments**:

- `result` _Pandas DataFrame_ - result

**Returns**:

  Pandas DataFrame: df containing data in specific format

<a id="utils.data_format.indices"></a>

#### indices

```python
def indices(data_json)
```

**Arguments**:

- `data_json` _json_ - data in json format

**Returns**:

  Pandas DataFrame: df with indexCloseOnlineRecords and indexTurnoverRecords

