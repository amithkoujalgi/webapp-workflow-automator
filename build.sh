rm -rf build dist *.egg-info
python setup.py bdist_wheel
rm -rf build *.egg-info
curr_dir=$(pwd)
whl_file=$(cd ./dist/ && ls *.whl)
whl_file="$curr_dir/dist/$whl_file"
echo "\n[Wheel build complete]\n\nTo install the wheel, run: \n\npip install -U $whl_file"