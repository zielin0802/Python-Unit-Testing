echo 'Running nosetest unit tests...'
test_dirs=(
  'assignment1'
  'assignment3'
)
export num_dirs=${#test_dirs[@]}
for ((i=0; i < num_dirs; i++)) do
  nosetests ./${test_dirs[i]}
  exit_status=$?
  if [ $exit_status -ne 0 ]; then
    exit $exit_status
  fi
done

echo 'Running doctest...'
python assignment1/fibonacci.py
python assignment1/volume.py

echo 'Running pytest'
pytest assignment4/test_course.py -v

echo 'Running flake8...'
python_scripts=(
  'assignment1/fibonacci.py'
  'assignment1/volume.py'
  'assignment1/test_fibonacci.py'
  'assignment1/test_volume.py'
  'assignment3/sensor_check.py'
  'assignment3/test_sensor_check.py'
)
export num_scripts=${#python_scripts[@]}
for ((i=0; i < num_scripts; i++)) do
  flake8 ./${python_scripts[i]}
  exit_status=$?
  if [ $exit_status -ne 0 ]; then
    exit $exit_status
  fi
done