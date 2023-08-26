# Additional data for the years of the presidency of each U.S. President
import matplotlib.pyplot as plt
import numpy as np

presidents_data = [
    {'name': 'George Washington', 'birth_year': 1732, 'death_year': 1799},
    {'name': 'John Adams', 'birth_year': 1735, 'death_year': 1826},
    {'name': 'Thomas Jefferson', 'birth_year': 1743, 'death_year': 1826},
    {'name': 'James Madison', 'birth_year': 1751, 'death_year': 1836},
    {'name': 'James Monroe', 'birth_year': 1758, 'death_year': 1831},
    {'name': 'John Quincy Adams', 'birth_year': 1767, 'death_year': 1848},
    {'name': 'Andrew Jackson', 'birth_year': 1767, 'death_year': 1845},
    {'name': 'Martin Van Buren', 'birth_year': 1782, 'death_year': 1862},
    {'name': 'William Henry Harrison', 'birth_year': 1773, 'death_year': 1841},
    {'name': 'John Tyler', 'birth_year': 1790, 'death_year': 1862},
    {'name': 'James K. Polk', 'birth_year': 1795, 'death_year': 1849},
    {'name': 'Zachary Taylor', 'birth_year': 1784, 'death_year': 1850},
    {'name': 'Millard Fillmore', 'birth_year': 1800, 'death_year': 1874},
    {'name': 'Franklin Pierce', 'birth_year': 1804, 'death_year': 1869},
    {'name': 'James Buchanan', 'birth_year': 1791, 'death_year': 1868},
    {'name': 'Abraham Lincoln', 'birth_year': 1809, 'death_year': 1865},
    {'name': 'Andrew Johnson', 'birth_year': 1808, 'death_year': 1875},
    {'name': 'Ulysses S. Grant', 'birth_year': 1822, 'death_year': 1885},
    {'name': 'Rutherford B. Hayes', 'birth_year': 1822, 'death_year': 1893},
    {'name': 'James A. Garfield', 'birth_year': 1831, 'death_year': 1881},
    {'name': 'Chester A. Arthur', 'birth_year': 1829, 'death_year': 1886},
    {'name': 'Grover Cleveland', 'birth_year': 1837, 'death_year': 1908},
    {'name': 'Benjamin Harrison', 'birth_year': 1833, 'death_year': 1901},
    {'name': 'William McKinley', 'birth_year': 1843, 'death_year': 1901},
    {'name': 'Theodore Roosevelt', 'birth_year': 1858, 'death_year': 1919},
    {'name': 'William Howard Taft', 'birth_year': 1857, 'death_year': 1930},
    {'name': 'Woodrow Wilson', 'birth_year': 1856, 'death_year': 1924},
    {'name': 'Warren G. Harding', 'birth_year': 1865, 'death_year': 1923},
    {'name': 'Calvin Coolidge', 'birth_year': 1872, 'death_year': 1933},
    {'name': 'Herbert Hoover', 'birth_year': 1874, 'death_year': 1964},
    {'name': 'Franklin D. Roosevelt', 'birth_year': 1882, 'death_year': 1945},
    {'name': 'Harry S. Truman', 'birth_year': 1884, 'death_year': 1972},
    {'name': 'Dwight D. Eisenhower', 'birth_year': 1890, 'death_year': 1969},
    {'name': 'John F. Kennedy', 'birth_year': 1917, 'death_year': 1963},
    {'name': 'Lyndon B. Johnson', 'birth_year': 1908, 'death_year': 1973},
    {'name': 'Richard Nixon', 'birth_year': 1913, 'death_year': 1994},
    {'name': 'Gerald Ford', 'birth_year': 1913, 'death_year': 2006},
    {'name': 'Jimmy Carter', 'birth_year': 1924, 'death_year': None},  # Still alive as of September 2021
    {'name': 'Ronald Reagan', 'birth_year': 1911, 'death_year': 2004},
    {'name': 'George H. W. Bush', 'birth_year': 1924, 'death_year': 2018},
    {'name': 'Bill Clinton', 'birth_year': 1946, 'death_year': None},  # Still alive as of September 2021
    {'name': 'George W. Bush', 'birth_year': 1946, 'death_year': None},  # Still alive as of September 2021
    {'name': 'Barack Obama', 'birth_year': 1961, 'death_year': None},  # Still alive as of September 2021
    {'name': 'Donald Trump', 'birth_year': 1946, 'death_year': None},  # Still alive as of September 2021
    {'name': 'Joe Biden', 'birth_year': 1942, 'death_year': None}  # Still alive as of September 2021
]

# Sorting the data by birth_year for a chronological timeline
presidents_data_sorted = sorted(presidents_data, key=lambda x: x['birth_year'])

# Generate the timeline
timeline = []
for president in presidents_data_sorted:
    timeline.append(f"{president['name']}: {president['birth_year']} - {president['death_year'] if president['death_year'] else 'N/A'}")

timeline


# Data preparation
names = [president['name'] for president in presidents_data_sorted]
birth_years = [president['birth_year'] for president in presidents_data_sorted]
death_years = [president['death_year'] if president['death_year'] else 2023 for president in presidents_data_sorted]

