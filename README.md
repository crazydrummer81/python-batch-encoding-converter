# Python batch files encoding converter

### Usage

##### Specify source and target folders and encodings.

```python
source_folder = 'D:\\Temp\\some_folder\\unconverted'
target_folder = 'D:\\Temp\\some_folder\\utf-8'
target_encoding = 'utf-8'
target_encoding_str = 'utf-8' # Need for check with OS.
```
```python
source_folder = 'D:\\Temp\\some_folder\\unconverted'
target_folder = 'D:\\Temp\\some_folder\\utf-8'
target_encoding = 'cp1261'
target_encoding_str = 'windows-1251' # Need for check with OS.
```

##### Run code from terminal

```
py encoding-converter.py
```