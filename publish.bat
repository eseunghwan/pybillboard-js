rmdir /s /q build
rmdir /s /q dist
rmdir /s /q pybillboard_js.egg-info

python3 setup.py sdist bdist_wheel
twine upload dist/* -u eseunghwan -p 2@etmdghks
