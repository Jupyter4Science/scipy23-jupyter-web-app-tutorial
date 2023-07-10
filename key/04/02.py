

plt.xlabel('Year')
plt.ylabel('Temperature')
plt.plot(selected['Year'], selected['Temperature'])  # plt.plot(selected_range['Year'], selected_range['Temperature'])
plt.plot(selected['Year'], selected['Savitzky-Golay']) # plt.plot(selected_range['Year'], selected_range['Savitzky-Golay'])
plt.show()
