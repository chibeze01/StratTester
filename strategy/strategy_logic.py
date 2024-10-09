 
# strategy/strategy_logic.py
import pandas as pd

def make_decision(price_data):
    # Simple Moving Average Crossover Strategy Example
    close_price = price_data['close']
    timestamp = price_data['timestamp']

    # For demonstration, we'll use a simplistic condition
    if close_price > 100:
        action = 'buy'
    else:
        action = 'sell'

    decision = {
        'action': action,
        'quantity': 10,  # Example fixed quantity
        'stop_loss': close_price - 5,
        'take_profit': close_price + 5
    }
    return decision

def prevent_look_ahead_bias(data: pd.DataFrame, tick_date: any, time_field_name: str) -> pd.DataFrame:
    """
    Prevent look-ahead bias by truncating data to ensure only historical information is accessible.
    
    Parameters:
    - data: The dataset (e.g., Pandas DataFrame) containing historical data.
    - tick_date: The current date/time of the tick being processed.
    - time_field_name: The name of the column representing the timestamp in the data.
    
    Returns:
    - A truncated version of the data containing only rows with timestamps before or equal to tick_date.
    """
    truncated_data = data[data[time_field_name] <= tick_date]
    return truncated_data