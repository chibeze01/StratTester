@echo off

mkdir backtester
cd backtester
echo. > __init__.py
echo. > backtester.py
echo. > data_loader.py
echo. > trade_executor.py
echo. > utils.py
echo. > config.py
cd ..

mkdir strategy
cd strategy
echo. > __init__.py
echo. > strategy.py
echo. > strategy_logic.py
echo. > requirements.txt
echo. > build_exe.sh
cd ..

mkdir data
cd data
echo. > historical_data.csv
mkdir processed
cd ..

mkdir logs
cd logs
echo. > backtester.log
echo. > strategy.log
cd ..

mkdir tests
cd tests
echo. > test_backtester.py
echo. > test_strategy.py
echo. > test_trade_executor.py
cd ..

mkdir docs
cd docs
echo. > README.md
cd ..

echo. > requirements.txt
echo. > run_backtester.py

echo File structure created successfully.