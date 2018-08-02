python3 setup.py sdist bdist_wheel
twine upload dist/* -u eseunghwan -p 2@etmdghks

rm -rf build dist pybillboard_js.egg-info