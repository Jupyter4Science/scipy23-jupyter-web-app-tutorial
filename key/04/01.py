
def on_window_size_change(change): # def on_window_size_change(change):
    global original_data, selected #     global original_data, selected
    original_data['Savitzky-Golay'] = savgol_filter(original_data['Temperature'], change['new'], poly_order.value) #     original_data['Savitzky-Golay'] = savgol_filter(original_data['Temperature'], window_size, poly_order)
    selected = original_data[(original_data['Year'] >= year_range.value[0]) & (original_data['Year'] <= year_range.value[1])] #     selected = original_data[(original_data['Year'] >= year_range.value[0]) & (original_data['Year'] <= year_range.value[1])]
