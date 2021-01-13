Codeforces API
[![License](https://img.shields.io/github/license/VadVergasov/CodeforcesApiPy)](https://github.com/VadVergasov/CodeforcesApiPy/blob/master/LICENSE)
[![Stars](https://img.shields.io/github/stars/VadVergasov/CodeforcesApiPy)](https://github.com/VadVergasov/CodeforcesApiPy/stargazers)
[![Forks](https://img.shields.io/github/forks/VadVergasov/CodeforcesApiPy)](https://github.com/VadVergasov/CodeforcesApiPy/network/members)
[![Issues](https://img.shields.io/github/issues/VadVergasov/CodeforcesApiPy)](https://github.com/VadVergasov/CodeforcesApiPy/issues)
[![Publish to PyPI and TestPyPI](https://github.com/VadVergasov/CodeforcesApiPy/workflows/Publish%20to%20PyPI%20and%20TestPyPI/badge.svg?branch=master)](https://pypi.org/project/CodeforcesApiPy/)
[![Generate wiki](https://github.com/VadVergasov/CodeforcesApiPy/workflows/Generate%20wiki/badge.svg?branch=master)](https://github.com/VadVergasov/CodeforcesApiPy/wiki)
[![Downloads](https://static.pepy.tech/personalized-badge/codeforcesapipy?period=total&units=international_system&left_color=black&right_color=blue&left_text=Total%20downloads)](https://pepy.tech/project/codeforcesapipy)
==========

Installing
----------

With pip:

```bash
pip install CodeforcesApiPy
```

From the repository:

```bash
git clone https://github.com/VadVergasov/CodeforcesApiPy.git
cd codeforcesapipy
python3 setup.py install
```

Using
---------

```python
import codeforces_api

cf_api = codeforces_api.CodeforcesApi(api_key, secret) #Authorized access to api.
anonim_cf_api = codeforces_api.CodeforcesApi() #Unauthorized access to api.

parser = codeforces_api.CodeforcesParser() #Create parser.
```

Wiki
--------
Here is link to the [wiki](https://github.com/VadVergasov/CodeforcesApiPy/wiki) for more details.

Examples
---------

Here are some examples of using this library:

* [A2OJ](https://github.com/subodhk01/a2oj) by subodhk01 - allows you to look at your ladder progress.
* [cf_utils](https://github.com/xennygrimmato/cf_utils) by xennygrimmato - allows you to find common solved problems.