presidency_years = [
    {'name': 'George Washington', 'start_year': 1789, 'end_year': 1797},
    {'name': 'John Adams', 'start_year': 1797, 'end_year': 1801},
    {'name': 'Thomas Jefferson', 'start_year': 1801, 'end_year': 1809},
    {'name': 'James Madison', 'start_year': 1809, 'end_year': 1817},
    {'name': 'James Monroe', 'start_year': 1817, 'end_year': 1825},
    {'name': 'John Quincy Adams', 'start_year': 1825, 'end_year': 1829},
    {'name': 'Andrew Jackson', 'start_year': 1829, 'end_year': 1837},
    {'name': 'Martin Van Buren', 'start_year': 1837, 'end_year': 1841},
    {'name': 'William Henry Harrison', 'start_year': 1841, 'end_year': 1841},
    {'name': 'John Tyler', 'start_year': 1841, 'end_year': 1845},
    {'name': 'James K. Polk', 'start_year': 1845, 'end_year': 1849},
    {'name': 'Zachary Taylor', 'start_year': 1849, 'end_year': 1850},
    {'name': 'Millard Fillmore', 'start_year': 1850, 'end_year': 1853},
    {'name': 'Franklin Pierce', 'start_year': 1853, 'end_year': 1857},
    {'name': 'James Buchanan', 'start_year': 1857, 'end_year': 1861},
    {'name': 'Abraham Lincoln', 'start_year': 1861, 'end_year': 1865},
    {'name': 'Andrew Johnson', 'start_year': 1865, 'end_year': 1869},
    {'name': 'Ulysses S. Grant', 'start_year': 1869, 'end_year': 1877},
    {'name': 'Rutherford B. Hayes', 'start_year': 1877, 'end_year': 1881},
    {'name': 'James A. Garfield', 'start_year': 1881, 'end_year': 1881},
    {'name': 'Chester A. Arthur', 'start_year': 1881, 'end_year': 1885},
    {'name': 'Grover Cleveland', 'start_year': 1885, 'end_year': 1889},
    {'name': 'Benjamin Harrison', 'start_year': 1889, 'end_year': 1893},
    {'name': 'Grover Cleveland', 'start_year': 1893, 'end_year': 1897},
    {'name': 'William McKinley', 'start_year': 1897, 'end_year': 1901},
    {'name': 'Theodore Roosevelt', 'start_year': 1901, 'end_year': 1909},
    {'name': 'William Howard Taft', 'start_year': 1909, 'end_year': 1913},
    {'name': 'Woodrow Wilson', 'start_year': 1913, 'end_year': 1921},
    {'name': 'Warren G. Harding', 'start_year': 1921, 'end_year': 1923},
    {'name': 'Calvin Coolidge', 'start_year': 1923, 'end_year': 1929},
    {'name': 'Herbert Hoover', 'start_year': 1929, 'end_year': 1933},
    {'name': 'Franklin D. Roosevelt', 'start_year': 1933, 'end_year': 1945},
    {'name': 'Harry S. Truman', 'start_year': 1945, 'end_year': 1953},
    {'name': 'Dwight D. Eisenhower', 'start_year': 1953, 'end_year': 1961},
    {'name': 'John F. Kennedy', 'start_year': 1961, 'end_year': 1963},
    {'name': 'Lyndon B. Johnson', 'start_year': 1963, 'end_year': 1969},
    {'name': 'Richard Nixon', 'start_year': 1969, 'end_year': 1974},
    {'name': 'Gerald Ford', 'start_year': 1974, 'end_year': 1977},
    {'name': 'Jimmy Carter', 'start_year': 1977, 'end_year': 1981},
    {'name': 'Ronald Reagan', 'start_year': 1981, 'end_year': 1989},
    {'name': 'George H. W. Bush', 'start_year': 1989, 'end_year': 1993},
    {'name': 'Bill Clinton', 'start_year': 1993, 'end_year': 2001},
    {'name': 'George W. Bush', 'start_year': 2001, 'end_year': 2009},
    {'name': 'Barack Obama', 'start_year': 2009, 'end_year': 2017},
    {'name': 'Donald Trump', 'start_year': 2017, 'end_year': 2021},
    {'name': 'Joe Biden', 'start_year': 2021, 'end_year': 2023}  # Assumed to be in office until 2023 based on data cut-off
]

# Generate the overlay plot
plt.figure(figsize=(20, 15))
plt.scatter(birth_years, np.arange(len(names)), color='blue', label='Birth Year')
plt.scatter(death_years, np.arange(len(names)), color='red', label='Death Year')

# Overlay presidency years
for president in presidency_years:
    if president['name'] in names:
        i = names.index(president['name'])
        plt.plot([president['start_year'], president['end_year']], [i, i], color='green', linewidth=4, alpha=0.7, label='Presidency Years' if president['name'] == 'George Washington' else '')

# Add labels and lines
print(birth_years)
print(names)
print(presidency_years)

# Access and print the whole object with Bill Clinton
bill_clinton_object = next((president for president in presidency_years if president['name'] == 'Bill Clinton'), None)
barack_obama_start_year = next((president['start_year'] for president in presidency_years if president['name'] == 'Barack Obama'), None)
print(barack_obama_start_year)

for i, (birth, death, name) in enumerate(zip(birth_years, death_years, names)):
    start_year = next((president['start_year'] for president in presidency_years if president['name'] == name), None)
    plt.text(birth - 10, i, str(birth), ha='right', va='center', color='blue')
    plt.text(death + 5, i, str(death) if death != 2023 else "N/A", ha='left', va='center', color='red')
    plt.plot([birth, death], [i, i], color='gray', linestyle='--')
    plt.text(start_year - 5, i, name, ha='right', va='center', backgroundcolor='0.75')

plt.yticks([])
plt.xlabel('Year')
plt.title('Timeline of U.S. Presidents by Birth, Death, and Presidency Years')
plt.legend()
plt.grid(True, axis='x')

plt.show()
