# indices

get data for indices

<a id="indices.get_price"></a>

#### get\_price

```python
def get_price(start_date, end_date, symbol, response_type="panda_df")
```

**Arguments**:

- `symbol` _str_ - stock symbol.
- `response_type` _str, Optional_ - define the response type panda_df | json. Default panda_df
  

**Returns**:

  Pandas DataFrame: df containing company info
  or
- `Json` - json containing company info

