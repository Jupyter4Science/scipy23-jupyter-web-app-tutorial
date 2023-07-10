
def on_value_change(change):
     print(f"Value was {change['old']} but is now {change['new']}")  # update this print statement to be more informative 

slider.observe(on_value_change, 'value') # something is missing here
