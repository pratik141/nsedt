<a id="equity"></a>

# equity

get data for Equity

<a id="equity.get_companyinfo"></a>

#### get\_companyinfo

```python
def get_companyinfo(symbol, response_type="panda_df")
```

**Arguments**:

- `symbol` _str_ - stock symbol.
- `response_type` _str, Optional_ - define the response type panda_df | json. Default panda_df
  

**Returns**:

  Pandas DataFrame: df containing company info
  or
- `Json` - json containing company info

<a id="equity.get_marketstatus"></a>

#### get\_marketstatus

```python
def get_marketstatus(response_type="panda_df")
```

**Arguments**:

- `response_type` _str, Optional_ - define the response type panda_df | json. Default panda_df

**Returns**:

  Pandas DataFrame: df containing market status
  Json : Json containing market status

<a id="equity.get_price"></a>

#### get\_price

```python
def get_price(start_date,
              end_date,
              symbol=None,
              input_type="stock",
              series="EQ")
```

Create threads for different requests, parses data, combines them and returns dataframe

**Arguments**:

- `start_date` _datetime.datetime_ - start date
- `end_date` _datetime.datetime_ - end date
- `input_type` _str_ - Either 'stock' or 'index'
- `symbol` _str, optional_ - stock symbol. Defaults to None. TODO: implement for index`

**Returns**:

  Pandas DataFrame: df containing data for symbol of provided date range

<a id="equity.get_corpinfo"></a>

#### get\_corpinfo

```python
def get_corpinfo(start_date, end_date, symbol=None, response_type="panda_df")
```

Create threads for different requests, parses data, combines them and returns dataframe

**Arguments**:

- `start_date` _datetime.datetime_ - start date
- `end_date` _datetime.datetime_ - end date
- `symbol` _str, optional_ - stock symbol. Defaults to None.

**Returns**:

  Pandas DataFrame: df containing data for symbol of provided date range
  or
- `Json` - json containing data for symbol of provided date range

<a id="equity.get_event"></a>

#### get\_event

```python
def get_event(start_date=None, end_date=None, index="equities")
```

**Arguments**:

- `start_date` _datetime.datetime,optional_ - start date
- `end_date` _datetime.datetime,optional_ - end date

**Returns**:

  Pandas DataFrame: df containing event of provided date range

<a id="equity.get_chartdata"></a>

#### get\_chartdata

```python
def get_chartdata(symbol, preopen=False, response_type="panda_df")
```

**Arguments**:

- `symbol` _str_ - stock symbol.

**Returns**:

  Pandas DataFrame: df containing chart data of provided date

<a id="equity.get_symbols_list"></a>

#### get\_symbols\_list

```python
def get_symbols_list()
```

**Arguments**:

  No arguments needed
  

**Returns**:

  List of stock or equity symbols

<a id="__init__"></a>

