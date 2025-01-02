# إنشاء بيئة عمل
```bash
python -m venv env
env\Scripts\activate
cd env
mkdir src
cd src
```
# تثبيت الأدوات داخل بيئة العمل
```bash
pip install setuptools wheel twine
```
# بناء المكتبة
```bash
python setup.py sdist bdist_wheel
```
# رفع المكتبة
```bash
twine upload dist/* -u __token__ -p <your_api_token>
```
