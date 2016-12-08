# jsondiff

jsondiff is a simple tool to compare json objects with values or without values.
The source code is based on jscompare by [https://github.com/monsur/jsoncompare](https://github.com/monsur/jsoncompare)
with modification to be easier used by other developers.
For complex compare of json files, please refer other tools such as:

[https://github.com/bazaarvoice/json-regex-difftool](https://github.com/bazaarvoice/json-regex-difftool)

[https://github.com/ZoomerAnalytics/jsondiff](https://github.com/ZoomerAnalytics/jsondiff)


usage:

`from jsondiff import diff`

`a = {1:'hello', 2:'world', 6:'python'}`

`b = {1:'helllo', 2:1, 3:'readme'}`

`print(diff(a,b))` # Without values

[('DISCARD', '6 | '), ('ADD', ' | 3')]
	

`print(diff(a,b, True))` # With values

[('VALUE', '1 - hello | helllo'), ('TYPE', '2 - str, int'), ('VALUE', '2 - world | 1'), ('DISCARD', '6 | '), ('ADD', ' | 3')]