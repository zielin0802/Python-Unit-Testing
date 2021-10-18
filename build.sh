echo 'Running unit tests...'
python assignment1/test_fibonacci.py
python assignment1/test_volume.py

echo 'Running modules (doctest)...'
python assignment1/fibonacci.py
python assignment1/volume.py

echo 'Running flake8...'
python_scripts=(
  '/assignment1/fibonacci.py'
  '/assignment1/volume.py'
  'assignment1/test_fibonacci.py'
  'assignment1/test_volume.py'
)
export num_scripts=${#python_scripts[@]}
for ((i=0; i < num_scripts; i++)) do
  flake8 ./${python_scripts[i]}
  exit_status=$?
  if [ $exit_status -ne 0 ]; then
    exit $exit_status
  fi
done