Usage
==========

Installing
----------

With pip:

```bash
pip install CodeforcesApiPy
```

From repository:

```bash
git clone https://github.com/VadVergasov/CodeforcesApiPy.git
cd codeforcesapipy
python3 setup.py install
```

Using
---------

```python
import codeforces_api

cf_api = codeforces_api.CodeforcesApi(api_key, secret) #Authorized access.
anonim_cf_api = codeforces_api.CodeforcesApi() #Unauthorized access.

parser = codeforces_api.CodeforcesParser() #Parse some info.
```
